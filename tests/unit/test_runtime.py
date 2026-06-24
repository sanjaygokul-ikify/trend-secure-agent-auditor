import asyncio
import unittest
from packages.core import run_audit

class TestRuntime(unittest.IsolatedAsyncioTestCase):
    async def test_run_audit(self):
        tasks = []
        results = await run_audit('example-audit', tasks)
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()