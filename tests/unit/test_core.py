import asyncio
import unittest
from packages.core import AgentTask, AuditResult, run_audit, validate_agent_task, InvalidAgentTaskError

class TestCore(unittest.IsolatedAsyncioTestCase):
    async def test_run_audit(self):
        tasks = [AgentTask(task_id='task-1', agent_id='agent-1'), AgentTask(task_id='task-2', agent_id='agent-2')]
        results = await run_audit('example-audit', tasks)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].task_id, 'task-1')
        self.assertEqual(results[0].agent_id, 'agent-1')
        self.assertEqual(results[1].task_id, 'task-2')
        self.assertEqual(results[1].agent_id, 'agent-2')

    def test_validate_agent_task(self):
        task = AgentTask(task_id='task-1', agent_id='agent-1')
        validate_agent_task(task)

        task = AgentTask(task_id='', agent_id='agent-1')
        with self.assertRaises(InvalidAgentTaskError):
            validate_agent_task(task)

        task = AgentTask(task_id='task-1', agent_id='')
        with self.assertRaises(InvalidAgentTaskError):
            validate_agent_task(task)

if __name__ == '__main__':
    unittest.main()