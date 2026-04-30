class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def is_recommended(self):
        return self.rating >= 8

    def display_info(self):
        print(f"Title: {self.title}, Rating: {self.rating}, Recommended: {self.is_recommended()}")

if __name__ == "__main__":
    movie = Movie("Inception", 9.0)
    movie.display_info()
