class Song:

    def __init__(self, title, artist, album,
                 rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.total_ratings = 1
        self.length = length
        self.bitrate = bitrate

    def get_rating(self):
        return self.rating

    def rate(self, rating):
        self.rating = (self.rating * self.total_ratings + rating) / \
            (self.total_ratings + 1)
        self.total_ratings += 1
