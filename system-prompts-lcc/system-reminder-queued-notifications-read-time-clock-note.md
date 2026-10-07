<!--
name: 'System Reminder: Queued notifications read-time clock note'
description: >-
  Clock note inserted into the queued-notifications delivery stating when the
  read was made by the machine's clock and explaining how to interpret each
  notification header's queued-at, reached-this-session and whole-wait times
  given possible clock differences.
ccVersion: 2.1.292
variables:
  - DATE_CLASS
  - READ_TIMESTAMP_MS
  - CLOCK_SKEW_TOLERANCE_MINUTES
-->
 This read was made at ${new DATE_CLASS(READ_TIMESTAMP_MS).toISOString()} by this machine's clock. A time that a body tells you to treat as current is when that notification fired, which is earlier than now by however long it waited. In each header, "queued at" is when the server queued the notification, by the server's clock, and "reached this session" is how long before this read it arrived here. Where its queued-at time is more than ${CLOCK_SKEW_TOLERANCE_MINUTES} minutes before its arrival here, the header also gives the whole wait, which compares the two clocks and can be off by their difference. Where the header gives no whole wait, count the notification as having waited only the time since it reached this session: a gap of up to ${CLOCK_SKEW_TOLERANCE_MINUTES} minutes between its queued-at time and its arrival here may be just the two clocks.
