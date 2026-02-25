## Context
The project currently mixes legacy Python 2.7 references with Python 3 documentation and CI behavior. The requested target is Python 3.13 as the supported baseline.

## Goals / Non-Goals
- Goals:
  - Remove Python 2 support language and compatibility code.
  - Align docs and CI configuration with Python 3.13 baseline.
- Non-Goals:
  - Porting unrelated runtime APIs.
  - Refactoring historical Docker image matrix beyond Python version cleanup.

## Decisions
- Decision: Use Python 3.13+ as the normative requirement in docs/spec.
- Decision: Delete Python 2 CI jobs instead of retaining deprecated paths.
- Decision: Remove Python 2 fallback import logic and use standard Python 3 logging handler.

## Risks / Trade-offs
- Risk: This may break users still relying on Python 2 workflows.
- Mitigation: Explicitly document Python 3.13+ requirement in docs and contributor guidance.
