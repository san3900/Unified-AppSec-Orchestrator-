def decide_action(finding, risk_score):
    if finding.severity.upper() == "CRITICAL":
        return "BLOCK"

    if risk_score >= 75:
        return "WARN"

    return "ALLOW"