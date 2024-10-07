import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Set Seaborn style
sns.set(style='whitegrid')

# Title for the Streamlit app
st.title("GOLD LAYER REPORTS FOR MOVIES")

# Load the gold layer data files
gold_movies_path = r'C:/Users/Dell E7440/Desktop/GOLD_MOVIES'

# Load the datasets
director_count = pd.read_csv(f'{gold_movies_path}/director_count.csv')
average_ratings = pd.read_csv(f'{gold_movies_path}/average_ratings.csv')
actor_count = pd.read_csv(f'{gold_movies_path}/actor_count.csv')
unique_movies = pd.read_csv(f'{gold_movies_path}/unique_movies.csv')
average_ratings_small = pd.read_csv(f'{gold_movies_path}/average_ratings_small.csv')

# Check the data loaded and display them using Streamlit
st.header("Loaded Data Previews")
st.subheader("Director Count DataFrame:")
st.write(director_count.head())

st.subheader("Average Ratings DataFrame:")
st.write(average_ratings.head())

st.subheader("Actor Count DataFrame:")
st.write(actor_count.head())

st.subheader("Unique Movies DataFrame:")
st.write(unique_movies.head())

st.subheader("Average Ratings Small DataFrame:")
st.write(average_ratings_small.head())




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title for the Streamlit app
st.title("Number of Films Produced per Year (Smoothed with 5-year Rolling Average)")

# Load the unique_movies dataset
unique_movies = pd.read_csv(r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES\unique_movies.csv')

# Group by release year and count the number of films per year
films_per_year = unique_movies.groupby('release_year').size()

# Apply rolling average with a window of 5 years for smoothing
rolling_films_per_year = films_per_year.rolling(window=5).mean()

# Plot the smoothed line plot
st.subheader("Films Produced per Year (5-Year Rolling Average)")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(films_per_year.index, rolling_films_per_year.values, marker='s', linestyle='-', color='g')
ax.set_title('Number of Films Produced per Year (Smoothed with 5-year Rolling Average)')
ax.set_xlabel('Release Year')
ax.set_ylabel('Number of Films')
ax.grid(True)

# Display the plot using Streamlit
st.pyplot(fig)



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Title of the Streamlit app
st.title('Top 10 Actors by Film Count (Excluding Unknown)')

# Load the datasets
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
actor_count = pd.read_csv(f'{gold_movies_path}\\actor_count.csv')

# Filter out "Unknown" actors
actor_count_filtered = actor_count[actor_count['main_actor'] != 'Unknown']

# Sort the filtered DataFrame by film_count and select the top 10 actors
top_actors = actor_count_filtered.sort_values(by='film_count', ascending=False).head(10)

# Display the filtered DataFrame in Streamlit
st.subheader('Top 10 Actors by Film Count:')
st.dataframe(top_actors)

# Create a line plot for actor count vs film count
fig, ax = plt.subplots(figsize=(14, 6))
sns.lineplot(x='main_actor', y='film_count', data=top_actors, marker='o', ax=ax)
ax.set_title('Top 10 Actors by Film Count (Excluding Unknown)', fontsize=16)
ax.set_xlabel('Main Actor', fontsize=14)
ax.set_ylabel('Film Count', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(fig)






import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets (adjust paths as needed)
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
average_ratings = pd.read_csv(f'{gold_movies_path}\\average_ratings.csv')
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Merge average_ratings with unique_movies
avg_ratings_over_time = pd.merge(average_ratings, unique_movies[['id', 'release_year']], left_on='movie_id', right_on='id')

# Group by release_year and calculate mean rating
avg_rating_by_year = avg_ratings_over_time.groupby('release_year')['user_rating'].mean().reset_index()

# Streamlit app title
st.title('Average Ratings Over Time')

# Plot
plt.figure(figsize=(12, 6))
plt.plot(avg_rating_by_year['release_year'], avg_rating_by_year['user_rating'], marker='o')
plt.title('Average Ratings Over Time')
plt.xlabel('Release Year')
plt.ylabel('Average User Rating')
plt.xticks(rotation=45)
plt.grid()

# Displaying the plot in Streamlit
st.pyplot(plt)

# Clear the current figure to avoid any unwanted output
plt.clf()









import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Load the gold layer data files
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'

# Load the Unique Movies dataset
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Exploding the genres into separate rows
unique_movies['genre_names'] = unique_movies['genre_names'].apply(eval)  
unique_movies_exploded = unique_movies.explode('genre_names')

# Counting the occurrences of each genre
genre_counts = unique_movies_exploded['genre_names'].value_counts().reset_index()
genre_counts.columns = ['genre_name', 'movie_count']

# Selecting the top 5 genres with the highest movie count
top_5_genres = genre_counts.nlargest(5, 'movie_count')

# Streamlit app title
st.title('Top 5 Movie Genres')

# Displaying the top 5 genres
st.subheader('Top 5 Genres with Highest Movie Count')
st.dataframe(top_5_genres)

# Plotting the top 5 genres as a horizontal bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=top_5_genres, y='genre_name', x='movie_count', hue='genre_name', palette='mako', legend=False)
plt.title('Top 5 Genres with Highest Movie Count')
plt.ylabel('Genre Name')
plt.xlabel('Movie Count')
plt.tight_layout()

# Displaying the plot in Streamlit
st.pyplot(plt)






import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Unique Movies dataset
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Get the top 5 movies with the highest budget
top_5_budget = unique_movies.nlargest(5, 'budget')

# Streamlit app title
st.title('Top 5 Movies by Budget and User Rating')

# Plotting the budget and user rating for the top 5 movies as a horizontal bar chart
plt.figure(figsize=(12, 6))

# Create two horizontal bars, one for budget and one for user rating
plt.barh(top_5_budget['original_title'], top_5_budget['budget'], color='#AEEEEE', label='Budget')  # Light Cyan
plt.barh(top_5_budget['original_title'], top_5_budget['user_rating'] * 10000000, color='#FFB6C1', label='User Rating', alpha=0.6)  # Light Pink

plt.title('Top 5 Movies by Budget and User Rating', fontsize=12)
plt.xlabel('Value', fontsize=10)
plt.ylabel('Original Title', fontsize=10)
plt.grid(axis='x')
plt.legend()

plt.tight_layout()

# Displaying the plot in Streamlit
st.pyplot(plt)

# Clear the current figure to avoid any unwanted output
plt.clf()













import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Unique Movies dataset
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Sort the movies by popularity and select the top 5
top_5_movies = unique_movies.sort_values(by='popularity', ascending=False).head(5)

# Set the Seaborn style
sns.set(style='whitegrid')

# Streamlit app title
st.title('Top 5 Movies by Popularity')

# Create a figure and axes
plt.figure(figsize=(12, 6))

# Plotting the top 5 movies as a horizontal bar chart with a light palette
plt.barh(top_5_movies['original_title'], top_5_movies['popularity'], color=sns.light_palette("skyblue", reverse=True, as_cmap=False))

plt.title('Top 5 Movies by Popularity', fontsize=16, pad=20)
plt.xlabel('Popularity', fontsize=14)
plt.ylabel('Original Title', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()

# Displaying the plot in Streamlit
st.pyplot(plt)

# Clear the current figure to avoid any unwanted output
plt.clf()




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Title for the Streamlit app
st.title("Top 10 Original Titles by Count")

# Load the gold layer data files
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Set the style for seaborn
sns.set(style='whitegrid')

# Pie Chart: Distribution of Original Titles
st.subheader("Top 10 Original Titles by Count")
fig, ax = plt.subplots(figsize=(10, 8))
top_titles = unique_movies['original_title'].value_counts()[:10]  # Get top 10 original titles
ax.pie(top_titles, labels=top_titles.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
ax.set_title('Top 10 Original Titles by Count')

# Display the pie chart using Streamlit
st.pyplot(fig)





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Title for the Streamlit app
st.title("Distribution of Top 5 Original Languages")

# Load the gold layer data files
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Set the style for seaborn
sns.set(style='whitegrid')

# Pie Chart: Distribution of Top 5 Original Languages
st.subheader("Top 5 Original Languages by Count")
fig, ax = plt.subplots(figsize=(10, 8))
language_counts = unique_movies['original_language'].value_counts()[:5]  # Get top 5 original languages
ax.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
ax.set_title('Top 5 Original Languages by Count')

# Display the pie chart using Streamlit
st.pyplot(fig)







import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Title for the Streamlit app
st.title("Distribution of Top 5 Production Countries")

# Load the Unique Movies data
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Count occurrences of production countries
production_countries = unique_movies['production_countries'].apply(eval).explode()

# Count the number of films per country
country_counts = Counter(production_countries)

# Create a DataFrame from the counts and sort by 'film_count' to get the top 5
production_countries_df = pd.DataFrame(country_counts.items(), columns=['production_countries', 'film_count'])
top_5_countries_df = production_countries_df.nlargest(5, 'film_count')

# Pie Chart: Top 5 Production Countries Distribution
st.subheader("Top 5 Production Countries by Film Count")
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(top_5_countries_df['film_count'], labels=top_5_countries_df['production_countries'], 
       autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax.set_title('Top 5 Production Countries Distribution')

# Display the pie chart using Streamlit
st.pyplot(fig)





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title for the Streamlit app
st.title("Distribution of Average User Ratings")

# Load the Average Ratings data
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
average_ratings = pd.read_csv(f'{gold_movies_path}\\average_ratings.csv')

# Histogram: Distribution of Average User Ratings
st.subheader("Distribution of Average User Ratings")
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(average_ratings['user_rating'], bins=20, color='lightblue', edgecolor='black')
ax.set_title('Distribution of Average User Ratings')
ax.set_xlabel('User Rating')
ax.set_ylabel('Frequency')
ax.grid(axis='y')

# Display the histogram using Streamlit
st.pyplot(fig)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Set the title of the app
st.title('Correlation Matrix Heatmap of Unique Movies Dataset')

# Load the Unique Movies dataset
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Select relevant numerical columns for correlation
correlation_data = unique_movies[['budget', 'popularity', 'vote_average', 'user_rating']]

# Calculate the correlation matrix
correlation_matrix = correlation_data.corr()

# Create heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Matrix Heatmap', fontsize=16)

# Show the plot in Streamlit
st.pyplot(plt)



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import streamlit as st

# Ignore warnings
warnings.filterwarnings('ignore')

# Set up the Streamlit app
st.title("Distribution of Average Votes by Release Year (2011-2020)")

# Load the dataset
gold_movies_path = r'C:\Users\Dell E7440\Desktop\GOLD_MOVIES'
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Filter out movies without a release year or vote average
unique_movies_filtered = unique_movies.dropna(subset=['release_year', 'vote_average'])

# Filter data for the last 10 years (e.g., 2011 to 2020)
unique_movies_filtered = unique_movies_filtered[(unique_movies_filtered['release_year'] >= 2011) &
                                                (unique_movies_filtered['release_year'] <= 2020)]

# Create a box plot for vote_average over release_year (Last ten years)
plt.figure(figsize=(12, 6))
sns.boxplot(x='release_year', y='vote_average', data=unique_movies_filtered, palette="Set2")

# Set titles and labels
plt.title('Distribution of Average Votes by Release Year (2011-2020)', fontsize=16)
plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Average Vote', fontsize=14)  # Updated Y-axis label

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot in Streamlit
st.pyplot(plt)

