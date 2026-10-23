import unittest
from password_analyzer import analyze_password, has_sequence


class PasswordAnalyzerTests(unittest.TestCase):
    def test_empty_password(self):
        self.assertEqual(analyze_password("").score, 0)

    def test_common_password(self):
        self.assertEqual(analyze_password("password123").rating, "Very weak")

    def test_short_password(self):
        self.assertLessEqual(analyze_password("A7!").score, 1)

    def test_long_varied_password(self):
        self.assertEqual(analyze_password("Maple!Cloud7River#29").rating, "Strong")

    def test_sequence_detection(self):
        self.assertTrue(has_sequence("Hello1234World!"))
        self.assertTrue(has_sequence("Testdcba2026!"))

    def test_repeated_characters_penalty(self):
        result = analyze_password("LongPassphrase!!!X7")
        self.assertTrue(any("repeating" in item for item in result.feedback))

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            analyze_password(None)


if __name__ == "__main__":
    unittest.main()
