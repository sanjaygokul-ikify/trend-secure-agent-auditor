import asyncio
import unittest
from packages.core import AgentTask, run_audit
from packages.cli.main import main as cli_main

class TestPipeline(unittest.IsolatedAsyncioTestCase):
    async def test_pipeline(self):
        tasks = [AgentTask(task_id='task-1', agent_id='agent-1'), AgentTask(task_id='task-2', agent_id='agent-2')]
        results = await run_audit('example-audit', tasks)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].task_id, 'task-1')
        self.assertEqual(results[0].agent_id, 'agent-1')
        self.assertEqual(results[1].task_id, 'task-2')
        self.assertEqual(results[1].agent_id, 'agent-2')

        await cli_main('example-audit', tasks)

if __name__ == '__main__':
    unittest.main()