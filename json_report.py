import json
from dataclasses import asdict

from summary import generate_summary


def save_json_report(findings, output_file="appsec_report.json"):
    report_data = {
        "summary": generate_summary(findings),
        "findings": [],
    }

    for finding in findings:
        report_data["findings"].append(asdict(finding))

    with open(output_file, "w") as file:
        json.dump(report_data, file, indent=4)

    print(f"\nJSON report saved to: {output_file}")