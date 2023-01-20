from unittest import TestCase, main

from translator import english_to_french, french_to_english


class TestEngishToFrench(TestCase):
    def test_null(self):
        self.assertEqual(english_to_french(None), None)

    def test_empty(self):
        self.assertEqual(english_to_french(''), '')

    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_how_are_you(self):
        self.assertEqual(english_to_french('How are you?'), 'Comment es-tu?')


class TestFrenchToEnglish(TestCase):
    def test_null(self):
        self.assertEqual(french_to_english(None), None)

    def test_empty(self):
        self.assertEqual(french_to_english(''), '')

    def test_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_how_are_you(self):
        self.assertEqual(french_to_english('Comment es-tu?'), 'How are you?')


if __name__ == '__main__':
    main()
