# Decision and Reasoning

An incident is breached when its nonnegative age exceeds target_minutes. The aggregate status is breached if any incident breaches, otherwise it is within_sla. The implementation returns structured findings so a reviewer can see how each result was derived.

# Inputs and Data Sources

The caller supplies a timezone-aware now timestamp and incidents with unique caller identifiers, timezone-aware started_at timestamps, and nonnegative target durations in minutes. No machine clock or severity mapping is inferred. The only data source is the caller-provided payload plus the checked-in rules and code; no network or private-file access is used.

# Known Limitations and Constraints

The checker does not account for pause windows, business hours, acknowledgements, service credits, or contractual exceptions. It reports arithmetic against supplied timestamps and does not page, escalate, or change incident state. The result is a bounded pre-review aid and must not be presented as professional certification or an official HiDevs result.
