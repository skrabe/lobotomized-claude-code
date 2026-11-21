<!--
name: 'Data: tools-external.d.ts'
description: Text asset tools-external.d.ts that Claude Code loads by path from its bundle.
ccVersion: 2.1.330
-->
// The inputs of the built-in tools this build has, from each tool's
// input schema. Merges into ToolCallInput (BuiltinToolInputs) so
// \`e.tool === "Bash"\` narrows to the tool's arguments.
declare module 'claude-code' {
  interface BuiltinToolInputs {
    Agent: {
      description: string
      prompt: string
      subagent_type?: string
      model?: "sonnet" | "opus" | "haiku" | "fable"
      effort?: "low" | "medium" | "high" | "xhigh" | "max"
      run_in_background?: boolean
      name?: string
      team_name?: string
      mode?: "acceptEdits" | "auto" | "bypassPermissions" | "default" | "dontAsk" | "plan" | "bubble"
      isolation?: "worktree" | "remote"
    }
    AppifactRepl: {
      skill?: string
      artifact?: string
      code: string
    }
    Artifact: {
      action?: "publish" | "list" | "read" | "list_types" | "describe_type" | "quickstart" | "comments" | "reply" | "resolve" | "watch" | "unwatch" | "status" | "resume_replies" | "read_db" | "write_db" | "list_files" | "read_file" | "pin" | "unpin"
      type_query?: string
      type?: string
      intent?: "document" | "slides" | "design" | "other"
      design_systems?: boolean
      db_op?: "get" | "list" | "query" | "set" | "update" | "delete" | "batch"
      writes?: Array<{
        op: "set" | "update" | "delete"
        collection: string
        doc_id: string
        data?: {}
        file_path?: string
      }>
      collection?: string
      doc_id?: string
      as_level?: "view" | "interact" | "admin"
      query?: {
        where?: unknown[][]
        order_by?: {
          field: string
          direction?: "asc" | "desc"
        }
        limit?: number
        cursor?: string
      }
      data?: {}
      file_path?: string
      favicon?: string
      icon?: string
      edits?: Array<{
        old_str: string
        new_str: string
      }>
      files?: Array<{
        path: string
        contentType?: string
      }> | {}
      root?: string
      limit?: number
      page_token?: string
      scope?: "mine" | "shared" | "all"
      title?: string
      description?: string
      label?: string
      overwrite_unread?: string[]
      url?: string
      type_url?: string
      auto_open?: "at_create" | "after_first_write"
      prompt?: string
      force?: boolean
      pin?: boolean
      thread_id?: string
      text?: string
      cursor?: string
      acknowledge_duplicate?: boolean
      out_dir?: string
      path?: string
      paths?: string[]
      page?: boolean
      capabilities?: {}
      contract?: "latest" | string
    }
    ArtifactCheck: {
      action: "verify"
    }
    ArtifactComments: {
      action: "read" | "reply" | "resolve" | "watch"
      url?: string
      thread_id?: string
      text?: string
      cursor?: string
      acknowledge_duplicate?: boolean
      on?: boolean
      replies?: boolean
    }
    ArtifactData: {
      action: "get" | "list" | "query" | "set" | "update" | "delete" | "batch" | "profiles"
      url?: string
      writes?: Array<{
        op: "set" | "update" | "delete"
        collection: string
        doc_id: string
        data?: {}
        file_path?: string
      }>
      collection?: string
      ids?: string[]
      doc_id?: string
      query?: {
        where?: unknown[][]
        order_by?: {
          field: string
          direction?: "asc" | "desc"
        }
        limit?: number
        cursor?: string
      }
      data?: {}
      file_path?: string
      out_dir?: string
      as_level?: "view" | "interact" | "admin"
    }
    AskUserQuestion: {
      questions: Array<{
        question: string
        header: string
        options: Array<{
          label: string
          description: string
          preview?: string
        }>
        multiSelect: boolean
      }>
      answers?: {}
      annotations?: {}
      metadata?: {
        source?: string
      }
    }
    Bash: {
      command: string
      timeout?: number
      description?: string
      run_in_background?: boolean
      dangerouslyDisableSandbox?: boolean
    }
    ClaudeDesign: {
      operation: string
      arguments: {}
    }
    CronCreate: {
      cron: string
      prompt: string
      recurring?: boolean
      durable?: boolean
    }
    CronDelete: {
      id: string
    }
    CronList: {}
    DesignSync: {
      method: "list_projects" | "get_project" | "list_files" | "get_file" | "finalize_plan" | "write_files" | "delete_files" | "register_assets" | "unregister_assets" | "create_project" | "report_validate"
      projectId?: string
      path?: string
      writes?: string[]
      deletes?: string[]
      planId?: string
      files?: Array<{
        path: string
        localPath?: string
        data?: string
        encoding?: "base64"
        mimeType?: string
      }>
      paths?: string[]
      name?: string
      assets?: Array<{
        name: string
        path: string
        subtitle?: string
        viewport?: {
          width: number
          height?: number
        }
        group?: string
      }>
      localDir?: string
      counts?: {
        total: number
        bad: number
        thin: number
        variantsIdentical: number
        iterations: number
      }
    }
    Edit: {
      file_path: string
      old_string: string
      new_string: string
      replace_all?: boolean
    }
    "enable__mcp__claude-in-chrome": {
      task?: string
    }
    "enable__mcp__remote-devices__Claude_Browser": {
      task?: string
    }
    "enable__mcp__remote-devices__computer": {
      task?: string
    }
    EndConversation: {}
    EnterPlanMode: {}
    EnterWorktree: {
      name?: string
      path?: string
    }
    ExitPlanMode: {
      allowedPrompts?: Array<{
        tool: "Bash"
        prompt: string
      }>
    }
    ExitWorktree: {
      action: "keep" | "remove"
      discard_changes?: boolean
    }
    FetchInboxMessage: {
      file_id: string
    }
    GetGoal: {}
    GetTask: {
      taskId: string
    }
    Glob: {
      pattern: string
      path?: string
    }
    Grep: {
      pattern: string
      path?: string
      glob?: string
      output_mode?: "content" | "files_with_matches" | "count"
      "-B"?: number
      "-A"?: number
      "-C"?: number
      context?: number
      "-n"?: boolean
      "-i"?: boolean
      "-o"?: boolean
      type?: string
      head_limit?: number
      offset?: number
      multiline?: boolean
    }
    ListAgents: {
      channel?: string
      q?: string
      cursor?: string
    }
    ListConnectors: {
      keywords?: string[]
    }
    ListMcpResourcesTool: {
      server?: string
    }
    ListPlugins: {
      keywords?: string[]
    }
    ListSkills: {
      keywords?: string[]
    }
    LSP: {
      operation: "goToDefinition" | "findReferences" | "hover" | "documentSymbol" | "workspaceSymbol" | "goToImplementation" | "prepareCallHierarchy" | "incomingCalls" | "outgoingCalls"
      filePath: string
      line: number
      character: number
      query?: string
    }
    McpTaskResumePolling: {
      task_id: string
    }
    memory_list: {
      store?: string
      path_prefix?: string
      cursor?: string
    }
    memory_read: {
      store: string
      path: string
    }
    memory_write: {
      store: string
      path: string
      content: string
      if_version: string
    }
    Monitor: {
      description: string
      timeout_ms: number
      command?: string
      ws?: {
        url: string
        protocols?: string[]
      }
    }
    NotebookEdit: {
      notebook_path: string
      cell_id?: string
      new_source: string
      cell_type?: "code" | "markdown"
      edit_mode?: "replace" | "insert" | "delete"
    }
    OfferChromeSetup: {
      reason?: string
    }
    PauseGoal: {
      reason: string
    }
    Poll: {}
    PowerShell: {
      command: string
      timeout?: number
      description?: string
      run_in_background?: boolean
      dangerouslyDisableSandbox?: boolean
    }
    Projects: {
      method: "project_info" | "project_read" | "project_search" | "project_write" | "project_delete" | "project_memory_list" | "project_memory_read"
      path?: string
      content?: string
      local_path?: string
      present_to_user?: boolean
      query?: string
      n?: number
    }
    propose_skills: {
      proposals: Array<{
        name: string
        kind: "new" | "improvement"
        target?: string
        description: string
        evidence?: string[]
        edits?: Array<{
          old_string: string
          new_string: string
        }>
        skillMd?: string
      }>
    }
    PublishPlugin: {
      path: string
      destination?: "organization"
      description?: string
      replace?: boolean
      shown?: string[]
      question?: {
        digest: string
        title: string
        organization: {
          id: string
          name?: string
        }
        plugin: {
          name: string
          version?: string
        }
        folder: string
        mode: "new" | "replace"
        steps: string[]
        warnings: string[]
        writes?: {
          path: string
          text: string
        }
        sends: {
          files: number
          bytes: number
        }
        files: Array<{
          path: string
          bytes: number
          sha256: string
          runs: boolean
        }>
        staying: number
        stays: Array<{
          path: string
          why: "link" | "hard-link" | "ignored" | "secret" | "never" | "generated" | "special" | "backslash"
          words: string
        }>
        list: {
          sha256: string
          path?: string
        }
        unnamed?: {
          files: number
          stays: number
        }
      }
    }
    PushNotification: {
      message: string
      status?: "proactive"
    }
    Read: {
      file_path: string
      offset?: number
      limit?: number
      pages?: string
      allow_large?: boolean
    }
    ReadMcpResourceDirTool: {
      server: string
      uri: string
    }
    ReadMcpResourceTool: {
      server: string
      uri: string
    }
    ReadNotifications: {}
    ReadWidgetContext: {
      widget_id?: string
    }
    RefreshMcpTools: {
      server?: string
    }
    RemoteTrigger: {
      action: "list" | "get" | "create" | "update" | "run" | "create_webhook_trigger" | "list_runs" | "get_run_log"
      trigger_id?: string
      session_id?: string
      cursor?: string
      body?: {}
    }
    ReportFindings: {
      level?: "low" | "medium" | "high" | "xhigh" | "max"
      findings: Array<{
        file: string
        line?: number
        summary: string
        short_summary?: string
        failure_scenario: string
        category?: string
        severity?: "important" | "pre_existing" | "nit"
        verdict?: "CONFIRMED" | "PLAUSIBLE"
        outcome?: "fixed" | "skipped" | "no_change_needed"
      }>
    }
    request_computer: {
      task?: unknown
    }
    ScheduleWakeup: {
      delaySeconds?: number
      reason?: string
      prompt?: string
      stop?: boolean
      noop?: boolean
    }
    SearchMcpRegistry: {
      keywords: string[]
    }
    SearchPlugins: {
      keywords: string[]
    }
    SearchSkills: {
      keywords: string[]
    }
    self_hosted_runner_get_pool: {
      pool_id: string
    }
    self_hosted_runner_list_runners: {
      pool_id: string
    }
    self_hosted_runner_list_secrets: {
      pool_id: string
    }
    self_hosted_runner_list_sessions: {
      pool_id: string
      status_filter?: string
    }
    self_hosted_runner_read_health: {
      health_port?: number
    }
    self_hosted_runner_read_metrics: {
      health_port?: number
    }
    self_hosted_runner_requeue_session: {
      session_id: string
      runner_id: string
    }
    self_hosted_runner_spawn_local: {
      secret_file_path: string
      capacity?: number
      base_dir?: string
      health_port?: number
      log_path?: string
    }
    self_hosted_runner_tail_log: {
      log_path: string
      bytes?: number
    }
    SendFeedback: {
      type: "bug" | "idea" | "missing_capability"
      title: string
      details: string
      area?: string
      failure_mode?: "instruction_following" | "destructive_actions" | "code_quality" | "repetition_and_looping" | "model_regression" | "overconfidence_and_hallucination" | "context_and_memory" | "overeager" | "over_correction" | "stopping_short" | "dispute_or_decline" | "subagent_overspawn" | "tone_or_preachiness" | "excessive_questions" | "unwanted_scope" | "other"
      task_category?: "code_edit" | "debug" | "explain" | "plan" | "shell" | "search" | "review" | "other"
    }
    SendFile: {
      to: string
      files: string[]
      message?: string
    }
    SendMessage: {
      to: unknown & unknown
      summary?: string
      message: string
      notify_when_idle?: boolean
    }
    SendToProject: {
      project_name: string
      project_id?: string
      attach_git_remote: boolean
      proposal: {
        name?: string
        icon?: "Projects" | "Folder" | "Code" | "Database" | "HandHeart" | "Beaker" | "Wrench" | "Activity" | "Chart" | "Team" | "Users" | "Book" | "Box" | "Note" | "File" | "Lightbulb" | "Palette" | "Star" | "Flag" | "Home" | "Sun" | "Clock" | "Calendar" | "Scroll" | "Moon" | "MoonStars" | "SunHorizon" | "Owl" | "Atom" | "DNA" | "Orbit" | "Globe" | "Cloud" | "Hammer" | "Key" | "Lock" | "Camera" | "Microphone" | "CoffeeCup" | "Gift" | "Ghost" | "GraduationCap" | "Library" | "Spreadsheet" | "Slides" | "Checklist" | "Clipboard" | "Image" | "Bookmark" | "Bank" | "Signpost" | "MapPin" | "Mailbox" | "Heart" | "Lightning" | "Shapes" | "Goal" | "Scale" | "Eye" | "Binoculars" | "Bullhorn" | "PaperPlane" | "ChartLine" | "Timer"
        color?: "red" | "orange" | "green" | "aqua" | "blue" | "violet" | "magenta"
        summary?: string
        instructions?: string
        routines?: {
          name: string
          cron_expression: string
          prompt: string
          description?: string
        }[]
        sessions?: Array<{
          title: string
          prompt: string
          description: string
          basis: string
          who: "claude" | "you"
          produces: "pr" | "doc" | "decision"
        }>
        evidence?: {
          sessions_matched?: number
          sessions_considered?: number
          window_days?: number
        }
      }
    }
    SendToProjectContext: {}
    SendUserFile: {
      files: string[]
      caption?: string
      status: "normal" | "proactive"
      display?: "render" | "attach"
    }
    SendUserMessage: {
      message: string
    }
    SetGoal: {
      condition: string
      ask_user?: boolean
    }
    ShareOnboardingGuide: {
      mode: "check" | "update" | "create" | "delete"
      short_code?: string
    }
    ShowOnboardingRolePicker: {}
    Skill: {
      skill: string
      args?: string
    }
    SuggestConnectors: {
      uuids: string[]
    }
    SuggestPluginInstall: {
      contextLabel: string
      plugins: {
        pluginId: string
        pluginName: string
        description: string
        skills?: {
          name: string
          description?: string
        }[]
      }[]
      trigger?: "user_asked" | "proactive"
    }
    SuggestSkills: {
      keywords: string[]
      contextLabel?: string
      trigger?: "user_asked" | "proactive"
    }
    TaskCreate: {
      subject: string
      description: string
      activeForm?: string
      metadata?: {}
    }
    TaskGet: {
      taskId: string
    }
    TaskList: {}
    TaskStop: {
      task_id?: string
      shell_id?: string
    }
    TaskUpdate: {
      taskId: string
      subject?: string
      description?: string
      activeForm?: string
      status?: "pending" | "in_progress" | "completed" | "deleted"
      addBlocks?: string[]
      addBlockedBy?: string[]
      owner?: string
      metadata?: {}
    }
    TodoWrite: {
      todos: Array<{
        content: string
        status: "pending" | "in_progress" | "completed"
        activeForm: string
      }>
    }
    ToolSearch: {
      query: string
      max_results: number
    }
    WaitForMcpServers: {
      servers?: string[]
    }
    WebFetch: {
      url: string
      prompt: string
      offset?: number
    }
    WebSearch: {
      query: string
      allowed_domains?: string[]
      blocked_domains?: string[]
    }
    Workflow: {
      script?: string
      name?: string
      description?: string
      title?: string
      args?: unknown
      scriptPath?: string
      resumeFromRunId?: string
    }
    WrapUp: {
      recap: string
      ask?: string
      blocked?: boolean
      actions?: Array<{
        label: string
      } | {
        action: "verify" | "fix_ci" | "address_comments" | "resolve_conflicts"
      }>
    }
    Write: {
      file_path: string
      content: string
    }
    Yield: {}
  }
}

// The structured results of the same tools, from each tool's output
// schema. Merges into ToolCallResult (BuiltinToolResults) so after
// \`e.tool === "Bash"\` the \`result\` of \`next(e)\` is the tool's record.
declare module 'claude-code' {
  interface BuiltinToolResults {
    Agent: {
      agentId: string
      harnessNoteCount?: number
      harnessTailCount?: number
      harnessSectionHash?: string
      agentType?: string
      handback?: "send" | "flagged" | "withheld"
      handbackReport?: {
        text: string
        warning?: string
        toolUseId?: string
      }
      content: Array<{
        type: "text"
        text: string
        citations?: unknown[] | null
      }>
      resolvedModel?: string
      modelsUsed?: string[]
      totalToolUseCount: number
      totalDurationMs: number
      totalTokens: number
      usage: {
        input_tokens: number
        output_tokens: number
        cache_creation_input_tokens: number | null
        cache_read_input_tokens: number | null
        server_tool_use: {
          web_search_requests: number
          web_fetch_requests: number
        } | null
        service_tier: string | null
        cache_creation: {
          ephemeral_1h_input_tokens: number
          ephemeral_5m_input_tokens: number
        } | null
        inference_geo?: string | null
        speed?: string | null
        iterations?: unknown
        output_tokens_details?: {
          thinking_tokens?: number | null
        } | null
        fallback_credit?: unknown
      }
      toolsUsed?: string[]
      toolStats?: {
        readCount: number
        searchCount: number
        bashCount: number
        editFileCount: number
        linesAdded: number
        linesRemoved: number
        otherToolCount: number
        frameCount?: number
      }
      status: "completed"
      prompt: string
      worktreePath?: string
      worktreeBranch?: string
      inPlace?: {
        vcs: string
        branch?: string
      }
      canContinueAgent?: boolean
      taskCalls?: Array<{
        name: "TaskCreate" | "TaskUpdate"
        input: unknown
        result: string
      }>
    } | {
      status: "async_launched"
      isAsync?: true
      agentId: string
      description: string
      resolvedModel?: string
      modelsUsed?: string[]
      prompt: string
      outputFile: string
      canReadOutputFile?: boolean
      canContinueAgent?: boolean
      waitsAtPermissionPrompt?: boolean
      sharesCwd?: boolean
    } | {
      status: "remote_launched"
      taskId: string
      sessionUrl: string
      description: string
      prompt: string
      outputFile: string
    }
    AppifactRepl: {
      output: string
      stderr: string
      exitCode: number | null
      signal: string | null
      note?: string
      seen?: Array<{
        text: string
        images: Array<{
          media_type: "image/png" | "image/jpeg"
          data: string
        }>
      }>
      toolsUsed?: string[]
    }
    Artifact: {
      created_from_type: true
      already_created?: true
      url: string
      version: string
      owned?: boolean
      path?: string
      title?: string
      type: {
        url: string
        release: string
      }
      own_files: string[]
      type_files: string[]
      served_at?: string
      served_root?: string
      files_written?: {
        path: string
        sha256: string
      }[]
      files_removed?: string[]
      auto_open?: "at_create" | "after_first_write"
      warnings?: string[]
      files_error?: string
      files_error_kind?: "type_owned_path"
      provisioned?: {
        store: string
        project_id: string
        file_id?: string
        node_id?: string
      }
      liveSubscription?: string
      pinned?: boolean
      instructions?: string
      instructions_chars?: number
      instructions_clipped?: boolean
      instructions_unavailable?: string
      viewer_note?: string
      init_references?: {
        docs: {
          path: string
          text: string
          chars: number
          clipped?: boolean
        }[]
        unavailable?: {
          path: string
          why: string
        }[]
      }
      after_quickstart?: {
        design_system?: string
        saved_system?: string
        saved_system_dir?: string
        saved_pages_dir?: string
        not_listed?: boolean
      }
      design_systems?: {
        type?: string
        type_url?: string
        scope: string
        instances: {
          title: string
          url: string
          description?: string
          created_at?: string
          rel?: string
          audience?: string
          outsiders_may_have_written?: true
          default?: string
        }[]
        more?: boolean
        overflow?: boolean
        dropped?: number
        unavailable?: boolean
      }
      design_systems_note?: string
      design_system?: {
        url?: string
        default?: string
        title?: string
        store?: boolean
        docs?: {
          path: string
          text: string
          chars: number
          clipped?: boolean
        }[]
        token_files?: string[]
        unavailable?: string
      }
    } | {
      opened: true
      url: string
      artifact_id: string
      title?: string
      owned?: boolean
    } | {
      url: string
      path: string
      artifact_id?: string
      title?: string
      version?: string
      capabilities?: unknown
      stored?: {
        contract: string
        preferredContract?: string
        capabilities?: {}
        carried?: boolean
        read?: string
      }
      warnings?: string[]
      publishesRemaining?: number
      publishesResetAt?: number
      contract?: string
      updated?: boolean
      owned?: boolean
      icon?: string
      faviconSent?: true
      iconDropped?: true
      audience?: string
      folder_audience?: "others" | "unknown"
      seq?: number
      unchanged?: true
      merged_over?: {
        base: string
        live?: string
        changed?: Array<{
          path: string
          sha256: string | null
        }>
        omitted?: number
      }
      liveSubscription?: string
      verifyGuide?: string
      editsApplied?: number
      editsNotWritten?: "write_failed" | "not_writable" | "changed_during_publish" | "hard_linked"
      seededThread?: string
      files_written?: {
        path: string
        sha256: string
      }[]
      files_removed?: string[]
      pinned?: boolean
      type?: {
        url: string
        release: string
        latest?: string
        blocked?: {
          to?: string
          reason: string
          conflict_count?: number
          paths?: string[]
        }
      }
      own_files?: string[]
      type_files?: string[]
      served_at?: string
      served_root?: string
      new_files?: string[]
      unchanged_files?: string[]
    } | {
      artifacts: Array<{
        title: string
        url: string
        favicon?: string
        updatedAt?: string
        rel?: "mine" | "shared"
        external?: true
        role?: "editor" | "commenter" | "reader" | "viewer"
        outsidersMayHaveWritten?: true
        pinned?: boolean
      }>
      truncated?: boolean
      total?: number
      total_at_least?: true
      next_page_token?: string
      pins_enabled?: boolean
      scope?: "shared" | "all"
      external_listed?: true
    } | {
      read: {
        url: string
        bytes: number
        code: number
        codeText: string
        result: string
        durationMs: number
        title?: string
      }
      owned?: boolean
      artifactRead?: {
        slug: string
        ver?: string
        seeded?: false
      }
    } | {
      artifact_types: {
        title: string
        type_url: string
        description?: string
        tier?: string
        third_party?: boolean
      }[]
      query?: string
      more?: boolean
      dropped?: number
      unavailable?: boolean
      docs_unfillable?: boolean
    } | {
      artifact_type: {
        title: string
        type_url: string
        description?: string
        tier?: string
        third_party?: boolean
        release?: string
        files: string[]
        files_omitted?: number
        instructions_file: boolean
        instructions?: string
        instructions_chars?: number
        instructions_clipped?: boolean
        instructions_unavailable?: string
        viewer_note?: string
        capabilities: string[]
        creatable?: boolean
      }
      read_of_type_link?: true
      type_file?: {
        path: string
        content?: string
        chars?: number
        clipped?: boolean
        unread?: "withheld" | "not_listed" | "not_text" | "too_large" | "unavailable" | "result_full"
        why?: string
      }
      type_files_read?: Array<{
        path: string
        content?: string
        chars?: number
        clipped?: boolean
        unread?: "withheld" | "not_listed" | "not_text" | "too_large" | "unavailable" | "result_full"
        why?: string
      }>
    } | {
      type_instances: {
        type?: string
        type_url?: string
        scope: string
        instances: {
          title: string
          url: string
          description?: string
          created_at?: string
          rel?: string
          audience?: string
          outsiders_may_have_written?: true
          default?: string
        }[]
        more?: boolean
        overflow?: boolean
        dropped?: number
        unavailable?: boolean
      }
    } | {
      quickstart: {
        intent: string
        match?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        match_of?: number
        ask_first?: boolean
        types?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }[]
        types_more?: boolean
        dashboard_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        motion_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        whiteboard_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        types_unavailable?: boolean
        types_ruled?: boolean
        types_ambiguous?: boolean
        types_partial?: boolean
        types_note?: string
        types_hooked?: boolean
        docs_connector?: boolean
        design_systems?: {
          type?: string
          type_url?: string
          scope: string
          instances: {
            title: string
            url: string
            description?: string
            created_at?: string
            rel?: string
            audience?: string
            outsiders_may_have_written?: true
            default?: string
          }[]
          more?: boolean
          overflow?: boolean
          dropped?: number
          unavailable?: boolean
        }
        design_systems_note?: string
        design_systems_off?: boolean
        design_system?: {
          url?: string
          default?: string
          title?: string
          store?: boolean
          docs?: {
            path: string
            text: string
            chars: number
            clipped?: boolean
          }[]
          token_files?: string[]
          unavailable?: string
        }
        design_guidance?: boolean
        start_kit?: {
          type?: {
            dir: string
            files: {
              path: string
              bytes: number
            }[]
            skipped: {
              path: string
              reason: string
            }[]
          }
          system_url?: string
          system?: {
            dir: string
            files: {
              path: string
              bytes: number
            }[]
            skipped: {
              path: string
              reason: string
            }[]
          }
          skill_in_result: boolean
          capabilities_skill: boolean
          repl_tool?: boolean
        }
      }
    } | {
      threads_dropped?: boolean
      thread_filter?: string
      scoped_dispatch?: boolean
      foreign?: true
      cursor?: string
      outside_org?: boolean
      page_owns_threads?: boolean
      names?: {}
      threads: {
        id: string
        created_at?: string
        resolved: boolean
        resolved_degraded?: boolean
        resolved_by_claude?: boolean
        claude_activated: boolean
        activated_degraded?: boolean
        carried?: boolean
        anchor_path?: string
        span_quote?: string
        anchor_file?: string
        anchor_file_degraded?: boolean
        anchor_file_sha?: string
        anchor_moved_at?: string
        anchor_label?: string
        anchor_detail?: string
        anchor_snippet?: string
        anchor_region?: boolean
        region_inside?: string[]
        comments_degraded?: boolean
        comments: {
          id: string
          account: string
          role?: string
          text: string
          created_at?: string
          sent_to_claude?: boolean
          sent_to_claude_degraded?: boolean
          sent_by_viewer?: boolean
          posted_by_artifact?: boolean
          awaiting_reply?: boolean
          presence?: string
          access?: string
          outside?: true
        }[]
      }[]
    } | {
      replied: boolean
      thread_id: string
      comment_id?: string
      replayed?: boolean
      not_activated?: boolean
      summon_answered?: boolean
      summon_foreign?: boolean
      already_answered?: boolean
      page_owns_threads?: boolean
      standing_reply_id?: string
    } | {
      thread_resolved: boolean
      thread_id: string
      not_activated?: boolean
      not_authorized?: boolean
      summon_foreign?: boolean
      relayed_credential?: boolean
      page_owns_threads?: boolean
    } | {
      watch: {
        url: string
        watching: boolean
        outcome: string
        reason?: string
        durable_skip_reason?: string
        task_id?: string
        since?: number
        token_expires_at?: number
        auto_reply?: string
        can_edit?: boolean
        user_turn?: boolean
        named_by_user?: boolean
        replies_declined?: boolean
        rail?: string
        trigger_id?: string
        durable_since?: string
        status?: number
        detail?: string
        note?: string
        events?: string[]
      }
    } | {
      unwatch: {
        url: string
        was_watching: boolean
      }
    } | {
      resume_replies: {
        url: string
        resumed: boolean
        outcome: string
        reason?: string
        task_id?: string
        stop_kind?: string
        in_place?: boolean
        connecting?: boolean
      }
    } | {
      watches: Array<{
        url: string
        task_id: string
        since: number
        explicit: boolean
        connected: boolean
        connecting?: boolean
        token_expires_at: number
        armed_via?: string
        auto_reply?: string
        unread_plain_comments?: number
        summons_awaiting_reply?: number
        comments_uncounted?: boolean
        comments_partially_counted?: boolean
      } | {
        url: string
        rail: "durable_wake"
        trigger_id: string
        since: string
        events?: string[]
        restored?: boolean
      } | {
        url: string
        rail: "live_stopped"
        since?: number
        explicit?: boolean
        armed_via?: string
        auto_reply: string
        stop_kind: string
      }>
      filter_url?: string
      arms?: {
        url: string
        rail?: string
        state: string
        reconnect?: boolean
        failures?: number
        max_failures?: number
        next_in_s?: number
        last_failure?: string
        reason?: string
        detail?: string
        server_message?: string
        at?: number
      }[]
    } | {
      db_read: {
        op: string
        collection: string
        doc_id?: string
        found?: boolean
        as_level?: string
        as_level_confirmed?: boolean
        docs?: {
          id: string
          data: {}
          version?: number
          updatedAt?: string
        }[]
        next_cursor?: string
        me_id?: string
        ordered_by?: {
          field: string
          limit: number
        }
        foreign?: true
        outside_writer?: true
        saved?: {
          dir: string
          files: {
            id: string
            path: string
            bytes: number
            compact?: boolean
            version?: number
            updatedAt?: string
          }[]
          skipped: {
            id: string
            reason: string
          }[]
        }
      }
    } | {
      db_profiles: {
        ids: string[]
        profiles?: {}
        unavailable?: true
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      as_level?: string
      as_level_confirmed?: boolean
      db_write: {
        op: string
        collection: string
        doc_id: string
        field?: string
        replace_all?: true
        version?: number
        committed: boolean
        usage?: {
          documents: number
          max_documents: number
        }
        embedded?: {
          strings: number
          kb: number
        }
        warnings?: string[]
      } | {
        op: "batch"
        committed: boolean
        results: {
          op: string
          collection: string
          doc_id: string
          field?: string
          replace_all?: true
          version?: number
        }[]
        usage?: {
          documents: number
          max_documents: number
        }
        embedded?: {
          strings: number
          kb: number
        }
        warnings?: string[]
        fallback?: "sequential"
      }
    } | {
      room_send: {
        url: string
        topic: string
        delivered: boolean
        peers?: number
        reason?: string
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_upload: {
        id: string
        url: string
        size_bytes: number
        content_type: string
        sha256?: string
        file_name: string
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_uploads: {
        url: string
        results: Array<{
          file_path: string
          status: "uploaded"
          id: string
          url: string
          size_bytes: number
          content_type: string
          sha256?: string
          file_name: string
        } | {
          file_path: string
          status: "failed" | "not_attempted"
          reason: string
          message: string
          may_be_stored?: true
        }>
      }
    } | {
      asset_list: {
        url: string
        assets: {
          id: string
          url: string
          content_type: string
          size_bytes: number
          sha256?: string
          created_at: string
        }[]
        usage: {
          files: number
          bytes: number
          max_files: number
          max_bytes: number
        }
        next?: string
        cowritten?: true
        outside_writer?: true
      }
    } | {
      asset_read: {
        id: string
        path: string
        size_bytes: number
        content_type: string
        sha256: string
        cowritten?: true
        outside_writer?: true
        public_read?: true
        foreign?: true
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_delete: {
        id: string
        deleted: boolean
      }
    } | {
      asset_copy: {
        url: string
        from_url: string
        assets: {
          from_id: string
          id: string
          url: string
          size_bytes: number
          content_type: string
          sha256?: string
        }[]
      }
    } | {
      file_list: {
        url: string
        ver: string
        files: {
          path: string
          content_type: string
          size_bytes: number
          sha256: string
          live?: true
        }[]
        can_publish?: boolean
        owned?: boolean
        audience?: "owner" | "users" | "org" | "public" | "agent_scoped" | "unknown"
        cowritten?: true
        outside_writer?: true
        public_read?: true
        narrowed?: true
        single_page?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
        stored?: {
          contract: string
          capabilities?: {}
        }
      }
    } | {
      file_read: {
        url?: string
        title?: string
        path: string
        saved_to: string
        ver: string
        size_bytes: number
        content_type: string
        sha256: string
        content?: string
        content_scrubbed?: true
        as_served?: true
        source?: true
        live?: true
        live_verified?: true
        seq?: number
        cowritten?: true
        outside_writer?: true
        public_read?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
      }
    } | {
      files_read: {
        url: string
        title?: string
        ver: string
        saved_dir: string
        files: Array<{
          path: string
          saved_to: string
          size_bytes: number
          content_type: string
          sha256: string
          content?: string
          content_scrubbed?: true
          as_served?: true
          source?: true
          foreign?: true
        } | {
          path: string
          error: string
        }>
        cowritten?: true
        outside_writer?: true
        public_read?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
      }
    } | {
      artifact_delete: {
        url: string
        deleted: true
        already_gone?: boolean
      }
    } | {
      pin: {
        action: "pin" | "unpin"
        url: string
        pinned: boolean
        title?: string
      }
    } | {
      shared: {
        url: string
        mode: string
        access: string
        read_mode: string
        added: number
        editors?: number
        unchanged?: boolean
        org_name?: string
        title?: string
      }
    } | {
      page_versions: {
        url: string
        rows: {
          id: string
          createdAt?: string
          current?: true
        }[]
        degraded?: true
        cut?: true
      }
    } | {
      verify: {
        url: string
        ver: string
        state: string
        entries: unknown[]
        truncated?: boolean
        dropped?: number
        waited?: boolean
        foreign?: true
      }
    } | {
      preview: {
        file: string
        bytes: number
        widths: number[]
        themes: string[]
        shots: {
          width: number
          theme: string
          height?: number
          pageHeight?: number
          path?: string
          base64?: string
          error?: string
        }[]
        issues: {
          kind: string
          text: string
        }[]
        issuesDropped?: number
        renderError?: string
      }
    } | {
      emulatorPreview: {
        file: string
        outcome: string
        pictures: {
          path: string
          base64?: string
        }[]
        marks?: string[]
        errors?: string[]
        outline?: string
        stopped?: string
      }
    }
    ArtifactCheck: {
      created_from_type: true
      already_created?: true
      url: string
      version: string
      owned?: boolean
      path?: string
      title?: string
      type: {
        url: string
        release: string
      }
      own_files: string[]
      type_files: string[]
      served_at?: string
      served_root?: string
      files_written?: {
        path: string
        sha256: string
      }[]
      files_removed?: string[]
      auto_open?: "at_create" | "after_first_write"
      warnings?: string[]
      files_error?: string
      files_error_kind?: "type_owned_path"
      provisioned?: {
        store: string
        project_id: string
        file_id?: string
        node_id?: string
      }
      liveSubscription?: string
      pinned?: boolean
      instructions?: string
      instructions_chars?: number
      instructions_clipped?: boolean
      instructions_unavailable?: string
      viewer_note?: string
      init_references?: {
        docs: {
          path: string
          text: string
          chars: number
          clipped?: boolean
        }[]
        unavailable?: {
          path: string
          why: string
        }[]
      }
      after_quickstart?: {
        design_system?: string
        saved_system?: string
        saved_system_dir?: string
        saved_pages_dir?: string
        not_listed?: boolean
      }
      design_systems?: {
        type?: string
        type_url?: string
        scope: string
        instances: {
          title: string
          url: string
          description?: string
          created_at?: string
          rel?: string
          audience?: string
          outsiders_may_have_written?: true
          default?: string
        }[]
        more?: boolean
        overflow?: boolean
        dropped?: number
        unavailable?: boolean
      }
      design_systems_note?: string
      design_system?: {
        url?: string
        default?: string
        title?: string
        store?: boolean
        docs?: {
          path: string
          text: string
          chars: number
          clipped?: boolean
        }[]
        token_files?: string[]
        unavailable?: string
      }
    } | {
      opened: true
      url: string
      artifact_id: string
      title?: string
      owned?: boolean
    } | {
      url: string
      path: string
      artifact_id?: string
      title?: string
      version?: string
      capabilities?: unknown
      stored?: {
        contract: string
        preferredContract?: string
        capabilities?: {}
        carried?: boolean
        read?: string
      }
      warnings?: string[]
      publishesRemaining?: number
      publishesResetAt?: number
      contract?: string
      updated?: boolean
      owned?: boolean
      icon?: string
      faviconSent?: true
      iconDropped?: true
      audience?: string
      folder_audience?: "others" | "unknown"
      seq?: number
      unchanged?: true
      merged_over?: {
        base: string
        live?: string
        changed?: Array<{
          path: string
          sha256: string | null
        }>
        omitted?: number
      }
      liveSubscription?: string
      verifyGuide?: string
      editsApplied?: number
      editsNotWritten?: "write_failed" | "not_writable" | "changed_during_publish" | "hard_linked"
      seededThread?: string
      files_written?: {
        path: string
        sha256: string
      }[]
      files_removed?: string[]
      pinned?: boolean
      type?: {
        url: string
        release: string
        latest?: string
        blocked?: {
          to?: string
          reason: string
          conflict_count?: number
          paths?: string[]
        }
      }
      own_files?: string[]
      type_files?: string[]
      served_at?: string
      served_root?: string
      new_files?: string[]
      unchanged_files?: string[]
    } | {
      artifacts: Array<{
        title: string
        url: string
        favicon?: string
        updatedAt?: string
        rel?: "mine" | "shared"
        external?: true
        role?: "editor" | "commenter" | "reader" | "viewer"
        outsidersMayHaveWritten?: true
        pinned?: boolean
      }>
      truncated?: boolean
      total?: number
      total_at_least?: true
      next_page_token?: string
      pins_enabled?: boolean
      scope?: "shared" | "all"
      external_listed?: true
    } | {
      read: {
        url: string
        bytes: number
        code: number
        codeText: string
        result: string
        durationMs: number
        title?: string
      }
      owned?: boolean
      artifactRead?: {
        slug: string
        ver?: string
        seeded?: false
      }
    } | {
      artifact_types: {
        title: string
        type_url: string
        description?: string
        tier?: string
        third_party?: boolean
      }[]
      query?: string
      more?: boolean
      dropped?: number
      unavailable?: boolean
      docs_unfillable?: boolean
    } | {
      artifact_type: {
        title: string
        type_url: string
        description?: string
        tier?: string
        third_party?: boolean
        release?: string
        files: string[]
        files_omitted?: number
        instructions_file: boolean
        instructions?: string
        instructions_chars?: number
        instructions_clipped?: boolean
        instructions_unavailable?: string
        viewer_note?: string
        capabilities: string[]
        creatable?: boolean
      }
      read_of_type_link?: true
      type_file?: {
        path: string
        content?: string
        chars?: number
        clipped?: boolean
        unread?: "withheld" | "not_listed" | "not_text" | "too_large" | "unavailable" | "result_full"
        why?: string
      }
      type_files_read?: Array<{
        path: string
        content?: string
        chars?: number
        clipped?: boolean
        unread?: "withheld" | "not_listed" | "not_text" | "too_large" | "unavailable" | "result_full"
        why?: string
      }>
    } | {
      type_instances: {
        type?: string
        type_url?: string
        scope: string
        instances: {
          title: string
          url: string
          description?: string
          created_at?: string
          rel?: string
          audience?: string
          outsiders_may_have_written?: true
          default?: string
        }[]
        more?: boolean
        overflow?: boolean
        dropped?: number
        unavailable?: boolean
      }
    } | {
      quickstart: {
        intent: string
        match?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        match_of?: number
        ask_first?: boolean
        types?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }[]
        types_more?: boolean
        dashboard_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        motion_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        whiteboard_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        types_unavailable?: boolean
        types_ruled?: boolean
        types_ambiguous?: boolean
        types_partial?: boolean
        types_note?: string
        types_hooked?: boolean
        docs_connector?: boolean
        design_systems?: {
          type?: string
          type_url?: string
          scope: string
          instances: {
            title: string
            url: string
            description?: string
            created_at?: string
            rel?: string
            audience?: string
            outsiders_may_have_written?: true
            default?: string
          }[]
          more?: boolean
          overflow?: boolean
          dropped?: number
          unavailable?: boolean
        }
        design_systems_note?: string
        design_systems_off?: boolean
        design_system?: {
          url?: string
          default?: string
          title?: string
          store?: boolean
          docs?: {
            path: string
            text: string
            chars: number
            clipped?: boolean
          }[]
          token_files?: string[]
          unavailable?: string
        }
        design_guidance?: boolean
        start_kit?: {
          type?: {
            dir: string
            files: {
              path: string
              bytes: number
            }[]
            skipped: {
              path: string
              reason: string
            }[]
          }
          system_url?: string
          system?: {
            dir: string
            files: {
              path: string
              bytes: number
            }[]
            skipped: {
              path: string
              reason: string
            }[]
          }
          skill_in_result: boolean
          capabilities_skill: boolean
          repl_tool?: boolean
        }
      }
    } | {
      threads_dropped?: boolean
      thread_filter?: string
      scoped_dispatch?: boolean
      foreign?: true
      cursor?: string
      outside_org?: boolean
      page_owns_threads?: boolean
      names?: {}
      threads: {
        id: string
        created_at?: string
        resolved: boolean
        resolved_degraded?: boolean
        resolved_by_claude?: boolean
        claude_activated: boolean
        activated_degraded?: boolean
        carried?: boolean
        anchor_path?: string
        span_quote?: string
        anchor_file?: string
        anchor_file_degraded?: boolean
        anchor_file_sha?: string
        anchor_moved_at?: string
        anchor_label?: string
        anchor_detail?: string
        anchor_snippet?: string
        anchor_region?: boolean
        region_inside?: string[]
        comments_degraded?: boolean
        comments: {
          id: string
          account: string
          role?: string
          text: string
          created_at?: string
          sent_to_claude?: boolean
          sent_to_claude_degraded?: boolean
          sent_by_viewer?: boolean
          posted_by_artifact?: boolean
          awaiting_reply?: boolean
          presence?: string
          access?: string
          outside?: true
        }[]
      }[]
    } | {
      replied: boolean
      thread_id: string
      comment_id?: string
      replayed?: boolean
      not_activated?: boolean
      summon_answered?: boolean
      summon_foreign?: boolean
      already_answered?: boolean
      page_owns_threads?: boolean
      standing_reply_id?: string
    } | {
      thread_resolved: boolean
      thread_id: string
      not_activated?: boolean
      not_authorized?: boolean
      summon_foreign?: boolean
      relayed_credential?: boolean
      page_owns_threads?: boolean
    } | {
      watch: {
        url: string
        watching: boolean
        outcome: string
        reason?: string
        durable_skip_reason?: string
        task_id?: string
        since?: number
        token_expires_at?: number
        auto_reply?: string
        can_edit?: boolean
        user_turn?: boolean
        named_by_user?: boolean
        replies_declined?: boolean
        rail?: string
        trigger_id?: string
        durable_since?: string
        status?: number
        detail?: string
        note?: string
        events?: string[]
      }
    } | {
      unwatch: {
        url: string
        was_watching: boolean
      }
    } | {
      resume_replies: {
        url: string
        resumed: boolean
        outcome: string
        reason?: string
        task_id?: string
        stop_kind?: string
        in_place?: boolean
        connecting?: boolean
      }
    } | {
      watches: Array<{
        url: string
        task_id: string
        since: number
        explicit: boolean
        connected: boolean
        connecting?: boolean
        token_expires_at: number
        armed_via?: string
        auto_reply?: string
        unread_plain_comments?: number
        summons_awaiting_reply?: number
        comments_uncounted?: boolean
        comments_partially_counted?: boolean
      } | {
        url: string
        rail: "durable_wake"
        trigger_id: string
        since: string
        events?: string[]
        restored?: boolean
      } | {
        url: string
        rail: "live_stopped"
        since?: number
        explicit?: boolean
        armed_via?: string
        auto_reply: string
        stop_kind: string
      }>
      filter_url?: string
      arms?: {
        url: string
        rail?: string
        state: string
        reconnect?: boolean
        failures?: number
        max_failures?: number
        next_in_s?: number
        last_failure?: string
        reason?: string
        detail?: string
        server_message?: string
        at?: number
      }[]
    } | {
      db_read: {
        op: string
        collection: string
        doc_id?: string
        found?: boolean
        as_level?: string
        as_level_confirmed?: boolean
        docs?: {
          id: string
          data: {}
          version?: number
          updatedAt?: string
        }[]
        next_cursor?: string
        me_id?: string
        ordered_by?: {
          field: string
          limit: number
        }
        foreign?: true
        outside_writer?: true
        saved?: {
          dir: string
          files: {
            id: string
            path: string
            bytes: number
            compact?: boolean
            version?: number
            updatedAt?: string
          }[]
          skipped: {
            id: string
            reason: string
          }[]
        }
      }
    } | {
      db_profiles: {
        ids: string[]
        profiles?: {}
        unavailable?: true
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      as_level?: string
      as_level_confirmed?: boolean
      db_write: {
        op: string
        collection: string
        doc_id: string
        field?: string
        replace_all?: true
        version?: number
        committed: boolean
        usage?: {
          documents: number
          max_documents: number
        }
        embedded?: {
          strings: number
          kb: number
        }
        warnings?: string[]
      } | {
        op: "batch"
        committed: boolean
        results: {
          op: string
          collection: string
          doc_id: string
          field?: string
          replace_all?: true
          version?: number
        }[]
        usage?: {
          documents: number
          max_documents: number
        }
        embedded?: {
          strings: number
          kb: number
        }
        warnings?: string[]
        fallback?: "sequential"
      }
    } | {
      room_send: {
        url: string
        topic: string
        delivered: boolean
        peers?: number
        reason?: string
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_upload: {
        id: string
        url: string
        size_bytes: number
        content_type: string
        sha256?: string
        file_name: string
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_uploads: {
        url: string
        results: Array<{
          file_path: string
          status: "uploaded"
          id: string
          url: string
          size_bytes: number
          content_type: string
          sha256?: string
          file_name: string
        } | {
          file_path: string
          status: "failed" | "not_attempted"
          reason: string
          message: string
          may_be_stored?: true
        }>
      }
    } | {
      asset_list: {
        url: string
        assets: {
          id: string
          url: string
          content_type: string
          size_bytes: number
          sha256?: string
          created_at: string
        }[]
        usage: {
          files: number
          bytes: number
          max_files: number
          max_bytes: number
        }
        next?: string
        cowritten?: true
        outside_writer?: true
      }
    } | {
      asset_read: {
        id: string
        path: string
        size_bytes: number
        content_type: string
        sha256: string
        cowritten?: true
        outside_writer?: true
        public_read?: true
        foreign?: true
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_delete: {
        id: string
        deleted: boolean
      }
    } | {
      asset_copy: {
        url: string
        from_url: string
        assets: {
          from_id: string
          id: string
          url: string
          size_bytes: number
          content_type: string
          sha256?: string
        }[]
      }
    } | {
      file_list: {
        url: string
        ver: string
        files: {
          path: string
          content_type: string
          size_bytes: number
          sha256: string
          live?: true
        }[]
        can_publish?: boolean
        owned?: boolean
        audience?: "owner" | "users" | "org" | "public" | "agent_scoped" | "unknown"
        cowritten?: true
        outside_writer?: true
        public_read?: true
        narrowed?: true
        single_page?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
        stored?: {
          contract: string
          capabilities?: {}
        }
      }
    } | {
      file_read: {
        url?: string
        title?: string
        path: string
        saved_to: string
        ver: string
        size_bytes: number
        content_type: string
        sha256: string
        content?: string
        content_scrubbed?: true
        as_served?: true
        source?: true
        live?: true
        live_verified?: true
        seq?: number
        cowritten?: true
        outside_writer?: true
        public_read?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
      }
    } | {
      files_read: {
        url: string
        title?: string
        ver: string
        saved_dir: string
        files: Array<{
          path: string
          saved_to: string
          size_bytes: number
          content_type: string
          sha256: string
          content?: string
          content_scrubbed?: true
          as_served?: true
          source?: true
          foreign?: true
        } | {
          path: string
          error: string
        }>
        cowritten?: true
        outside_writer?: true
        public_read?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
      }
    } | {
      artifact_delete: {
        url: string
        deleted: true
        already_gone?: boolean
      }
    } | {
      pin: {
        action: "pin" | "unpin"
        url: string
        pinned: boolean
        title?: string
      }
    } | {
      shared: {
        url: string
        mode: string
        access: string
        read_mode: string
        added: number
        editors?: number
        unchanged?: boolean
        org_name?: string
        title?: string
      }
    } | {
      page_versions: {
        url: string
        rows: {
          id: string
          createdAt?: string
          current?: true
        }[]
        degraded?: true
        cut?: true
      }
    } | {
      verify: {
        url: string
        ver: string
        state: string
        entries: unknown[]
        truncated?: boolean
        dropped?: number
        waited?: boolean
        foreign?: true
      }
    } | {
      preview: {
        file: string
        bytes: number
        widths: number[]
        themes: string[]
        shots: {
          width: number
          theme: string
          height?: number
          pageHeight?: number
          path?: string
          base64?: string
          error?: string
        }[]
        issues: {
          kind: string
          text: string
        }[]
        issuesDropped?: number
        renderError?: string
      }
    } | {
      emulatorPreview: {
        file: string
        outcome: string
        pictures: {
          path: string
          base64?: string
        }[]
        marks?: string[]
        errors?: string[]
        outline?: string
        stopped?: string
      }
    }
    ArtifactComments: {
      created_from_type: true
      already_created?: true
      url: string
      version: string
      owned?: boolean
      path?: string
      title?: string
      type: {
        url: string
        release: string
      }
      own_files: string[]
      type_files: string[]
      served_at?: string
      served_root?: string
      files_written?: {
        path: string
        sha256: string
      }[]
      files_removed?: string[]
      auto_open?: "at_create" | "after_first_write"
      warnings?: string[]
      files_error?: string
      files_error_kind?: "type_owned_path"
      provisioned?: {
        store: string
        project_id: string
        file_id?: string
        node_id?: string
      }
      liveSubscription?: string
      pinned?: boolean
      instructions?: string
      instructions_chars?: number
      instructions_clipped?: boolean
      instructions_unavailable?: string
      viewer_note?: string
      init_references?: {
        docs: {
          path: string
          text: string
          chars: number
          clipped?: boolean
        }[]
        unavailable?: {
          path: string
          why: string
        }[]
      }
      after_quickstart?: {
        design_system?: string
        saved_system?: string
        saved_system_dir?: string
        saved_pages_dir?: string
        not_listed?: boolean
      }
      design_systems?: {
        type?: string
        type_url?: string
        scope: string
        instances: {
          title: string
          url: string
          description?: string
          created_at?: string
          rel?: string
          audience?: string
          outsiders_may_have_written?: true
          default?: string
        }[]
        more?: boolean
        overflow?: boolean
        dropped?: number
        unavailable?: boolean
      }
      design_systems_note?: string
      design_system?: {
        url?: string
        default?: string
        title?: string
        store?: boolean
        docs?: {
          path: string
          text: string
          chars: number
          clipped?: boolean
        }[]
        token_files?: string[]
        unavailable?: string
      }
    } | {
      opened: true
      url: string
      artifact_id: string
      title?: string
      owned?: boolean
    } | {
      url: string
      path: string
      artifact_id?: string
      title?: string
      version?: string
      capabilities?: unknown
      stored?: {
        contract: string
        preferredContract?: string
        capabilities?: {}
        carried?: boolean
        read?: string
      }
      warnings?: string[]
      publishesRemaining?: number
      publishesResetAt?: number
      contract?: string
      updated?: boolean
      owned?: boolean
      icon?: string
      faviconSent?: true
      iconDropped?: true
      audience?: string
      folder_audience?: "others" | "unknown"
      seq?: number
      unchanged?: true
      merged_over?: {
        base: string
        live?: string
        changed?: Array<{
          path: string
          sha256: string | null
        }>
        omitted?: number
      }
      liveSubscription?: string
      verifyGuide?: string
      editsApplied?: number
      editsNotWritten?: "write_failed" | "not_writable" | "changed_during_publish" | "hard_linked"
      seededThread?: string
      files_written?: {
        path: string
        sha256: string
      }[]
      files_removed?: string[]
      pinned?: boolean
      type?: {
        url: string
        release: string
        latest?: string
        blocked?: {
          to?: string
          reason: string
          conflict_count?: number
          paths?: string[]
        }
      }
      own_files?: string[]
      type_files?: string[]
      served_at?: string
      served_root?: string
      new_files?: string[]
      unchanged_files?: string[]
    } | {
      artifacts: Array<{
        title: string
        url: string
        favicon?: string
        updatedAt?: string
        rel?: "mine" | "shared"
        external?: true
        role?: "editor" | "commenter" | "reader" | "viewer"
        outsidersMayHaveWritten?: true
        pinned?: boolean
      }>
      truncated?: boolean
      total?: number
      total_at_least?: true
      next_page_token?: string
      pins_enabled?: boolean
      scope?: "shared" | "all"
      external_listed?: true
    } | {
      read: {
        url: string
        bytes: number
        code: number
        codeText: string
        result: string
        durationMs: number
        title?: string
      }
      owned?: boolean
      artifactRead?: {
        slug: string
        ver?: string
        seeded?: false
      }
    } | {
      artifact_types: {
        title: string
        type_url: string
        description?: string
        tier?: string
        third_party?: boolean
      }[]
      query?: string
      more?: boolean
      dropped?: number
      unavailable?: boolean
      docs_unfillable?: boolean
    } | {
      artifact_type: {
        title: string
        type_url: string
        description?: string
        tier?: string
        third_party?: boolean
        release?: string
        files: string[]
        files_omitted?: number
        instructions_file: boolean
        instructions?: string
        instructions_chars?: number
        instructions_clipped?: boolean
        instructions_unavailable?: string
        viewer_note?: string
        capabilities: string[]
        creatable?: boolean
      }
      read_of_type_link?: true
      type_file?: {
        path: string
        content?: string
        chars?: number
        clipped?: boolean
        unread?: "withheld" | "not_listed" | "not_text" | "too_large" | "unavailable" | "result_full"
        why?: string
      }
      type_files_read?: Array<{
        path: string
        content?: string
        chars?: number
        clipped?: boolean
        unread?: "withheld" | "not_listed" | "not_text" | "too_large" | "unavailable" | "result_full"
        why?: string
      }>
    } | {
      type_instances: {
        type?: string
        type_url?: string
        scope: string
        instances: {
          title: string
          url: string
          description?: string
          created_at?: string
          rel?: string
          audience?: string
          outsiders_may_have_written?: true
          default?: string
        }[]
        more?: boolean
        overflow?: boolean
        dropped?: number
        unavailable?: boolean
      }
    } | {
      quickstart: {
        intent: string
        match?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        match_of?: number
        ask_first?: boolean
        types?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }[]
        types_more?: boolean
        dashboard_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        motion_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        whiteboard_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        types_unavailable?: boolean
        types_ruled?: boolean
        types_ambiguous?: boolean
        types_partial?: boolean
        types_note?: string
        types_hooked?: boolean
        docs_connector?: boolean
        design_systems?: {
          type?: string
          type_url?: string
          scope: string
          instances: {
            title: string
            url: string
            description?: string
            created_at?: string
            rel?: string
            audience?: string
            outsiders_may_have_written?: true
            default?: string
          }[]
          more?: boolean
          overflow?: boolean
          dropped?: number
          unavailable?: boolean
        }
        design_systems_note?: string
        design_systems_off?: boolean
        design_system?: {
          url?: string
          default?: string
          title?: string
          store?: boolean
          docs?: {
            path: string
            text: string
            chars: number
            clipped?: boolean
          }[]
          token_files?: string[]
          unavailable?: string
        }
        design_guidance?: boolean
        start_kit?: {
          type?: {
            dir: string
            files: {
              path: string
              bytes: number
            }[]
            skipped: {
              path: string
              reason: string
            }[]
          }
          system_url?: string
          system?: {
            dir: string
            files: {
              path: string
              bytes: number
            }[]
            skipped: {
              path: string
              reason: string
            }[]
          }
          skill_in_result: boolean
          capabilities_skill: boolean
          repl_tool?: boolean
        }
      }
    } | {
      threads_dropped?: boolean
      thread_filter?: string
      scoped_dispatch?: boolean
      foreign?: true
      cursor?: string
      outside_org?: boolean
      page_owns_threads?: boolean
      names?: {}
      threads: {
        id: string
        created_at?: string
        resolved: boolean
        resolved_degraded?: boolean
        resolved_by_claude?: boolean
        claude_activated: boolean
        activated_degraded?: boolean
        carried?: boolean
        anchor_path?: string
        span_quote?: string
        anchor_file?: string
        anchor_file_degraded?: boolean
        anchor_file_sha?: string
        anchor_moved_at?: string
        anchor_label?: string
        anchor_detail?: string
        anchor_snippet?: string
        anchor_region?: boolean
        region_inside?: string[]
        comments_degraded?: boolean
        comments: {
          id: string
          account: string
          role?: string
          text: string
          created_at?: string
          sent_to_claude?: boolean
          sent_to_claude_degraded?: boolean
          sent_by_viewer?: boolean
          posted_by_artifact?: boolean
          awaiting_reply?: boolean
          presence?: string
          access?: string
          outside?: true
        }[]
      }[]
    } | {
      replied: boolean
      thread_id: string
      comment_id?: string
      replayed?: boolean
      not_activated?: boolean
      summon_answered?: boolean
      summon_foreign?: boolean
      already_answered?: boolean
      page_owns_threads?: boolean
      standing_reply_id?: string
    } | {
      thread_resolved: boolean
      thread_id: string
      not_activated?: boolean
      not_authorized?: boolean
      summon_foreign?: boolean
      relayed_credential?: boolean
      page_owns_threads?: boolean
    } | {
      watch: {
        url: string
        watching: boolean
        outcome: string
        reason?: string
        durable_skip_reason?: string
        task_id?: string
        since?: number
        token_expires_at?: number
        auto_reply?: string
        can_edit?: boolean
        user_turn?: boolean
        named_by_user?: boolean
        replies_declined?: boolean
        rail?: string
        trigger_id?: string
        durable_since?: string
        status?: number
        detail?: string
        note?: string
        events?: string[]
      }
    } | {
      unwatch: {
        url: string
        was_watching: boolean
      }
    } | {
      resume_replies: {
        url: string
        resumed: boolean
        outcome: string
        reason?: string
        task_id?: string
        stop_kind?: string
        in_place?: boolean
        connecting?: boolean
      }
    } | {
      watches: Array<{
        url: string
        task_id: string
        since: number
        explicit: boolean
        connected: boolean
        connecting?: boolean
        token_expires_at: number
        armed_via?: string
        auto_reply?: string
        unread_plain_comments?: number
        summons_awaiting_reply?: number
        comments_uncounted?: boolean
        comments_partially_counted?: boolean
      } | {
        url: string
        rail: "durable_wake"
        trigger_id: string
        since: string
        events?: string[]
        restored?: boolean
      } | {
        url: string
        rail: "live_stopped"
        since?: number
        explicit?: boolean
        armed_via?: string
        auto_reply: string
        stop_kind: string
      }>
      filter_url?: string
      arms?: {
        url: string
        rail?: string
        state: string
        reconnect?: boolean
        failures?: number
        max_failures?: number
        next_in_s?: number
        last_failure?: string
        reason?: string
        detail?: string
        server_message?: string
        at?: number
      }[]
    } | {
      db_read: {
        op: string
        collection: string
        doc_id?: string
        found?: boolean
        as_level?: string
        as_level_confirmed?: boolean
        docs?: {
          id: string
          data: {}
          version?: number
          updatedAt?: string
        }[]
        next_cursor?: string
        me_id?: string
        ordered_by?: {
          field: string
          limit: number
        }
        foreign?: true
        outside_writer?: true
        saved?: {
          dir: string
          files: {
            id: string
            path: string
            bytes: number
            compact?: boolean
            version?: number
            updatedAt?: string
          }[]
          skipped: {
            id: string
            reason: string
          }[]
        }
      }
    } | {
      db_profiles: {
        ids: string[]
        profiles?: {}
        unavailable?: true
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      as_level?: string
      as_level_confirmed?: boolean
      db_write: {
        op: string
        collection: string
        doc_id: string
        field?: string
        replace_all?: true
        version?: number
        committed: boolean
        usage?: {
          documents: number
          max_documents: number
        }
        embedded?: {
          strings: number
          kb: number
        }
        warnings?: string[]
      } | {
        op: "batch"
        committed: boolean
        results: {
          op: string
          collection: string
          doc_id: string
          field?: string
          replace_all?: true
          version?: number
        }[]
        usage?: {
          documents: number
          max_documents: number
        }
        embedded?: {
          strings: number
          kb: number
        }
        warnings?: string[]
        fallback?: "sequential"
      }
    } | {
      room_send: {
        url: string
        topic: string
        delivered: boolean
        peers?: number
        reason?: string
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_upload: {
        id: string
        url: string
        size_bytes: number
        content_type: string
        sha256?: string
        file_name: string
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_uploads: {
        url: string
        results: Array<{
          file_path: string
          status: "uploaded"
          id: string
          url: string
          size_bytes: number
          content_type: string
          sha256?: string
          file_name: string
        } | {
          file_path: string
          status: "failed" | "not_attempted"
          reason: string
          message: string
          may_be_stored?: true
        }>
      }
    } | {
      asset_list: {
        url: string
        assets: {
          id: string
          url: string
          content_type: string
          size_bytes: number
          sha256?: string
          created_at: string
        }[]
        usage: {
          files: number
          bytes: number
          max_files: number
          max_bytes: number
        }
        next?: string
        cowritten?: true
        outside_writer?: true
      }
    } | {
      asset_read: {
        id: string
        path: string
        size_bytes: number
        content_type: string
        sha256: string
        cowritten?: true
        outside_writer?: true
        public_read?: true
        foreign?: true
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_delete: {
        id: string
        deleted: boolean
      }
    } | {
      asset_copy: {
        url: string
        from_url: string
        assets: {
          from_id: string
          id: string
          url: string
          size_bytes: number
          content_type: string
          sha256?: string
        }[]
      }
    } | {
      file_list: {
        url: string
        ver: string
        files: {
          path: string
          content_type: string
          size_bytes: number
          sha256: string
          live?: true
        }[]
        can_publish?: boolean
        owned?: boolean
        audience?: "owner" | "users" | "org" | "public" | "agent_scoped" | "unknown"
        cowritten?: true
        outside_writer?: true
        public_read?: true
        narrowed?: true
        single_page?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
        stored?: {
          contract: string
          capabilities?: {}
        }
      }
    } | {
      file_read: {
        url?: string
        title?: string
        path: string
        saved_to: string
        ver: string
        size_bytes: number
        content_type: string
        sha256: string
        content?: string
        content_scrubbed?: true
        as_served?: true
        source?: true
        live?: true
        live_verified?: true
        seq?: number
        cowritten?: true
        outside_writer?: true
        public_read?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
      }
    } | {
      files_read: {
        url: string
        title?: string
        ver: string
        saved_dir: string
        files: Array<{
          path: string
          saved_to: string
          size_bytes: number
          content_type: string
          sha256: string
          content?: string
          content_scrubbed?: true
          as_served?: true
          source?: true
          foreign?: true
        } | {
          path: string
          error: string
        }>
        cowritten?: true
        outside_writer?: true
        public_read?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
      }
    } | {
      artifact_delete: {
        url: string
        deleted: true
        already_gone?: boolean
      }
    } | {
      pin: {
        action: "pin" | "unpin"
        url: string
        pinned: boolean
        title?: string
      }
    } | {
      shared: {
        url: string
        mode: string
        access: string
        read_mode: string
        added: number
        editors?: number
        unchanged?: boolean
        org_name?: string
        title?: string
      }
    } | {
      page_versions: {
        url: string
        rows: {
          id: string
          createdAt?: string
          current?: true
        }[]
        degraded?: true
        cut?: true
      }
    } | {
      verify: {
        url: string
        ver: string
        state: string
        entries: unknown[]
        truncated?: boolean
        dropped?: number
        waited?: boolean
        foreign?: true
      }
    } | {
      preview: {
        file: string
        bytes: number
        widths: number[]
        themes: string[]
        shots: {
          width: number
          theme: string
          height?: number
          pageHeight?: number
          path?: string
          base64?: string
          error?: string
        }[]
        issues: {
          kind: string
          text: string
        }[]
        issuesDropped?: number
        renderError?: string
      }
    } | {
      emulatorPreview: {
        file: string
        outcome: string
        pictures: {
          path: string
          base64?: string
        }[]
        marks?: string[]
        errors?: string[]
        outline?: string
        stopped?: string
      }
    }
    ArtifactData: {
      created_from_type: true
      already_created?: true
      url: string
      version: string
      owned?: boolean
      path?: string
      title?: string
      type: {
        url: string
        release: string
      }
      own_files: string[]
      type_files: string[]
      served_at?: string
      served_root?: string
      files_written?: {
        path: string
        sha256: string
      }[]
      files_removed?: string[]
      auto_open?: "at_create" | "after_first_write"
      warnings?: string[]
      files_error?: string
      files_error_kind?: "type_owned_path"
      provisioned?: {
        store: string
        project_id: string
        file_id?: string
        node_id?: string
      }
      liveSubscription?: string
      pinned?: boolean
      instructions?: string
      instructions_chars?: number
      instructions_clipped?: boolean
      instructions_unavailable?: string
      viewer_note?: string
      init_references?: {
        docs: {
          path: string
          text: string
          chars: number
          clipped?: boolean
        }[]
        unavailable?: {
          path: string
          why: string
        }[]
      }
      after_quickstart?: {
        design_system?: string
        saved_system?: string
        saved_system_dir?: string
        saved_pages_dir?: string
        not_listed?: boolean
      }
      design_systems?: {
        type?: string
        type_url?: string
        scope: string
        instances: {
          title: string
          url: string
          description?: string
          created_at?: string
          rel?: string
          audience?: string
          outsiders_may_have_written?: true
          default?: string
        }[]
        more?: boolean
        overflow?: boolean
        dropped?: number
        unavailable?: boolean
      }
      design_systems_note?: string
      design_system?: {
        url?: string
        default?: string
        title?: string
        store?: boolean
        docs?: {
          path: string
          text: string
          chars: number
          clipped?: boolean
        }[]
        token_files?: string[]
        unavailable?: string
      }
    } | {
      opened: true
      url: string
      artifact_id: string
      title?: string
      owned?: boolean
    } | {
      url: string
      path: string
      artifact_id?: string
      title?: string
      version?: string
      capabilities?: unknown
      stored?: {
        contract: string
        preferredContract?: string
        capabilities?: {}
        carried?: boolean
        read?: string
      }
      warnings?: string[]
      publishesRemaining?: number
      publishesResetAt?: number
      contract?: string
      updated?: boolean
      owned?: boolean
      icon?: string
      faviconSent?: true
      iconDropped?: true
      audience?: string
      folder_audience?: "others" | "unknown"
      seq?: number
      unchanged?: true
      merged_over?: {
        base: string
        live?: string
        changed?: Array<{
          path: string
          sha256: string | null
        }>
        omitted?: number
      }
      liveSubscription?: string
      verifyGuide?: string
      editsApplied?: number
      editsNotWritten?: "write_failed" | "not_writable" | "changed_during_publish" | "hard_linked"
      seededThread?: string
      files_written?: {
        path: string
        sha256: string
      }[]
      files_removed?: string[]
      pinned?: boolean
      type?: {
        url: string
        release: string
        latest?: string
        blocked?: {
          to?: string
          reason: string
          conflict_count?: number
          paths?: string[]
        }
      }
      own_files?: string[]
      type_files?: string[]
      served_at?: string
      served_root?: string
      new_files?: string[]
      unchanged_files?: string[]
    } | {
      artifacts: Array<{
        title: string
        url: string
        favicon?: string
        updatedAt?: string
        rel?: "mine" | "shared"
        external?: true
        role?: "editor" | "commenter" | "reader" | "viewer"
        outsidersMayHaveWritten?: true
        pinned?: boolean
      }>
      truncated?: boolean
      total?: number
      total_at_least?: true
      next_page_token?: string
      pins_enabled?: boolean
      scope?: "shared" | "all"
      external_listed?: true
    } | {
      read: {
        url: string
        bytes: number
        code: number
        codeText: string
        result: string
        durationMs: number
        title?: string
      }
      owned?: boolean
      artifactRead?: {
        slug: string
        ver?: string
        seeded?: false
      }
    } | {
      artifact_types: {
        title: string
        type_url: string
        description?: string
        tier?: string
        third_party?: boolean
      }[]
      query?: string
      more?: boolean
      dropped?: number
      unavailable?: boolean
      docs_unfillable?: boolean
    } | {
      artifact_type: {
        title: string
        type_url: string
        description?: string
        tier?: string
        third_party?: boolean
        release?: string
        files: string[]
        files_omitted?: number
        instructions_file: boolean
        instructions?: string
        instructions_chars?: number
        instructions_clipped?: boolean
        instructions_unavailable?: string
        viewer_note?: string
        capabilities: string[]
        creatable?: boolean
      }
      read_of_type_link?: true
      type_file?: {
        path: string
        content?: string
        chars?: number
        clipped?: boolean
        unread?: "withheld" | "not_listed" | "not_text" | "too_large" | "unavailable" | "result_full"
        why?: string
      }
      type_files_read?: Array<{
        path: string
        content?: string
        chars?: number
        clipped?: boolean
        unread?: "withheld" | "not_listed" | "not_text" | "too_large" | "unavailable" | "result_full"
        why?: string
      }>
    } | {
      type_instances: {
        type?: string
        type_url?: string
        scope: string
        instances: {
          title: string
          url: string
          description?: string
          created_at?: string
          rel?: string
          audience?: string
          outsiders_may_have_written?: true
          default?: string
        }[]
        more?: boolean
        overflow?: boolean
        dropped?: number
        unavailable?: boolean
      }
    } | {
      quickstart: {
        intent: string
        match?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        match_of?: number
        ask_first?: boolean
        types?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }[]
        types_more?: boolean
        dashboard_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        motion_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        whiteboard_type?: {
          title: string
          type_url: string
          description?: string
          tier?: string
          third_party?: boolean
        }
        types_unavailable?: boolean
        types_ruled?: boolean
        types_ambiguous?: boolean
        types_partial?: boolean
        types_note?: string
        types_hooked?: boolean
        docs_connector?: boolean
        design_systems?: {
          type?: string
          type_url?: string
          scope: string
          instances: {
            title: string
            url: string
            description?: string
            created_at?: string
            rel?: string
            audience?: string
            outsiders_may_have_written?: true
            default?: string
          }[]
          more?: boolean
          overflow?: boolean
          dropped?: number
          unavailable?: boolean
        }
        design_systems_note?: string
        design_systems_off?: boolean
        design_system?: {
          url?: string
          default?: string
          title?: string
          store?: boolean
          docs?: {
            path: string
            text: string
            chars: number
            clipped?: boolean
          }[]
          token_files?: string[]
          unavailable?: string
        }
        design_guidance?: boolean
        start_kit?: {
          type?: {
            dir: string
            files: {
              path: string
              bytes: number
            }[]
            skipped: {
              path: string
              reason: string
            }[]
          }
          system_url?: string
          system?: {
            dir: string
            files: {
              path: string
              bytes: number
            }[]
            skipped: {
              path: string
              reason: string
            }[]
          }
          skill_in_result: boolean
          capabilities_skill: boolean
          repl_tool?: boolean
        }
      }
    } | {
      threads_dropped?: boolean
      thread_filter?: string
      scoped_dispatch?: boolean
      foreign?: true
      cursor?: string
      outside_org?: boolean
      page_owns_threads?: boolean
      names?: {}
      threads: {
        id: string
        created_at?: string
        resolved: boolean
        resolved_degraded?: boolean
        resolved_by_claude?: boolean
        claude_activated: boolean
        activated_degraded?: boolean
        carried?: boolean
        anchor_path?: string
        span_quote?: string
        anchor_file?: string
        anchor_file_degraded?: boolean
        anchor_file_sha?: string
        anchor_moved_at?: string
        anchor_label?: string
        anchor_detail?: string
        anchor_snippet?: string
        anchor_region?: boolean
        region_inside?: string[]
        comments_degraded?: boolean
        comments: {
          id: string
          account: string
          role?: string
          text: string
          created_at?: string
          sent_to_claude?: boolean
          sent_to_claude_degraded?: boolean
          sent_by_viewer?: boolean
          posted_by_artifact?: boolean
          awaiting_reply?: boolean
          presence?: string
          access?: string
          outside?: true
        }[]
      }[]
    } | {
      replied: boolean
      thread_id: string
      comment_id?: string
      replayed?: boolean
      not_activated?: boolean
      summon_answered?: boolean
      summon_foreign?: boolean
      already_answered?: boolean
      page_owns_threads?: boolean
      standing_reply_id?: string
    } | {
      thread_resolved: boolean
      thread_id: string
      not_activated?: boolean
      not_authorized?: boolean
      summon_foreign?: boolean
      relayed_credential?: boolean
      page_owns_threads?: boolean
    } | {
      watch: {
        url: string
        watching: boolean
        outcome: string
        reason?: string
        durable_skip_reason?: string
        task_id?: string
        since?: number
        token_expires_at?: number
        auto_reply?: string
        can_edit?: boolean
        user_turn?: boolean
        named_by_user?: boolean
        replies_declined?: boolean
        rail?: string
        trigger_id?: string
        durable_since?: string
        status?: number
        detail?: string
        note?: string
        events?: string[]
      }
    } | {
      unwatch: {
        url: string
        was_watching: boolean
      }
    } | {
      resume_replies: {
        url: string
        resumed: boolean
        outcome: string
        reason?: string
        task_id?: string
        stop_kind?: string
        in_place?: boolean
        connecting?: boolean
      }
    } | {
      watches: Array<{
        url: string
        task_id: string
        since: number
        explicit: boolean
        connected: boolean
        connecting?: boolean
        token_expires_at: number
        armed_via?: string
        auto_reply?: string
        unread_plain_comments?: number
        summons_awaiting_reply?: number
        comments_uncounted?: boolean
        comments_partially_counted?: boolean
      } | {
        url: string
        rail: "durable_wake"
        trigger_id: string
        since: string
        events?: string[]
        restored?: boolean
      } | {
        url: string
        rail: "live_stopped"
        since?: number
        explicit?: boolean
        armed_via?: string
        auto_reply: string
        stop_kind: string
      }>
      filter_url?: string
      arms?: {
        url: string
        rail?: string
        state: string
        reconnect?: boolean
        failures?: number
        max_failures?: number
        next_in_s?: number
        last_failure?: string
        reason?: string
        detail?: string
        server_message?: string
        at?: number
      }[]
    } | {
      db_read: {
        op: string
        collection: string
        doc_id?: string
        found?: boolean
        as_level?: string
        as_level_confirmed?: boolean
        docs?: {
          id: string
          data: {}
          version?: number
          updatedAt?: string
        }[]
        next_cursor?: string
        me_id?: string
        ordered_by?: {
          field: string
          limit: number
        }
        foreign?: true
        outside_writer?: true
        saved?: {
          dir: string
          files: {
            id: string
            path: string
            bytes: number
            compact?: boolean
            version?: number
            updatedAt?: string
          }[]
          skipped: {
            id: string
            reason: string
          }[]
        }
      }
    } | {
      db_profiles: {
        ids: string[]
        profiles?: {}
        unavailable?: true
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      as_level?: string
      as_level_confirmed?: boolean
      db_write: {
        op: string
        collection: string
        doc_id: string
        field?: string
        replace_all?: true
        version?: number
        committed: boolean
        usage?: {
          documents: number
          max_documents: number
        }
        embedded?: {
          strings: number
          kb: number
        }
        warnings?: string[]
      } | {
        op: "batch"
        committed: boolean
        results: {
          op: string
          collection: string
          doc_id: string
          field?: string
          replace_all?: true
          version?: number
        }[]
        usage?: {
          documents: number
          max_documents: number
        }
        embedded?: {
          strings: number
          kb: number
        }
        warnings?: string[]
        fallback?: "sequential"
      }
    } | {
      room_send: {
        url: string
        topic: string
        delivered: boolean
        peers?: number
        reason?: string
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_upload: {
        id: string
        url: string
        size_bytes: number
        content_type: string
        sha256?: string
        file_name: string
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_uploads: {
        url: string
        results: Array<{
          file_path: string
          status: "uploaded"
          id: string
          url: string
          size_bytes: number
          content_type: string
          sha256?: string
          file_name: string
        } | {
          file_path: string
          status: "failed" | "not_attempted"
          reason: string
          message: string
          may_be_stored?: true
        }>
      }
    } | {
      asset_list: {
        url: string
        assets: {
          id: string
          url: string
          content_type: string
          size_bytes: number
          sha256?: string
          created_at: string
        }[]
        usage: {
          files: number
          bytes: number
          max_files: number
          max_bytes: number
        }
        next?: string
        cowritten?: true
        outside_writer?: true
      }
    } | {
      asset_read: {
        id: string
        path: string
        size_bytes: number
        content_type: string
        sha256: string
        cowritten?: true
        outside_writer?: true
        public_read?: true
        foreign?: true
      }
    } | {
      written?: {
        url: string
      }
      owned?: boolean
      asset_delete: {
        id: string
        deleted: boolean
      }
    } | {
      asset_copy: {
        url: string
        from_url: string
        assets: {
          from_id: string
          id: string
          url: string
          size_bytes: number
          content_type: string
          sha256?: string
        }[]
      }
    } | {
      file_list: {
        url: string
        ver: string
        files: {
          path: string
          content_type: string
          size_bytes: number
          sha256: string
          live?: true
        }[]
        can_publish?: boolean
        owned?: boolean
        audience?: "owner" | "users" | "org" | "public" | "agent_scoped" | "unknown"
        cowritten?: true
        outside_writer?: true
        public_read?: true
        narrowed?: true
        single_page?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
        stored?: {
          contract: string
          capabilities?: {}
        }
      }
    } | {
      file_read: {
        url?: string
        title?: string
        path: string
        saved_to: string
        ver: string
        size_bytes: number
        content_type: string
        sha256: string
        content?: string
        content_scrubbed?: true
        as_served?: true
        source?: true
        live?: true
        live_verified?: true
        seq?: number
        cowritten?: true
        outside_writer?: true
        public_read?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
      }
    } | {
      files_read: {
        url: string
        title?: string
        ver: string
        saved_dir: string
        files: Array<{
          path: string
          saved_to: string
          size_bytes: number
          content_type: string
          sha256: string
          content?: string
          content_scrubbed?: true
          as_served?: true
          source?: true
          foreign?: true
        } | {
          path: string
          error: string
        }>
        cowritten?: true
        outside_writer?: true
        public_read?: true
        from_type?: true
        type?: {
          url: string
          title?: string
        }
        foreign?: true
      }
    } | {
      artifact_delete: {
        url: string
        deleted: true
        already_gone?: boolean
      }
    } | {
      pin: {
        action: "pin" | "unpin"
        url: string
        pinned: boolean
        title?: string
      }
    } | {
      shared: {
        url: string
        mode: string
        access: string
        read_mode: string
        added: number
        editors?: number
        unchanged?: boolean
        org_name?: string
        title?: string
      }
    } | {
      page_versions: {
        url: string
        rows: {
          id: string
          createdAt?: string
          current?: true
        }[]
        degraded?: true
        cut?: true
      }
    } | {
      verify: {
        url: string
        ver: string
        state: string
        entries: unknown[]
        truncated?: boolean
        dropped?: number
        waited?: boolean
        foreign?: true
      }
    } | {
      preview: {
        file: string
        bytes: number
        widths: number[]
        themes: string[]
        shots: {
          width: number
          theme: string
          height?: number
          pageHeight?: number
          path?: string
          base64?: string
          error?: string
        }[]
        issues: {
          kind: string
          text: string
        }[]
        issuesDropped?: number
        renderError?: string
      }
    } | {
      emulatorPreview: {
        file: string
        outcome: string
        pictures: {
          path: string
          base64?: string
        }[]
        marks?: string[]
        errors?: string[]
        outline?: string
        stopped?: string
      }
    }
    AskUserQuestion: {
      questions: Array<{
        question: string
        header: string
        kind?: "choice" | "text" | "number"
        description?: string
        options: Array<{
          label: string
          description?: string
          preview?: string
        }>
        multiSelect: boolean
        placeholder?: string
        min?: number
        max?: number
        step?: number
        defaultValue?: number
        unit?: string
      }>
      answers: {}
      response?: string
      annotations?: {}
      afkTimeoutMs?: number
      followUp?: boolean
    }
    Bash: {
      stdout: string
      stderr: string
      rawOutputPath?: string
      interrupted: boolean
      isImage?: boolean
      backgroundTaskId?: string
      backgroundOutputPath?: string
      backgroundedByUser?: boolean
      backgroundedByTurnAbort?: boolean
      backgroundedToDeliverMessage?: boolean
      backgroundedForAgentReport?: true
      timedOutAfterMs?: number
      subagentCapApplied?: true
      backgroundCwdHint?: string
      backgroundEndsWithFinalResponse?: true
      backgroundWakesOwner?: true
      dangerouslyDisableSandbox?: boolean
      returnCodeInterpretation?: string
      noOutputExpected?: boolean
      structuredContent?: unknown[]
      persistedOutputPath?: string
      persistedOutputSize?: number
      stdoutHoldsOutputEnd?: boolean
      memoryLimitNote?: string
      triggeredNote?: string
      staleReadFileStateHint?: string
      ghRateLimitHint?: string
      gitOperation?: {
        commit?: {
          sha: string
          kind: "committed" | "amended" | "cherry-picked"
          branch?: string
        }
        push?: {
          branch: string
        }
        branch?: {
          ref: string
          action: "merged" | "rebased"
        }
        pr?: {
          number: number
          url?: string
          action: "created" | "edited" | "merged" | "commented" | "closed" | "reopened" | "ready" | "draft" | "auto-merge-enabled" | "auto-merge-disabled"
        }
      }
      bashEditDiff?: {
        files: {
          filePath: string
          hunks: {
            oldStart: number
            oldLines: number
            newStart: number
            newLines: number
            lines: string[]
          }[]
          created?: true
          deleted?: true
        }[]
        moreFiles: number
        changedFiles?: string[]
        unavailable?: true
        skipped?: true
        shared?: true
      }
      viewedImagePaths?: string[]
    }
    ClaudeDesign: {
      operation: string
      content: {}[]
      isError?: boolean
    }
    CronCreate: {
      id: string
      humanSchedule: string
      recurring: boolean
      durable?: boolean
      nextFireAt?: number
      maxAgeMs?: number
      otherOneShots?: {
        id: string
        humanSchedule: string
        prompt: string
      }[]
    }
    CronDelete: {
      id: string
      endedLoopWakeup?: true
    }
    CronList: {
      jobs: Array<{
        id: string
        cron: string
        humanSchedule: string
        prompt: string
        recurring?: boolean
        durable?: boolean
        nextFireAt?: number
      }>
    }
    DesignSync: {
      method: "list_projects"
      notice?: string
      projects: {
        projectId: string
        name: string
        ownerDisplayName?: string
        isOwned?: boolean
        updatedAt?: string
      }[]
    } | {
      method: "get_project"
      notice?: string
      projectId: string
      name: string
      type?: string
      ownerDisplayName?: string
      isOwned?: boolean
      canEdit?: boolean
      moveState?: "moving" | "moved"
      movedTo?: string
      movedToHeldBy?: "you" | "owner" | "someone_else"
    } | {
      method: "list_files"
      notice?: string
      paths: string[]
    } | {
      method: "get_file"
      notice?: string
      path: string
      content: string
      contentType: string
      isBase64: boolean
      truncated: boolean
    } | {
      method: "finalize_plan"
      notice?: string
      planId: string
      writes: string[]
      deletes: string[]
    } | {
      method: "write_files"
      notice?: string
      written: number
    } | {
      method: "delete_files"
      notice?: string
      deleted: number
    } | {
      method: "register_assets"
      notice?: string
      registered: number
    } | {
      method: "unregister_assets"
      notice?: string
      unregistered: number
    } | {
      method: "create_project"
      notice?: string
      projectId: string
      name: string
    } | {
      method: "report_validate"
      notice?: string
    }
    Edit: {
      filePath: string
      oldString: string
      newString: string
      originalFile: string | null
      structuredPatch: {
        oldStart: number
        oldLines: number
        newStart: number
        newLines: number
        lines: string[]
      }[]
      userModified: boolean
      replaceAll: boolean
      gitDiff?: {
        filename: string
        status: "modified" | "added"
        additions: number
        deletions: number
        changes: number
        patch: string
        repository?: string | null
      }
      staged?: boolean
      stagedWording?: "review" | "card" | "cloud" | "linked" | "policy"
    }
    "enable__mcp__claude-in-chrome": {
      message: string
    }
    "enable__mcp__remote-devices__Claude_Browser": {
      message: string
    }
    "enable__mcp__remote-devices__computer": {
      message: string
    }
    EndConversation: {
      ended: boolean
      message: string
    }
    EnterPlanMode: {
      message: string
    }
    EnterWorktree: {
      worktreePath: string
      worktreeBranch?: string
      message: string
      sandboxNote?: string
    }
    ExitPlanMode: {
      plan: string | null
      isAgent: boolean
      filePath?: string
      hasTaskTool?: boolean
      planWasEdited?: boolean
      awaitingLeaderApproval?: boolean
      requestId?: string
    }
    ExitWorktree: {
      action: "keep" | "remove"
      originalCwd: string
      worktreePath: string
      worktreeBranch?: string
      tmuxSessionName?: string
      discardedFiles?: number
      discardedCommits?: number
      restoredCwd?: string
      originalCwdMissing?: boolean
      message: string
      releaseNote?: string
      sandboxNote?: string
    }
    FetchInboxMessage: {
      ok: boolean
      file_id?: string
      message_id?: string
      enveloped_text?: string
      body?: string
      sender_display?: string
      sender_kind?: string
      source?: string
      slack_permalink?: string
      received_at?: string
      attachments_prefix?: string
      reason?: string
    }
    GetGoal: {
      condition: string | null
      lastReason?: string
      paused?: boolean
    }
    GetTask: {
      taskId: string
      statusMessage: string
      createdAt: string
      lastUpdatedAt: string
      status: "working"
    } | {
      taskId: string
      statusMessage: string
      createdAt: string
      lastUpdatedAt: string
      status: "completed"
      result: {
        content: Array<{
          type: "text"
          text: string
        } | {
          type: "image"
          source: {
            type: "base64"
            media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"
            data: string
          }
        }>
        isError: boolean
      }
    } | {
      taskId: string
      statusMessage: string
      createdAt: string
      lastUpdatedAt: string
      status: "failed"
      error: {
        code: number
        message: string
      }
    } | {
      taskId: string
      statusMessage: string
      createdAt: string
      lastUpdatedAt: string
      status: "cancelled"
    }
    Glob: {
      durationMs: number
      numFiles: number
      filenames: string[]
      truncated: boolean
      totalMatches?: number
      countIsComplete?: boolean
      timedOut?: boolean
    }
    Grep: {
      mode?: "content" | "files_with_matches" | "count"
      numFiles: number
      filenames: string[]
      content?: string
      numLines?: number
      numMatches?: number
      totalFiles?: number
      totalLines?: number
      appliedLimit?: number
      appliedOffset?: number
      timedOut?: boolean
    }
    ListAgents: {
      listing: string
      sections?: {
        kind: string
        total: number
        rows: {
          name?: string
          ref?: string
          id?: string
          type?: string
          status?: string
        }[]
      }[]
      notes?: {
        kind: string
        text: string
      }[]
    }
    ListConnectors: {
      connectors: {
        name?: string
      }[]
      opt_in_required?: true
      message?: string
    }
    ListMcpResourcesTool: Array<{
      uri: string
      name: string
      mimeType?: string
      description?: string
      server: string
    }>
    ListPlugins: {
      results: Array<{
        id: string
        name: string
        display_name?: string | null
        description?: string | null
        enabled?: boolean | null
        presents_as?: string | null
        installation_preference?: string | null
      }>
      note?: string
    }
    ListSkills: {
      results: Array<{
        id: string
        name: string
        display_name?: string | null
        description?: string | null
        enabled?: boolean | null
        presents_as?: string | null
        installation_preference?: string | null
      }>
      note?: string
    }
    LSP: {
      operation: "goToDefinition" | "findReferences" | "hover" | "documentSymbol" | "workspaceSymbol" | "goToImplementation" | "prepareCallHierarchy" | "incomingCalls" | "outgoingCalls"
      result: string
      filePath: string
      resultCount?: number
      fileCount?: number
    }
    McpTaskResumePolling: {
      message: string
      isError: boolean
    }
    memory_list: {
      outcome: "ok" | "refused" | "failed"
      store_kind?: "personal" | "project"
      entries?: {
        path: string
        bytes?: number
        updatedAt?: string
      }[]
      remaining?: number
      stores?: {
        id: string
        description: string
        writable: boolean
        index: string
      }[]
      reason?: string
      message?: string
    }
    memory_read: {
      outcome: "ok" | "not_found" | "refused" | "failed"
      path: string
      store_kind?: "personal" | "project"
      content?: string
      updatedAt?: string
      version?: string
      reason?: string
      message?: string
    }
    memory_write: {
      outcome: "ok" | "conflict" | "missing" | "refused" | "failed"
      path: string
      store_kind?: "personal" | "project"
      version?: string
      bytes?: number
      content?: string
      op?: "created" | "updated"
      currentVersion?: string
      currentContent?: string
      reason?: string
      message?: string
    }
    Monitor: {
      taskId: string
      timeoutMs: number
      persistent?: boolean
      keptInSandboxByCheck?: boolean
    }
    NotebookEdit: {
      new_source: string
      old_source?: string
      cell_id?: string
      cell_type: "code" | "markdown"
      language: string
      edit_mode: string
      error?: string
      notebook_path: string
      original_file: string
      updated_file: string
    }
    OfferChromeSetup: {
      outcome: "connected" | "not_now" | "no_attempt_yet"
    }
    PauseGoal: {
      condition: string
    }
    Poll: {
      content: string
      eventCount: number
      remainingWakeCount: number
      media?: Array<Array<{
        type: "image"
        source: {
          type: "base64"
          media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"
          data: string
        }
      } | {
        type: "document"
        source: {
          type: "base64"
          media_type: "application/pdf"
          data: string
        }
      }>>
      toolsUsed?: string[]
      provenance?: Array<{
        authority: "human-principal" | "human-other" | "peer-agent" | "world-event"
        senderId?: string
        senderText?: string
      } | null>
      declared?: Array<{
        kind: string
        at: string
        fields: {}
      } | null>
      rows?: Array<string | null>
    }
    PowerShell: {
      stdout: string
      stderr: string
      interrupted: boolean
      returnCodeInterpretation?: string
      isImage?: boolean
      persistedOutputPath?: string
      persistedOutputSize?: number
      backgroundTaskId?: string
      backgroundedByUser?: boolean
      backgroundedByTurnAbort?: boolean
      backgroundedToDeliverMessage?: boolean
      backgroundedForAgentReport?: true
      timedOutAfterMs?: number
      subagentCapApplied?: true
      backgroundEndsWithFinalResponse?: true
      gitOperation?: {
        commit?: {
          sha: string
          kind: "committed" | "amended" | "cherry-picked"
          branch?: string
        }
        push?: {
          branch: string
        }
        branch?: {
          ref: string
          action: "merged" | "rebased"
        }
        pr?: {
          number: number
          url?: string
          action: "created" | "edited" | "merged" | "commented" | "closed" | "reopened" | "ready" | "draft" | "auto-merge-enabled" | "auto-merge-disabled"
        }
      }
    }
    Projects: {
      method: "project_info"
      notice?: string
      local_file?: string
      name: string
      description: string
      instructions: string
      docs: Array<{
        path: string
        created_at: string | null
      }>
      files?: Array<{
        path: string
        file_kind: string
        created_at: string | null
      }>
      sync_sources?: Array<{
        type: string | null
        config: {}
      }>
      knowledge: {
        knowledge_size: number
        max_knowledge_size: number
      }
    } | {
      method: "project_read"
      notice?: string
      path: string
      version?: string
      file_kind?: string
      content?: string
      local_file?: string
      size_bytes?: number
      created_at: string | null
    } | {
      method: "project_search"
      notice?: string
      rag: boolean
      hits?: {
        name?: string
        doc_uuid?: string
        text?: string
        image_attached?: boolean
        page?: number
      }[]
      images?: Array<{
        content_id: string
        page?: number
        media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"
        data: string
      }>
      docs?: string[]
    } | {
      method: "project_write"
      notice?: string
      path: string
      doc_uuid: string
      version?: string
      replaced: boolean
      present_to_user?: boolean
      local_path?: string
    } | {
      method: "project_delete"
      notice?: string
      path: string
      deleted: boolean
    } | {
      method: "project_memory_list"
      notice?: string
      files: Array<{
        path: string
        size_bytes: number
        updated_at: string | null
        truncated: boolean
      }>
      truncated: boolean
    } | {
      method: "project_memory_read"
      notice?: string
      path: string
      content?: string
      local_file?: string
      size_bytes: number
      updated_at: string | null
      truncated: boolean
    }
    propose_skills: {
      proposalCount: number
    }
    PublishPlugin: {
      state: "published" | "in-review" | "publishing" | "on-shelf" | "refused"
      refusal?: string
      lines: string[]
    }
    PushNotification: {
      message: string
      pushSent?: boolean
      localSent?: boolean
      disabledReason?: "config_off" | "user_present" | "no_transport"
      sentAt?: string
    }
    Read: {
      type: "text"
      file: {
        filePath: string
        content: string
        numLines: number
        startLine: number
        totalLines: number
        truncatedByTokenCap?: boolean
      }
      artifactRead?: {
        slug: string
        ver: string
      }
    } | {
      type: "image"
      file: {
        base64: string
        type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"
        originalSize: number
        dimensions?: {
          originalWidth?: number
          originalHeight?: number
          displayWidth?: number
          displayHeight?: number
        }
      }
    } | {
      type: "notebook"
      file: {
        filePath: string
        cells: unknown[]
      }
    } | {
      type: "pdf"
      file: {
        filePath: string
        base64: string
        originalSize: number
      }
    } | {
      type: "parts"
      file: {
        filePath: string
        originalSize: number
        count: number
        outputDir: string
      }
      firstPage?: number
      totalPages?: number
      pages?: Array<{
        base64: string
        mediaType: "image/jpeg" | "image/png" | "image/gif" | "image/webp"
        error?: string
        text?: string
      }>
    }
    ReadMcpResourceDirTool: {
      resources: Array<{
        uri: string
        name: string
        mimeType?: string
      }>
      error?: string
    }
    ReadMcpResourceTool: {
      contents: Array<{
        uri: string
        mimeType?: string
        text?: string
        blobSavedTo?: string
      }>
      error?: string
    }
    ReadNotifications: {
      notifications: Array<{
        notification_id: string
        origin: string
        queued_at: string
        content: string
        arrived_at?: string
      }>
      remaining: number
      read_at?: string
    }
    ReadWidgetContext: {
      blocks: Array<{
        type: "text"
        text: string
      } | {
        type: "image"
        source: {
          type: "base64"
          media_type: "image/png" | "image/jpeg" | "image/gif" | "image/webp"
          data: string
        }
      }>
      isError: boolean
    }
    RefreshMcpTools: Array<{
      server: string
      status: "refreshed" | "error" | "not_connected"
      toolCount?: number
      added?: string[]
      removed?: string[]
      error?: string
    }>
    RemoteTrigger: {
      status: number
      json: string
      summary?: string
    }
    ReportFindings: {
      count: number
      level?: "low" | "medium" | "high" | "xhigh" | "max"
      findings: Array<{
        file: string
        line?: number
        summary: string
        short_summary?: string
        failure_scenario: string
        category?: string
        severity?: "important" | "pre_existing" | "nit"
        verdict?: "CONFIRMED" | "PLAUSIBLE"
        outcome?: "fixed" | "skipped" | "no_change_needed"
      }>
    }
    request_computer: {
      message: string
    }
    ScheduleWakeup: {
      scheduledFor: number
      clampedDelaySeconds: number
      wasClamped: boolean
      stopped?: boolean
      cancelledWakeups?: number
    }
    SearchMcpRegistry: {
      results: {
        name?: string
      }[]
      opt_in_required?: true
      message?: string
    }
    SearchPlugins: {
      results: Array<{
        id: string
        name: string
        display_name?: string | null
        description?: string | null
        enabled?: boolean | null
        presents_as?: string | null
        installation_preference?: string | null
      }>
      note?: string
    }
    SearchSkills: {
      results: Array<{
        id: string
        name: string
        display_name?: string | null
        description?: string | null
        enabled?: boolean | null
        presents_as?: string | null
        installation_preference?: string | null
      }>
      note?: string
    }
    self_hosted_runner_get_pool: {
      pool: {}
      equivalent: {
        ui: string
      }
    }
    self_hosted_runner_list_runners: {
      runners: {}[]
      equivalent: {
        ui: string
      }
    }
    self_hosted_runner_list_secrets: {
      secrets: {}[]
      equivalent: {
        ui: string
      }
    }
    self_hosted_runner_list_sessions: {
      sessions: {}[]
      equivalent: {
        ui: string
      }
    }
    self_hosted_runner_read_health: {
      health?: {}
      disabled?: boolean
      unreachable?: boolean
      error?: string
    }
    self_hosted_runner_read_metrics: {
      gauges?: {}
      raw?: string
      disabled?: boolean
      unreachable?: boolean
      error?: string
    }
    self_hosted_runner_requeue_session: {
      excluded_count?: number
      equivalent: {
        ui: string
      }
    }
    self_hosted_runner_spawn_local: {
      pid: number
      pid_file: string
      log_path: string
      health_port: number
      command: string
    }
    self_hosted_runner_tail_log: {
      lines: string
      bytes_read: number
      error?: string
    }
    SendFeedback: {
      success: boolean
      message: string
    }
    SendFile: {
      success: boolean
      message: string
      msg_id?: string
      files: {
        path: string
        size?: number
        sha256?: string
        file_uuid?: string
        error?: string
      }[]
    }
    SendMessage: unknown
    SendToProject: {
      created: boolean
      reason?: string
      mayExist?: boolean
      projectId?: string
      projectName?: string
      projectUrl?: string
      attachedRepo?: string | null
      appInstallPending?: boolean
      mode?: "new" | "existing"
      savedToMemory?: boolean
      memoryOmitted?: boolean
      handedOff?: boolean
      setupSubmitted?: boolean
      setupUncertain?: boolean
      threadsOnCard?: number
      message?: "sent" | "uncertain" | "not_sent" | null
      openedInBrowser?: boolean
      browserOpenPending?: boolean
      notes?: string[]
    }
    SendToProjectContext: {
      status: "delivered" | "already_delivered" | "nothing_read" | "no_run"
      context?: string
    }
    SendUserFile: {
      caption?: string
      display?: "render" | "attach"
      attachments: {
        path: string
        size: number
        isImage: boolean
        file_uuid?: string
        media_type?: string
        pathValidated?: boolean
        upload_error?: string
        upload_error_code?: string
        upload_suspected_limit_bytes?: number
        scaled?: {
          width: number
          height: number
          original_width: number
          original_height: number
        }
        thumbnail?: {
          width: number
          height: number
        }
        project_path?: string
        partial_error?: string
      }[]
      rendered_locally?: boolean
    }
    SendUserMessage: {
      message: string
      attachments?: {
        path: string
        size: number
        isImage: boolean
        file_uuid?: string
        media_type?: string
        pathValidated?: boolean
        upload_error?: string
        upload_error_code?: string
        upload_suspected_limit_bytes?: number
        scaled?: {
          width: number
          height: number
          original_width: number
          original_height: number
        }
        thumbnail?: {
          width: number
          height: number
        }
      }[]
      sentAt?: string
      rendered_locally?: boolean
    }
    SetGoal: {
      condition: string
      askUser: boolean
    }
    ShareOnboardingGuide: {
      status: "created" | "updated" | "deleted" | "has_existing" | "unavailable"
      share_url?: string
      short_code?: string
      message: string
    }
    ShowOnboardingRolePicker: {
      role?: string
      dismissed?: boolean
    }
    Skill: {
      success: boolean
      commandName: string
      allowedTools?: string[]
      model?: string
      status?: "inline"
      readOnly?: boolean
    } | {
      success: boolean
      commandName: string
      status: "forked"
      agentId: string
      result: string
      background?: boolean
      toolsUsedLine?: string
    }
    SuggestConnectors: {
      connectors: {
        name?: string
      }[]
      opt_in_required?: true
      message?: string
    }
    SuggestPluginInstall: {
      contextLabel: string
      plugins: {
        pluginId: string
        pluginName: string
        description: string
      }[]
      note: string
      trigger?: "user_asked" | "proactive"
      answer?: "added" | "not_added" | "not_now"
      added?: string[]
    }
    SuggestSkills: {
      results: Array<{
        id: string
        name: string
        display_name?: string | null
        description?: string | null
        enabled?: boolean | null
        presents_as?: string | null
        installation_preference?: string | null
      }>
      trigger?: "user_asked" | "proactive"
    }
    TaskCreate: {
      task: {
        id: string
        subject: string
        description?: string
      }
      appKeepsStatuses?: true
    }
    TaskGet: {
      task: {
        id: string
        subject: string
        description: string
        status: "pending" | "in_progress" | "completed"
        blocks: string[]
        blockedBy: string[]
      } | null
    }
    TaskList: {
      tasks: Array<{
        id: string
        subject: string
        status: "pending" | "in_progress" | "completed"
        owner?: string
        blockedBy: string[]
      }>
    }
    TaskStop: {
      message: string
      task_id: string
      task_type: string
      command?: string
    }
    TaskUpdate: {
      success: boolean
      taskId: string
      updatedFields: string[]
      error?: string
      statusChange?: {
        from: string
        to: string
      }
    }
    TodoWrite: {
      oldTodos: Array<{
        content: string
        status: "pending" | "in_progress" | "completed"
        activeForm: string
      }>
      newTodos: Array<{
        content: string
        status: "pending" | "in_progress" | "completed"
        activeForm: string
      }>
    }
    ToolSearch: {
      matches: string[]
      query: string
      total_deferred_tools: number
      pending_mcp_servers?: string[]
      failed_mcp_servers?: {
        name: string
        errorCode?: string
        error?: string
      }[]
    }
    WaitForMcpServers: {
      ready: boolean
      connected: string[]
      cached?: string[]
      failed: string[]
      stillPending: string[]
      needsAuth: string[]
      disabled: string[]
      unconfigured?: string[]
      unknown: string[]
    }
    WebFetch: {
      bytes: number
      code: number
      codeText: string
      result: string
      durationMs: number
      url: string
      citable?: true
      artifactRead?: {
        slug: string
        ver?: string
        seeded?: false
      }
    }
    WebSearch: {
      query: string
      results: Array<{
        tool_use_id: string
        content: Array<{
          title: string
          url: string
          snippet?: string
        }>
      } | string>
      durationSeconds: number
      searchCount?: number
      plainPageText?: true
    }
    Workflow: {
      status: "async_launched" | "remote_launched"
      taskId: string
      taskType?: "local_workflow" | "remote_agent"
      workflowName?: string
      runId?: string
      summary?: string
      transcriptDir?: string
      scriptPath?: string
      sessionUrl?: string
      warning?: string
      error?: string
    }
    WrapUp: {
      asks: boolean
      nextStep?: {
        recap: string
        ask?: string
        blocked: boolean
        actions: Array<{
          label: string
        } | {
          action: "verify" | "fix_ci" | "address_comments" | "resolve_conflicts"
        }>
      }
    }
    Write: {
      type: "create" | "update"
      filePath: string
      content: string
      structuredPatch: {
        oldStart: number
        oldLines: number
        newStart: number
        newLines: number
        lines: string[]
      }[]
      originalFile: string | null
      gitDiff?: {
        filename: string
        status: "modified" | "added"
        additions: number
        deletions: number
        changes: number
        patch: string
        repository?: string | null
      }
      userModified?: boolean
      staged?: boolean
      stagedWording?: "review" | "card" | "cloud" | "linked" | "policy"
    }
    Yield: {
      content: string
      eventCount: number
      remainingWakeCount: number
      media?: Array<Array<{
        type: "image"
        source: {
          type: "base64"
          media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"
          data: string
        }
      } | {
        type: "document"
        source: {
          type: "base64"
          media_type: "application/pdf"
          data: string
        }
      }>>
      toolsUsed?: string[]
      provenance?: Array<{
        authority: "human-principal" | "human-other" | "peer-agent" | "world-event"
        senderId?: string
        senderText?: string
      } | null>
      declared?: Array<{
        kind: string
        at: string
        fields: {}
      } | null>
      rows?: Array<string | null>
    }
  }
}
