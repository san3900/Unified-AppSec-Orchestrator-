from models import Finding


def run_semgrep_scan():
    findings = [
        Finding(
            title="Possible SQL Injection",
            tool="semgrep",
            category="SAST",
            severity="HIGH",
            description="Semgrep detected possible SQL injection.",
            cwe="CWE-89",
            file_path="src/db.py",
            line=42,
        ),
        Finding(
            title="Hardcoded Secret",
            tool="semgrep",
            category="SECRET",
            severity="CRITICAL",
            description="Semgrep detected a possible hardcoded secret.",
            cwe="CWE-798",
            file_path="src/config.py",
            line=10,
        ),
    ]

    return findings