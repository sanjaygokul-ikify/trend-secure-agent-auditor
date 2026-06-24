import asyncio
from ..core.engine import run_audit
from ..core.types import AgentTask

async def run_audit(audit_id: str, tasks: list) -> list:
    # Validate the agent tasks
    for task in tasks:
        validate_agent_task(task)
    # Run the audit
    results = await run_audit(audit_id, tasks)
    return results

def validate_agent_task(task: AgentTask) -> None:
    # Validate the agent task
    if not task.task_id:
        raise ValueError("Task ID is required")
    if not task.agent_id:
        raise ValueError("Agent ID is required")
