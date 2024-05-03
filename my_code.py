import tkinter as tk 
from tkinter import messagebox
import random


def load_movies(action):
  try:
    with open (f"{action}.txt, "r") as file: 
               moives = file.readlines()
    movies = [movie.strop() for movie in movies]
    return movies 
  except FileNotFoundError:
    return []

def load_movies(romance):
  try:
    with open (f"{romance}.txt, "r") as file: 
               moives = file.readlines()
    movies = [movie.strop() for movie in movies]
    return movies 
  except FileNotFoundError:
    return []
def load_movies(horror):
  try:
    with open (f"{horror}.txt, "r") as file: 
               moives = file.readlines()
    movies = [movie.strop() for movie in movies]
    return movies 
  except FileNotFoundError:
    return []
def load_movies(comedy):
  try:
    with open (f"{comedy}.txt, "r") as file: 
               moives = file.readlines()
    movies = [movie.strop() for movie in movies]
    return movies 
  except FileNotFoundError:
    return []

#This is going to be where I put the personality test questions, but for now Im just going to keep it as 1 question
movie_recommendations = {
  "action": ["Die Hard", "Avengers", "John Wick"]
  "comedy": ["The Hangover", "Ferris Bueller's Day Off"]
  "romance": ["The Notebook", "Pretty Woman"]
# There will be a file associated with each of the genres that contains a large list of movies and answers to questions
}

#Function to recommend movies based on the answer, for now just off of "what is ur fav movie"
def recommend_movies(favorite_movie):
  #This is a placeholder for now. The real recomendation logic I'll add based on how i decide to do the personality test
  #for now it will just pick one from the same genre, for now just the list, later the file
  movies = load_movies(fav_genre):
    if movies:
      return random.choice(movies)
    else:
      return ["Try another movie] #This is also a place holder, Im having the personality test as mutiple choice
        #So something similar will be displayed when something other than an option is input
#This is going to be in charg of the Reccomend button
def recomment_movie(fav_genre):
  if fav_genre in movie_recommendations:
    return random.choice(movie_recommendations[fav_genre]
  
def on_recommend():
  favorite_movie = movie_entry.get()
  favorite_actor = entry_actor.get()
  fav_genre = genre_var.get()
  recommendations = recommend_movies(favorite_movie)
  messagebox.showinfo("Recommendations", "/n".join(recommendations))

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

tk.Label(root, text= "what if your favorite type of movie?")
genre_var = tk.StringVar()
genre_var.set("Select a genre")
genres = [ #Instert genres here]
genre_menu = tk.OptionMenu(root, genre_var, *genres)
genre_menu.pack()

#Button 
recommend_btn = tk.Button(root, text="Recommend!", command=on_recommend)
recommend_btn.pack() #Pack just for now

root.mainloop()
