# SLA Deadline Checker

Computes incident age from explicit timestamps and compares it with each supplied SLA target. It identifies breached incidents without contacting an incident system.

## Architecture

```text
JSON payload → domain algorithm → evidence-backed findings → human review
                              └→ OpenAI / CrewAI / Claude Code / Lyzr export surfaces
```

The core implementation is `agent.py` and exposes `analyze(payload)`. Tests include valid, malformed, boundary, and domain-specific cases.

## Run

```bash
python3 agent.py examples/good-input.json
python3 -m unittest discover -s tests -v
python3 tools/audit-sla-deadline-checker.py examples/good-input.json
```

## Limitations

The checker does not account for pause windows, business hours, acknowledgements, service credits, or contractual exceptions. It reports arithmetic against supplied timestamps and does not page, escalate, or change incident state.
