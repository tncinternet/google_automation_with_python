import main
import changeImage
import unittest
import imghdr
import run


class TestMain(unittest.TestCase):
    def test_dict(self):
        testcase = run.dict_fruits('fruittexttest')
        expected = [{'name': 'papaya', 'weight': '200', 'description': 'papaya description short', 'image_name': '010.jpeg'}]
        print(expected)
        self.assertEqual(testcase, expected)


#
#     def test_empty(self):
#         testcase = ""
#         expected = ""
#         self.assertEqual(rearrange_name(testcase), expected)
#
#     def test_double_name(self):
#         testcase = "Hopper, Grace M."
#         expected = "Grace M. Hopper"
#         self.assertEqual(rearrange_name(testcase), expected)
#
#     def test_one_name(self):
#         testcase = "Jeffry"
#         expected = "Jeffry"
#         self.assertEqual(rearrange_name(testcase), expected)
#
#     def test_digit(self):
#         testcase = 100
#         expected = ""
#         self.assertEqual(rearrange_name(testcase), expected)
unittest.main()
