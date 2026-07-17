# Project 3: Simple Recommendation System
# Decode Labs AI Internship

# Movie dataset
movies = [
    {
        "title": "Inception",
        "genre": "sci-fi",
        "language": "english"
    },
    {
        "title": "Interstellar",
        "genre": "sci-fi",
        "language": "english"
    },
    {
        "title": "The Dark Knight",
        "genre": "action",
        "language": "english"
    },
    {
        "title": "3 Idiots",
        "genre": "comedy",
        "language": "hindi"
    },
    {
        "title": "Dangal",
        "genre": "sports",
        "language": "hindi"
    },
    {
        "title": "Parasite",
        "genre": "thriller",
        "language": "korean"
    }
]

print("=" * 40)
print("     MOVIE RECOMMENDATION SYSTEM")
print("=" * 40)

# Take user preferences
user_genre = input("Enter your preferred genre: ").lower()
user_language = input("Enter your preferred language: ").lower()

# Match movies with user preferences
recommendations = []

for movie in movies:
    if movie["genre"] == user_genre and movie["language"] == user_language:
        recommendations.append(movie["title"])

# Display recommendations
print("\nRecommended Movies:")

if recommendations:
    for movie in recommendations:
        print("-", movie)
else:
    print("Sorry, no exact match found.")
    print("Try another genre or language.")

print("\nThank you for using the Recommendation System!")