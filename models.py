from dataclasses import dataclass
from typing import Optional


@dataclass
class Finding:
    title: str
    tool: str
    category: str  
    severity: str  

    description: Optional[str] = None
    cwe: Optional[str] = None
    cve: Optional[str] = None

    file_path: Optional[str] = None
    line: Optional[int] = None

    package_name: Optional[str] = None
    package_version: Optional[str] = None

    confidence: str = "MEDIUM"