import unittest
from collections import Counter

text = ('A LLM takes a sequence of words as input and predicts the most likely next word, '
        'generating text one token at a time. LLM are neural networks trained on vast '
        'text datasets to perform a fundamental task: predicting the next word in a sequence. '
        'This simple objective drives the sophisticated capabilities we see in systems like GPT and ChatGPT.')


class TestCountWords(unittest.TestCase):

    def test_return_counter(self):
        # given
        words = text.split()
        expected = [('a', 4), ('the', 3), ('LLM', 2), ('and', 2), ('next', 2)]
        # when
        counter = Counter(words)
        counts = counter.most_common(5)
        # then
        self.assertEqual(counts, expected)


if __name__ == '__main__':
    unittest.main()
