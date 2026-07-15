from models import Finding


def run_sonarqube_scan():
    findings = [
        Finding(
            title="SQL Injection",
            tool="sonarqube",
            category="SAST",
            severity="HIGH",
            description="SonarQube detected possible SQL injection.",
            cwe="CWE-89",
            file_path="src/db.py",
            line=43,
        )
    ]

    return findings