from typing import List
import asyncio
from packages.core import AgentTask, run_audit

class Orchestrator:
    async def run(self, audit_id: str, tasks: List[AgentTask]) -> List[AgentTask]:
        results = await run_audit(audit_id, tasks)
        return tasks