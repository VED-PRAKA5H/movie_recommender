import pandas as pd
sim_df = pd.read_csv('../../data/similarity.csv')
pro_df = pd.rad_csv('../../data/processed.csv')
# Assuming new_df and similarity are defined elsewhere in your code
# new_df: DataFrame containing movie data with titles and other attributes
# similarity: A matrix containing similarity scores between movies

def recommend(movie):
    """
    Recommend movies based on the input movie title.

    Parameters:
    movie (str): The title of the movie for which recommendations are to be made.

    This function finds the index of the given movie in the DataFrame,
    retrieves the similarity scores for that movie, and then sorts 
    the other movies based on their similarity scores. 
    It prints the titles of the top 10 recommended movies (excluding the input movie itself).
    """
    
    # Get the index of the input movie from the DataFrame
    movie_index = new_df[new_df.title == movie].index[0]  # Getting index of the movie

    # Retrieve the similarity scores for the input movie
    distances = similarity[movie_index]  # Get similarity scores for the movie

    # Sort the movies based on similarity scores in descending order
    sorted_list = sorted(enumerate(distances), key=lambda item: item[1], reverse=True)

    # Print the titles of the top 10 recommended movies
    print("Recommended movies for '{}':".format(movie))
    for movie in sorted_list[1:11]:  # Skip the first one as it's the input movie itself
        print(new_df['title'][movie[0]])  # Print the title of the recommended movie

