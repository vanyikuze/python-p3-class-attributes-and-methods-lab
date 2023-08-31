class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artists, genre):
        self.name = name
        Song.add_to_artists(artists)
        Song.add_to_genres(genre)
        self.add_song_to_count()
        self.add_to_artists_count(artists)
        self.add_to_genre_count(genre)
    
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artists):
        cls.artists.append(artists)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artists):
        if artists in cls.artist_count:
            cls.artist_count[artists] += 1
        else:
            cls.artist_count[artists] = 1