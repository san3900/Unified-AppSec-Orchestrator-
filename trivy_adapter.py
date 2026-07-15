from models import Finding


def run_trivy_scan():
    findings = [
        Finding(
            title="Vulnerable lodash dependency",
            tool="trivy",
            category="SCA",
            severity="CRITICAL",
            description="Trivy detected a vulnerable lodash dependency.",
            cve="CVE-2021-23337",
            package_name="lodash",
            package_version="4.17.20",
        ),
        Finding(
            title="Vulnerable minimist dependency",
            tool="trivy",
            category="SCA",
            severity="HIGH",
            description="Trivy detected a vulnerable minimist dependency.",
            cve="CVE-2021-44906",
            package_name="minimist",
            package_version="1.2.5",
        ),
    ]

    return findings