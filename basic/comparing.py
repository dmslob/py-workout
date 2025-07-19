import unittest


class TestComparingFunctions(unittest.TestCase):

    def test_return_first_non_empty_string(self):
        # given
        string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
        # when
        # short-circuit operator
        non_empty = string1 or string2 or string3
        # then
        self.assertEqual(non_empty, "Trondheim")

    def test_comparing(self):
        self.assertTrue((1, 2, 3) < (1, 2, 4))
        self.assertTrue([1, 2, 3] < [1, 2, 4])

        with self.assertRaises(TypeError):
            r3 = (1, 2, 3) < [1, 2, 4]

        self.assertTrue('ABC' < 'C' < 'Pascal' < 'Python')
        self.assertTrue((1, 2, 3, 4) < (1, 2, 4))
        self.assertTrue((1, 2) < (1, 2, -1))
        self.assertTrue((1, 2, 3) == (1.0, 2.0, 3.0))
        self.assertTrue((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))


# to run from terminal
# python3 -m unittest -v comparing.py
# if __name__ == '__main__':
#     unittest.main()
