import unittest

from add_two_numbers import add_two_numbers


class TestAddTwoNumbers(unittest.TestCase):

    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(1, 2), 3)
        self.assertEqual(add_two_numbers(-1, -2), -3)
        self.assertEqual(add_two_numbers(0, 0), 0)


if __name__ == "__main__":
    unittest.main()

import unittest

from add_two_numbers import add_two_numbers


class TestAddTwoNumbers(unittest.TestCase):

    def test_add_two_numbers_with_valid_input(self):
        # Create two valid numbers.
        num1 = 1
        num2 = 2

        # Add the two numbers together.
        expected_sum = num1 + num2

        # Call the `add_two_numbers()` function.
        actual_sum = add_two_numbers(num1, num2)

        # Assert that the actual sum is equal to the expected sum.
        self.assertEqual(actual_sum, expected_sum)

        # Various other cases
        self.assertEqual(add_two_numbers(1, 2), 3)
        self.assertEqual(add_two_numbers(-1, -2), -3)
        self.assertEqual(add_two_numbers(0, 0), 0)

    def test_add_two_numbers_with_invalid_input(self):
        # Create an invalid number.
        num1 = "a"

        # Call the `add_two_numbers()` function.
        with self.assertRaises(TypeError):
            add_two_numbers(num1, 2)

    def test_add_two_numbers_with_empty_input(self):
        # Create an empty input.
        nums = ""

        # Call the `add_two_numbers()` function.
        with self.assertRaises(ValueError):
            add_two_numbers(nums)


if __name__ == "__main__":
    unittest.main()