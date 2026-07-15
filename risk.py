def calculate_risk_score(finding):
    severity_scores = {
        "CRITICAL": 100,
        "HIGH": 75,
        "MEDIUM": 50,
        "LOW": 25,
        "INFO": 10,
    }

    return severity_scores.get(finding.severity.upper(), 0)