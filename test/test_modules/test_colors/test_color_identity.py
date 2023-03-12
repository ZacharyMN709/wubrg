import unittest

from core.colors.color_identity import ColorIdentity


class TestColorIdentity(unittest.TestCase):

    def test(self):
        self.assertEqual(ColorIdentity.C, ColorIdentity.by_name(''))