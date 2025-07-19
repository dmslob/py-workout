import unittest


class TestDictionaries(unittest.TestCase):

    def test_dictionary_read_and_write(self):
        # given
        tel = {'jack': 4098, 'sape': 4139}
        # when
        tel['guido'] = 4127
        # then
        self.assertEqual(tel['guido'], 4127)
        self.assertEqual(list(tel.values()), [4098, 4139, 4127])
        # when
        del tel['sape']
        # then
        self.assertEqual(list(tel.values()), [4098, 4127])
        self.assertEqual(list(tel.keys()), ['jack', 'guido'])
        # when
        sorted_tel = sorted(tel)
        # then
        self.assertEqual(list(sorted_tel), ['guido', 'jack'])
        self.assertTrue('guido' in tel)
        self.assertFalse('jack' not in tel)

    def test_create_dict(self):
        # when
        dc = {x: x ** 2 for x in (2, 4, 6)}
        # then
        self.assertEqual(list(dc.keys()), [2, 4, 6])
        self.assertEqual(list(dc.values()), [4, 16, 36])

    def test_iteration(self):
        knights = {'gallahad': 'the pure', 'robin': 'the brave'}
        for k, v in knights.items():
            print(k, v)

        for i, v in enumerate(['tic', 'tac', 'toe']):
            print(i, v)

        for i, j in [(1, 2), (1, 3)]:
            print(i, j)
