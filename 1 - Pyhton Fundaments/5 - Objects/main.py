 
class Movie():
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return 'Title: '+ self.title
    def __eq__(self, other_movie):
        return self.title == other_movie.title

movies = []

movies.append(Movie("Jhon Wick"))
movies.append(Movie("Avengers"))
movies.append(Movie("Lord of the ring"))

for movie in movies:
    print(movie)

print(Movie("Ant-Man") in movies)
print(Movie("Jhon Wick") in movies)