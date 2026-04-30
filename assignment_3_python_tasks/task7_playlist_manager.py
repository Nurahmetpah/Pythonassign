class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_duration(self):
        return sum(song.duration for song in self.songs)

    def longest_song(self):
        if not self.songs:
            return None
        return max(self.songs, key=lambda s: s.duration)

    def show_playlist(self):
        print("Playlist:")
        for song in self.songs:
            print(f"- {song.title} ({song.duration} min)")
        print(f"Total Duration: {self.total_duration()} min")
        longest = self.longest_song()
        if longest:
            print(f"Longest Song: {longest.title} ({longest.duration} min)")

if __name__ == "__main__":
    pl = Playlist()
    pl.add_song(Song("Song A", 3))
    pl.add_song(Song("Song B", 5))
    pl.add_song(Song("Song C", 4))
    pl.show_playlist()
