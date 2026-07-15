from risk import calculate_risk_score
from policy import decide_action


def generate_summary(findings):
    summary = {
        "total": len(findings),
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "info": 0,
        "block": 0,
        "warn": 0,
        "allow": 0,
    }

    for finding in findings:
        severity = finding.severity.lower()

        if severity in summary:
            summary[severity] += 1

        risk_score = calculate_risk_score(finding)
        action = decide_action(finding, risk_score).lower()

        if action in summary:
            summary[action] += 1

    return summary