import tkinter as tk 
from tkinter import messagebox
import random


def load_movies(genre):
  try:
    with open(f"{genre}.txt", "r") as file: 
               moives = file.readlines()
    movies = [movie.strop() for movie in movies]
    return movies 
  except FileNotFoundError:
    return []
def load_movie_rec(genre_rec):
    try:
        with open(f"{genre}_rec.txt", "r") as file:
            movies = [line.strip() for line in file.readlines()]
        return movies
    except FileNotFoundError:
        return []


#Function to recommend movies based on the answer, for now just off of "what is ur fav movie"
def recommend_movie(genre_rec):
    movies = load_movies(genre_rec)
    if movies:
        return random.choice(movies)
    else:
      return ["Try another movie or try typing it more simple. Ex. The Avengers (instead of specific avengers move)"]

  
def on_recommend():
    favorite_actor = actor_entry.get()
    favorite_movie = movie_entry.get()
    fav_genre = genre_var.get()

    # Find genre from actor
    genre_from_actor = None
    actor_found = False
    genres = ['action', 'comedy', 'romance', 'horror']  # Assuming these are your genres
    for genre in genres:
        actors = load_movies(genre)  # This assumes your genre.txt files contain actors too
        if favorite_actor in actors:
            genre_from_actor = genre
            actor_found = True
            break

    # If actor not found in any genre list
    if not actor_found:
        genre_from_actor = fav_genre

    # Recommend movie from the identified genre or user's favorite genre
    if favorite_movie:
        recommendation = recommend_movie(genre_from_actor)
    else:
        recommendation = recommend_movie(fav_genre)

    messagebox.showinfo("Recommendations", recommendation)


messagebox.showinfo("Recommendations", recommendation)

root = tk.Tk()
root.title("Movie Recommender")
root.geometry("900x500")

nice_font = ("Helvetica", 20)

# Entry for favorite movie
tk.Label(root, text="What is your favorite movie:").pack()
tk.Label(root, text= "(try keeping titles simple Ex. The Avengers instead of the full title)").pack()
movie_entry = tk.Entry(root)
movie_entry.pack()

# Entry for favorite actor
tk.Label(root, text="Who is your favorite actor:").pack()
actor_entry = tk.Entry(root)
actor_entry.pack()

# Dropdown for favorite genre
tk.Label(root, text="What genre of movies do you typically like watching?").pack()
genre_var = tk.StringVar()
genre_var.set("Select a genre")
genres = ['action', 'comedy', 'romance', 'horror']  # Assuming these are your genres
genre_menu = tk.OptionMenu(root, genre_var, *genres)
genre_menu.pack()

# Button for recommendations
recommend_btn = tk.Button(root, text="Recommend!", command=on_recommend,
font= nice_font)
recommend_btn.pack()

root.mainloop()
