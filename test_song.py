import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song(
            "Skinny Love",
            "Birdy",
            "Birdy",
            5,
            190,
            320,
        )

    def test_get_rating(self):
        self.assertEqual(5, self.song.get_rating())

    def test_rate(self):
        self.song.rate(3)
        self.assertEqual(4, self.song.get_rating())
        self.song.rate(1)
        self.assertEqual(3, self.song.get_rating())


if __name__ == '__main__':
    unittest.main()
