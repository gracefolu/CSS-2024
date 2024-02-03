import pandas as pd 

movie_data = pd.read_csv("movie_dataset.csv")



print(movie_data)
"""
print(movie_data.info())

print(movie_data.describe())

pd.set_option('display.max_rows',None)

print(movie_data)

# highest_rated = movie_data['Rating'].max()
lowest_rated = movie_data['Rating'].min()


highest_rated = movie_data['Rating'].max()

print(highest_rated)
"""

highest_rated_row = movie_data.loc[movie_data['Rating'].idxmax()]
name_highest_rated = highest_rated_row['Title']

print(name_highest_rated)



# Find the movie with the longest runtime
longest_runtime_movie = movie_data.loc[movie_data['Runtime (Minutes)'].idxmax()]

print(longest_runtime_movie)




