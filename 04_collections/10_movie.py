"""
--------------------------------------------------
MOVIE WATCHLIST PRACTICE
Using List + Tuple + Set
--------------------------------------------------
"""

# List → stores all movies (each movie is a tuple)
movies = []

# Set → stores unique genres
genres = set()

while True:
    name = input("Enter movie name (Q to quit): ")

    if name.upper() == "Q":
        break

    year = int(input("Enter release year: "))
    genre = input("Enter genre: ")

    # Tuple → fixed movie details
    movie_data = (name, year, genre)

    movies.append(movie_data)

    # Add genre to set
    genres.add(genre)


print("\n----------- MOVIE LIST -----------")

# Loop through list of tuples
for m in movies:
    title, year, genre = m   # unpacking
    print(f"{title} ({year}) - {genre}")

print("---------------------------------")


print("\nUnique genres:")

for g in genres:
    print(g)