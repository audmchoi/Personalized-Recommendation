import tkinter as tk 
from tkinter import messagebox

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
  for gnere, movies in movie_recommendations.items():
    if favorite_movie in movies:
      recommended = [movie for movie in movies if movie != favorite_movie]
      return recommended 
return ["No recommendations found. Try another movie] #This is also a place holder, Im having the personality test as mutiple choice
        #So something similar will be displayed when something other than an option is input
#This is going to be in charg of the Reccomend button
def on_recommend():
  favorite_movie = movie_entry.get()
  recommendations = recommend_movies(favorite_movie)
  messagebox.showinfo("Recommendations", "/n".join(recommendations))

#Tkinter 
root = tk.Tk()
root.title("Movie Recomender")
#entry to input answers to questions
tk.Label(root, text="Enter your favorite movie:").pack()
movie_entry = tk.Entry(root)
movie_entry.pack()
#I think i want to change this to grid later

#Button 
recommend_btn = tk.Button(root, text="Recommend!", command=on_recommend)
recommend_btn.pack() #Pack just for now

root.mainloop()
