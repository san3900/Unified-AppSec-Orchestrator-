from risk import calculate_risk_score
from policy import decide_action
from summary import generate_summary


def print_report(findings):
    print("\nUnified AppSec Report")
    print("====================")

    summary = generate_summary(findings)

    print("\nSummary")
    print("=======")
    print(f"Total Findings: {summary['total']}")
    print(f"Critical: {summary['critical']}")
    print(f"High: {summary['high']}")
    print(f"Medium: {summary['medium']}")
    print(f"Low: {summary['low']}")
    print(f"Info: {summary['info']}")
    print(f"Blocked Findings: {summary['block']}")
    print(f"Warn Findings: {summary['warn']}")
    print(f"Allowed Findings: {summary['allow']}")

    for index, finding in enumerate(findings, start=1):
        print(f"\nFinding #{index}")
        print(f"Title: {finding.title}")
        print(f"Tool: {finding.tool}")
        print(f"Category: {finding.category}")
        print(f"Severity: {finding.severity}")

        risk_score = calculate_risk_score(finding)
        print(f"Risk Score: {risk_score}")

        action = decide_action(finding, risk_score)
        print(f"Policy Action: {action}")

        if finding.description:
            print(f"Description: {finding.description}")

        if finding.cwe:
            print(f"CWE: {finding.cwe}")

        if finding.cve:
            print(f"CVE: {finding.cve}")

        if finding.file_path:
            print(f"File: {finding.file_path}")

        if finding.line:
            print(f"Line: {finding.line}")

        if finding.package_name:
            print(f"Package: {finding.package_name}")

        if finding.package_version:
            print(f"Version: {finding.package_version}")

        print(f"Confidence: {finding.confidence}")