def deduplicate_findings(findings):
    unique_findings = {}

    for finding in findings:
        key = create_finding_key(finding)

        if key not in unique_findings:
            unique_findings[key] = finding
        else:
            existing_finding = unique_findings[key]
            existing_finding.tool = existing_finding.tool + ", " + finding.tool
            existing_finding.confidence = "HIGH"

    return list(unique_findings.values())


def create_finding_key(finding):
    if finding.cve:
        return f"CVE:{finding.cve}"

    if finding.cwe and finding.file_path:
        return f"CWE:{finding.cwe}:FILE:{finding.file_path}"

    return f"TITLE:{finding.title}:SEVERITY:{finding.severity}"