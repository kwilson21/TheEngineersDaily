import unittest
from src.serve_one_person import main
import subprocess

class TestServeOnePerson(unittest.TestCase):

    def test_serve_person(self):
        res = subprocess.run(
            ["python", "src/serve_one_person.py", "--person", "Ruth", "--task", "see the next appointment action", "--success", "she can call the right family before leaving work"],
            capture_output=True,
            text=True,
        )

        expected_res = "Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work."

        self.assertEqual(res.stdout.strip(), expected_res)
        self.assertEqual(res.returncode, 0)