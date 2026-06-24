from dataclasses import dataclass
from typing import List

@dataclass
class AgentTask:
    task_id: str
    agent_id: str

@dataclass
class Finding:
    id: str
    description: str

@dataclass
class AuditResult:
    task_id: str
    agent_id: str
    findings: List[Finding]