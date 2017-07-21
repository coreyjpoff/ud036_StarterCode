import media
import fresh_tomatoes


"""The main main method that runs the favorite movies site

Creates 6 Movie instances and puts them in a list called movies.
Opens my favorites site using fresh_tomatoes.open_movies_page(movies).
"""

toy_story = media.Movie(
    "Toy Story", "Toys talk",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar", "A marine ruins a planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

dumb_and_dumber = media.Movie(
    "Dumb and Dumber", "Slapstick comedy",
    "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
    "https://www.youtube.com/watch?v=l13yPhimE3o")

juice = media.Movie(
    "Juice", "You got the juice now, man",
    "https://upload.wikimedia.org/wikipedia/en/c/ca/Juice_Poster.jpg",
    "https://www.youtube.com/watch?v=QsWto8p7t1E")

la_la_land = media.Movie(
    "La La Land", "Hot white people dance to jazz",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8")

the_big_sick = media.Movie(
    "The Big Sick", "Someone goes into a coma.",
    "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg?download",
    "https://www.youtube.com/watch?v=jcD0Daqc3Yw")

movies = [
    toy_story, avatar, dumb_and_dumber, juice, la_la_land, the_big_sick
]

if __name__ == '__main__':
    fresh_tomatoes.open_movies_page(movies)
