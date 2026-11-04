import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def file_hash(file):
    digest = hashlib.sha256()
    with file.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def structure(value):
    if isinstance(value, dict):
        return {key: structure(item) for key, item in value.items() if key not in ("description", "title")}
    if isinstance(value, list):
        return [structure(item) for item in value]
    return value


def measure(stock, patched, model):
    records = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            self.respond(b'{"data":[]}', "application/json")

        def do_POST(self):
            raw = self.rfile.read(int(self.headers.get("Content-Length", 0)))
            if self.headers.get("Content-Encoding") == "gzip":
                raw = gzip.decompress(raw)
            body = json.loads(raw)
            if "count_tokens" in self.path:
                self.respond(b'{"input_tokens":1}', "application/json")
                return
            records.append(body)
            message = {
                "id": "msg_local_fixture", "type": "message", "role": "assistant",
                "model": body.get("model"), "content": [], "stop_reason": None,
                "stop_sequence": None, "usage": {"input_tokens": 1, "output_tokens": 1},
            }
            events = [
                {"type": "message_start", "message": message},
                {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}},
                {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "PONG"}},
                {"type": "content_block_stop", "index": 0},
                {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": None}, "usage": {"output_tokens": 5}},
                {"type": "message_stop"},
            ]
            stream = "".join("event: " + event["type"] + "\ndata: " + json.dumps(event) + "\n\n" for event in events)
            self.respond(stream.encode(), "text/event-stream")

        def respond(self, raw, content_type):
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

    with tempfile.TemporaryDirectory(prefix="lcc-text-", dir="/tmp") as directory:
        root = Path(directory)
        config = root / "config"
        cwd = root / "cwd"
        config.mkdir()
        cwd.mkdir()
        key = "local-fixture-no-real-credential"
        (config / ".claude.json").write_text(json.dumps({
            "hasCompletedOnboarding": True,
            "customApiKeyResponses": {"approved": [key[-20:]], "rejected": []},
        }))
        (config / "settings.json").write_text(json.dumps({
            "disableAllHooks": True, "enabledPlugins": {}, "autoMemoryEnabled": False,
            "enableAllProjectMcpServers": False, "skipDangerousModePermissionPrompt": True,
        }))
        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        env = {key: os.environ[key] for key in ("USER", "LOGNAME", "SHELL", "PATH", "LANG") if key in os.environ}
        env.update(
            HOME=str(root), TERM="xterm-256color", CLAUDE_CONFIG_DIR=str(config),
            ANTHROPIC_API_KEY=key, ANTHROPIC_BASE_URL=f"http://127.0.0.1:{server.server_port}",
            DISABLE_AUTOUPDATER="1", DISABLE_TELEMETRY="1", DISABLE_ERROR_REPORTING="1",
            CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1", CLAUDE_CODE_DISABLE_AUTO_MEMORY="1",
            CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING="1", CLAUDE_CODE_DISABLE_CHROME="1",
            CLAUDE_CODE_DISABLE_REMOTE_CONTROL="1", CLAUDE_CODE_DISABLE_FAST_MODE="1",
        )
        flags = [
            "--print", "--no-session-persistence", "--system-prompt-snapshot", "off",
            "--model", model, "--effort", "medium", "--strict-mcp-config",
            "--mcp-config", '{"mcpServers":{}}', "--no-chrome", "--tools",
            "Agent,AskUserQuestion,Bash,Edit,Glob,Grep,Read,Skill,Write",
            "--dangerously-skip-permissions", "Reply with exactly PONG.",
        ]
        results = {}
        try:
            for arm, binary in (("stock", stock), ("lcc", patched)):
                start = len(records)
                process = subprocess.run(
                    [str(binary), *flags], env=env, cwd=cwd, stdin=subprocess.DEVNULL,
                    capture_output=True, text=True, timeout=90,
                )
                if process.returncode != 0 or process.stdout.strip() != "PONG":
                    raise RuntimeError(f"{arm} fixture failed: {process.returncode}\n{process.stdout}\n{process.stderr}")
                requests = [body for body in records[start:] if body.get("tools") and body.get("model") == model]
                if len(requests) != 1:
                    raise RuntimeError(f"Expected one {arm} model request, received {len(requests)}")
                body = requests[0]
                tools = {tool["name"]: tool for tool in body["tools"]}
                if len(tools) != len(body["tools"]):
                    raise RuntimeError("Duplicate tool names")
                if str(Path.home()) in canonical(body["system"]) + canonical(body["messages"]):
                    raise RuntimeError("Real home path appeared in isolated context")
                results[arm] = {
                    "systemCharacters": sum(len(block["text"]) for block in body["system"]),
                    "toolDescriptionCharacters": sum(len(tool.get("description", "")) for tool in tools.values()),
                    "toolNames": list(tools),
                    "schemaStructureSha256": hashlib.sha256(canonical(structure({name: tool.get("input_schema", {}) for name, tool in tools.items()})).encode()).hexdigest(),
                    "binarySha256": file_hash(binary),
                    "perToolCharacters": {name: len(tool.get("description", "")) for name, tool in tools.items()},
                }
            if results["stock"]["toolNames"] != results["lcc"]["toolNames"]:
                raise RuntimeError("Offered tools differ between arms")
            if results["stock"]["schemaStructureSha256"] != results["lcc"]["schemaStructureSha256"]:
                raise RuntimeError("Tool schema structure differs between arms")
            return {
                "model": model, "effort": "medium", "unit": "Unicode code points in decoded strings",
                "syntheticResponse": True, "externalModelRequestsForwarded": 0, "arms": results,
            }
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture Claude Code prompt text through a localhost SSE fixture.")
    parser.add_argument("--stock", type=Path, required=True)
    parser.add_argument("--patched", type=Path, required=True)
    parser.add_argument("--model", default="claude-opus-5-5")
    parser.add_argument("--out", type=Path, required=True)
    arguments = parser.parse_args()
    arguments.out.write_text(json.dumps(measure(arguments.stock.resolve(strict=True), arguments.patched.resolve(strict=True), arguments.model), indent=2) + "\n")
