import unittest

TestBool = None


class BoolFieldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global TestBool
        from test_bool_proto import TestBool

    def test_bool_field(self):
        message = TestBool()
        self.assertIsInstance(message.bool_field, bool)
        self.assertIs(message.bool_field, False)
        message.bool_field = True
        self.assertIs(message.bool_field, True)

    def test_bool_list(self):
        message = TestBool()
        message.bool_list.append(False)
        self.assertIsInstance(message.bool_list[0], bool)
        self.assertIs(message.bool_list[0], False)
        message.bool_list.append(True)
        self.assertIs(message.bool_list[1], True)
