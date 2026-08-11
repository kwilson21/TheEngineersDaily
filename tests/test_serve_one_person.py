import unittest
from src.serve_one_person import main, run_cli
import contextlib
import io

class TestServeOnePerson(unittest.TestCase):

    def test_valid_serve_person(self):
        res = main()
        expected_res = "Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work."
        self.assertEqual(res, expected_res)

    def test_invalid_serve_person(self):
        with self.assertRaises(ValueError) as e:
            main("/Users/kazon/repos/TheEngineersDaily/tests/data/incomplete_ruth_requirement.json")

        error_message = "Saved requirement is incomplete: success is required. Add a non-empty success value to the saved requirement file."

        value_error = e.exception

        self.assertEqual(str(value_error), error_message)

    def test_invalid_run_cli(self):
        stderr_buf = io.StringIO()
        stdout_buf = io.StringIO()

        error_message = "Saved requirement is incomplete: success is required. Add a non-empty success value to the saved requirement file."

        with contextlib.redirect_stderr(stderr_buf), contextlib.redirect_stdout(stdout_buf):
            res = run_cli("tests/data/incomplete_ruth_requirement.json")

        self.assertEqual(stdout_buf.getvalue(), "")
        self.assertEqual(stderr_buf.getvalue(), error_message)
        self.assertEqual(res, 1)

    def test_valid_run_cli(self):
        stderr_buf = io.StringIO()
        stdout_buf = io.StringIO()

        success_message = "Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work."

        with contextlib.redirect_stderr(stderr_buf), contextlib.redirect_stdout(stdout_buf):
            res = run_cli()

        self.assertEqual(stderr_buf.getvalue(),"")
        self.assertEqual(stdout_buf.getvalue(), success_message + "\n")
        self.assertEqual(res, 0)