import argparse
import sys

from semgrep_adapter import run_semgrep_scan
from trivy_adapter import run_trivy_scan
from sonarqube_adapter import run_sonarqube_scan
from correlation import deduplicate_findings
from report import print_report
from json_report import save_json_report
from summary import generate_summary


def run_scan(output_file, scanners):
    findings = []

    if "semgrep" in scanners:
        findings.extend(run_semgrep_scan())

    if "trivy" in scanners:
        findings.extend(run_trivy_scan())

    if "sonarqube" in scanners:
        findings.extend(run_sonarqube_scan())

    deduplicated_findings = deduplicate_findings(findings)

    print_report(deduplicated_findings)
    save_json_report(deduplicated_findings, output_file)

    summary = generate_summary(deduplicated_findings)

    if summary["block"] > 0:
        print("\nBuild failed: blocked findings detected.")
        sys.exit(1)

    print("\nBuild passed: no blocked findings detected.")
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Unified AppSec Orchestrator"
    )

    parser.add_argument(
        "--output",
        default="appsec_report.json",
        help="Path to save the JSON report"
    )

    parser.add_argument(
        "--scanners",
        nargs="+",
        choices=["semgrep", "trivy", "sonarqube"],
        default=["semgrep", "trivy", "sonarqube"],
        help="Scanners to run"
    )

    args = parser.parse_args()
    run_scan(args.output, args.scanners)


if __name__ == "__main__":
    main()