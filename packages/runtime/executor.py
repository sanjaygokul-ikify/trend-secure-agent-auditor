import asyncio
from ..core.engine import run_audit
from ..core.types import AgentTask

async def run_audit(audit_id: str, tasks: list) -> list:
    try:
        # Validate the agent tasks
        for task in tasks:
            validate_agent_task(task)
        # Run the audit
        results = await asyncio.wait_for(run_audit(audit_id, tasks), timeout=60)
        return results
    except asyncio.TimeoutError:
        # Handle the timeout error
        raise
    except Exception as e:
        # Handle any exceptions that occur during audit execution
        raise

def validate_agent_task(task: AgentTask) -> None:
    # Validate the agent task
    if not task.task_id:
        raise ValueError("Task ID is required")
    if not task.agent_id:
        raise ValueError("Agent ID is required")
