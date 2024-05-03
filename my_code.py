import tkinter as tk 
from tkinter import messagebox
import random


def load_movies(genre):
  try:
    with open (f"{genre}.txt, "r") as file: 
               moives = file.readlines()
    movies = [movie.strop() for movie in movies]
    return movies 
  except FileNotFoundError:
    return []
def load_movie_rec(genre_red):
  try:
    with open (f"{genre_rec}_rec.txt, "r") as file:
               movies = [line.strip() for line in file.readlines()]
    return movies
  except FileNotFoundError:
    return[]
def load_actors(genre_actor):
  try:
    with open(f"{genre_actor}_actor.txt, "r") as file:
              actors = [line.strip() for line in file.readlines()]
    return actors
  except FileNotFoundError:
    return []


#Function to recommend movies based on the answer, for now just off of "what is ur fav movie"
def recommend_movies(favorite_movie):
  movies = load_movies(genre_rec):
    if movies:
      return random.choice(movies)
    else:
      return ["Try another movie or try typing it more simple. Ex. The Avengers (instead of specific avengers move)"] #This is also a place holder, Im having the personality test as mutiple choice
        #So something similar will be displayed when something other than an option is input
  
def on_recommend():
  favorite_actor = actor_entry.get()
  favorite_movie = movie_entry.get()
  fav_genre = genre_var.get()

  genre_from_actor = None
  actor_found = False
  genres =['action', 'comedy', 'romance', 'horror']

for genre in genres:
  actors = load_movies(genre_actor)
  if favorite_actor in actors:
    genre_from_actor = genre
    actor_found = True 
    break

if not actor_found:
  genre_from_actor = fav_genre

if favorite_movie: 
  recommendation = recommend_movie(genre_from_actor)
else:
  recommendation = recommend_movie(fav_genre)

messagebox.showinfo("Recommendations", recommendation)

#Tkinter 
root = tk.Tk()
root.title("Movie Recomender")
#entry to input answers to questions
tk.Label(root, text="What is your favorite movie:").pack()
movie_entry = tk.Entry(root)
movie_entry.pack()
#I think i want to change this to grid later

tk.Label(root, text= "What genre of movies do you typically like?")
entry_actor = tk.Entry(root)
antry_actor.pack()

tk.Label(root, text= "what if your favorite genre of movie?")
genre_var = tk.StringVar()
genre_var.set("Select a genre")
genres = ['action', 'comedy', 'romance', 'horror']
genre_menu = tk.OptionMenu(root, genre_var, *genres)
genre_menu.pack()

#Button 
recommend_btn = tk.Button(root, text="Recommend!", command=on_recommend)
recommend_btn.pack() #Pack just for now

root.mainloop()
