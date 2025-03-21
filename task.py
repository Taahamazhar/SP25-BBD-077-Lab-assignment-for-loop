favorite_movies = ["Titanic", "The God Father", "The Dark side"]
for i in favorite_movies:
    print(i)


print("Movie Titles:")
for movie in favorite_movies:
    print(movie)



print("\nMovie Titles with Index:")
for index, movie in enumerate(favorite_movies):
    print(f"{index + 1}: {movie}")




full_name = ("Tuaha Mazhar")


print("\nCharacters in Full Name:")
for char in full_name:
    print(char)



vowels = ("AEIOUaeiou")
vowel_count = sum(1 for char in full_name if char in vowels)
print(f"\nNumber of vowels in '{full_name}': {vowel_count}")
