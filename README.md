# Unified AppSec Orchestrator

A Prototype AppSec orchestration platform that simulates multiple security scanners, normalizes findings, deduplicates duplicate issues, scores risk, applies policy decisions, prints a terminal report, and saves a JSON report.

## Features

- Scanner adapters for Semgrep, Trivy, and SonarQube
- Common `Finding` model for all scanner outputs
- Duplicate finding correlation
- Risk scoring based on severity
- Policy actions: `BLOCK`, `WARN`, `ALLOW`
- Terminal summary report
- JSON report with summary and findings
- CI/CD-style exit codes

## Run

From inside the `ORCHESTRATOR` folder:

```bash
python main.py