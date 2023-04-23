from typing import Any, Callable, TypeVar, Iterable, Hashable
from unittest import TestCase
from itertools import product


T = TypeVar('T')


class ExtendedTestCase(TestCase):  # pragma: nocover
    """A TestCase class, which adds in additional tests."""

    # TODO: Add this in a generic way. (Abstract Base Classes?)
    # ordered = custom_order_tests(unittest.defaultTestLoader)

    # noinspection PyPep8Naming
    def assertInValue(self, obj1: T, obj2: T, expected_value: bool):
        """
        Asserts whether an object should is in another or not.

        Based on ``expected_value`` uses ``assertIn`` or ``assertNotIn``
        to handle the test. Doing this improves the readability of error
        messages that generate on failed tests.

        :param obj1: The object to determine inclusion of.
        :param obj2: The object the first is included, or not included, in.
        :param expected_value: Whether ``obj1`` should be in ``obj2``.
        """
        if expected_value:
            self.assertIn(obj1, obj2)
        else:
            self.assertNotIn(obj1, obj2)

    # region Dunder Method Tests
    # noinspection PyPep8Naming
    def assertEqualityResult(self, op: Callable[[T, T], bool], obj1: T, obj2: T, expected_value: bool):
        """
        Asserts that a function which compares two objects returns a particular boolean value.

        Based on ``expected_value`` uses ``assertTrue`` or ``assertFalse``
        to handle the test. Doing this improves the readability of error
        messages that generate on failed tests.

        :param op: The function to run.
        :param obj1: The 1st argument to ``op``.
        :param obj2: The 2st argument to ``op``.
        :param expected_value: The value the function and arguments should return.
        """
        if expected_value:
            self.assertTrue(op(obj1, obj2), f"{obj1.__repr__()}.{op.__qualname__}({obj2.__repr__()}) should be True")
        else:
            self.assertFalse(op(obj1, obj2), f"{obj1.__repr__()}.{op.__qualname__}({obj2.__repr__()}) should be False")

    @staticmethod
    def _gen_dunder_test_msg(obj: T, op: str, true_val, expected) -> str:
        """
        Generates a simple message to describe a test failure.

        :param obj: The object which the message is about.
        :param op: The method that failed to generate a correct result.
        :param true_val: The value that the object generated.
        :param expected: The value that _should_ have been generated.
        :return: An error message for a unit test.
        """
        return f"{obj}'s `{op}` was not `{expected}` (was `{true_val}`)"

    def _test_single_dunder(self, obj: T, op: Callable, expected):
        """
        Tests a dunder which only requires a reference to a single object.

        :param obj: The object to test.
        :param op: The method to test (len, str, repr, etc.)
        :param expected: The value expected to be generated.
        """
        true_val = op(obj)
        self.assertEqual(true_val, expected,
                         msg=self._gen_dunder_test_msg(obj, op.__qualname__, true_val, expected))

    # noinspection PyPep8Naming
    def assertLengthDunderEqual(self, obj: T, expected: int):
        """
        Tests the ``__len__`` dunder method of the object.

        :param obj: The object to test.
        :param expected: The result the method should return.
        """
        self._test_single_dunder(obj, len, expected)

    # noinspection PyPep8Naming
    def assertIterDunderEqual(self, obj: T, expected: Iterable):
        """
        Tests the ``__iter__`` dunder method of the object.

        :param obj: The object to test.
        :param expected: The result the method should return.
        """
        expected: list = list(expected)
        true_val: list = list(obj.__iter__())
        self.assertListEqual(true_val, expected,
                             msg=self._gen_dunder_test_msg(obj, 'iter', true_val, expected))

    # noinspection PyPep8Naming
    def assertStringDunderEqual(self, obj: T, expected: str):
        """
        Tests the ``__str__`` dunder method of the object.

        :param obj: The object to test.
        :param expected: The result the method should return.
        """
        self._test_single_dunder(obj, str, expected)

    # noinspection PyPep8Naming
    def assertReprDunderEqual(self, obj: T, expected: str):
        """
        Tests the ``__repr__`` dunder method of the object.

        :param obj: The object to test.
        :param expected: The result the method should return.
        """
        self._test_single_dunder(obj, repr, expected)

    # noinspection PyPep8Naming
    def assertHashDunderEqual(self, obj: T, expected: Hashable):
        """
        Tests the ``__hash__`` dunder method of the object.

        :param obj: The object to test.
        :param expected: The result the method should return.
        """
        expected: int = hash(expected)
        self._test_single_dunder(obj, hash, expected)

    # noinspection PyPep8Naming
    def assertBoolDunderEqual(self, obj: T, expected: bool):
        """
        Tests the ``__bool__`` dunder method of the object.

        :param obj: The object to test.
        :param expected: The result the method should return.
        """
        self._test_single_dunder(obj, bool, expected)
    # endregion Dunder Method Tests

    # region AssetAllEqual
    # noinspection PyPep8Naming
    def assertAllEqualTransitive(self, objects: list[T]):
        """
        Test that a list of objects are equal, assuming that the equality is transitive.

        Takes the list of objects, and checks they are equal in a pairwise fashion.

        :param objects: The list of objects to compare.
        """
        # Walks from each end of the list, towards the middle, comparing pairs.
        #  When the indexes meet or cross, the bottom index resets to 0, while the
        #  upper index does not. This effectively splits the list in half on the next
        #  iteration which walks toward the middle again, but with the end being the
        #  middle of the previous list. This checks all pairs are equal to each other
        #  in the fewest number of checks.
        #  0*  1   2   3   4   5   6^    (*) b_idx: 0  (^) u_idx: 6
        #  0   1*  2   3   4   5^  6     (*) b_idx: 1  (^) u_idx: 5
        #  0   1   2*  3   4^  5   6     (*) b_idx: 2  (^) u_idx: 4
        #  0   1   2   3*^ 4   5   6     (*) b_idx: 3  (^) u_idx: 3  Skip compare, reset b_idx
        #  0*  1   2   3^  4   5   6     (*) b_idx: 0  (^) u_idx: 3
        #  0   1*  2^  3   4   5   6     (*) b_idx: 1  (^) u_idx: 2
        #  0   1^  2*  3   4   5   6     (*) b_idx: 2  (^) u_idx: 1  Skip compare, reset b_idx
        #  0*  1^  2   3   4   5   6     (*) b_idx: 0  (^) u_idx: 1
        #  0^  1*  2   3   4   5   6     (*) b_idx: 1  (^) u_idx: 0  Skip compare, complete
        u_idx = len(objects) - 1
        while u_idx > 0:
            b_idx = 0
            while b_idx < u_idx:
                obj1, obj2 = objects[b_idx], objects[u_idx]
                self.assertEqual(obj1, obj2)
                b_idx, u_idx = b_idx + 1, u_idx - 1

    # noinspection PyPep8Naming
    def assertAllEqualNonTransitive(self, objects: list[T]):
        """
        Test that a list of objects are equal, assuming that the equality is not transitive.

        Takes the cross-product of the list of objects, and checks that each pair is equal.

        :param objects: The list of objects to compare.
        """
        pairs = list(product(objects, repeat=2))
        for i in range(len(pairs)):
            obj1: T
            obj2: T
            obj1, obj2 = pairs[i]
            self.assertEqual(obj1, obj2)

    # noinspection PyPep8Naming
    def assertAllEqual(self, objects: list[T], eq_transitive: bool = True):
        """
        Asserts that all objects in a list are equal.

        This test supports a "fast" and a "thorough" testing. By default,
        the "fast" testing is used, which matches objects pairwise and
        checks their equality. Generally, this should be fine.

        If equality is not transitive, ``eq_transitive`` should be set to
        ``False``, which will test the equality of each object with each
        object in the list (including itself).

        :param objects: The list of objects to check are equal.
        :param eq_transitive: Whether the equality is transitive.
        """
        if eq_transitive:
            self.assertAllEqualTransitive(objects)
        else:
            self.assertAllEqualNonTransitive(objects)
    # endregion AssetAllEqual


class EnumTestCase(ExtendedTestCase):  # pragma: nocover
    """A TestCase class, which adds in additional tests and support for Enums."""

    # noinspection PyPep8Naming
    def assertEnumCount(self, cls: Iterable, count: int):
        """
        Tests that the FlagEnum range is limited to the bits that it uses.

        :param cls: The Enum class.
        :param count: The number of enum values which should be instantiated by default.
        """
        real_size = len([x for x in cls])
        self.assertEqual(real_size, count, msg=f"Enum had {real_size} elements, not {count}")


class FlagEnumTestCase(ExtendedTestCase):  # pragma: nocover
    """A TestCase class, which adds in additional tests and support for FlagEnums."""

    # noinspection PyPep8Naming
    def assertStrictFlagEnumRange(self, cls: type, bit_count: int):
        """
        Tests that the FlagEnum range is limited to the bits that it uses.

        :param cls: The FlagEnum class.
        :param bit_count: The number of bits used in the flags.
        """
        abs_range = 2 ** bit_count
        test_range = abs_range + (bit_count * 10)
        for i in range(-test_range, test_range):
            if i < -abs_range or i > (abs_range - 1):
                self.assertRaises(ValueError, cls, i)
            else:
                self.assertIsInstance(cls(i), cls)
