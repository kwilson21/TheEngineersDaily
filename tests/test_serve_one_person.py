import unittest
from src.serve_one_person import main

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