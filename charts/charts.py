import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from collections import Counter

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

# Plot 1: Number of Films Produced per Year (Smoothed with 5-year Rolling Average)
st.title("Number of Films Produced per Year (Smoothed with 5-year Rolling Average)")

# Group by release year and count the number of films per year
films_per_year = unique_movies.groupby('release_year').size()

# Apply rolling average with a window of 5 years for smoothing
rolling_films_per_year = films_per_year.rolling(window=5).mean()

# Plot the smoothed line plot
st.subheader("Films Produced per Year (5-Year Rolling Average)")
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(films_per_year.index, rolling_films_per_year.values, marker='s', linestyle='-', color='g')
ax1.set_title('Number of Films Produced per Year (Smoothed with 5-year Rolling Average)')
ax1.set_xlabel('Release Year')
ax1.set_ylabel('Number of Films')
ax1.grid(True)

# Display the plot using Streamlit
st.pyplot(fig1)

# Plot 2: Top 10 Actors by Film Count (Excluding Unknown)
st.title('Top 10 Actors by Film Count (Excluding Unknown)')

# Filter out "Unknown" actors
actor_count_filtered = actor_count[actor_count['main_actor'] != 'Unknown']

# Sort the filtered DataFrame by film_count and select the top 10 actors
top_actors = actor_count_filtered.sort_values(by='film_count', ascending=False).head(10)

# Display the filtered DataFrame in Streamlit
st.subheader('Top 10 Actors by Film Count:')
st.dataframe(top_actors)

# Create a line plot for actor count vs film count
fig2, ax2 = plt.subplots(figsize=(14, 6))
sns.lineplot(x='main_actor', y='film_count', data=top_actors, marker='o', ax=ax2)
ax2.set_title('Top 10 Actors by Film Count (Excluding Unknown)', fontsize=16)
ax2.set_xlabel('Main Actor', fontsize=14)
ax2.set_ylabel('Film Count', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(fig2)

# Plot 3: Average Ratings Over Time
st.title('Average Ratings Over Time')

# Merge average_ratings with unique_movies
avg_ratings_over_time = pd.merge(average_ratings, unique_movies[['id', 'release_year']], left_on='movie_id', right_on='id')

# Group by release_year and calculate mean rating
avg_rating_by_year = avg_ratings_over_time.groupby('release_year')['user_rating'].mean().reset_index()

# Plot
fig3, ax3 = plt.subplots(figsize=(12, 6))
ax3.plot(avg_rating_by_year['release_year'], avg_rating_by_year['user_rating'], marker='o')
ax3.set_title('Average Ratings Over Time')
ax3.set_xlabel('Release Year')
ax3.set_ylabel('Average User Rating')
plt.xticks(rotation=45)
plt.grid()
st.pyplot(fig3)

# Plot 4: Top 5 Movie Genres by Count
st.title('Top 5 Movie Genres')

# Exploding the genres into separate rows
unique_movies['genre_names'] = unique_movies['genre_names'].apply(eval)  
unique_movies_exploded = unique_movies.explode('genre_names')

# Counting the occurrences of each genre
genre_counts = unique_movies_exploded['genre_names'].value_counts().reset_index()
genre_counts.columns = ['genre_name', 'movie_count']

# Selecting the top 5 genres with the highest movie count
top_5_genres = genre_counts.nlargest(5, 'movie_count')

# Displaying the top 5 genres
st.subheader('Top 5 Genres with Highest Movie Count')
st.dataframe(top_5_genres)

# Plotting the top 5 genres as a horizontal bar plot
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_5_genres, y='genre_name', x='movie_count', hue='genre_name', palette='mako', ax=ax4)
ax4.set_title('Top 5 Genres with Highest Movie Count')
plt.tight_layout()
st.pyplot(fig4)

# Plot 5: Top 5 Movies by Budget and User Rating
st.title('Top 5 Movies by Budget and User Rating')

# Get the top 5 movies with the highest budget
top_5_budget = unique_movies.nlargest(5, 'budget')

# Plotting the budget and user rating for the top 5 movies as a horizontal bar chart
fig5, ax5 = plt.subplots(figsize=(12, 6))
ax5.barh(top_5_budget['original_title'], top_5_budget['budget'], color='#AEEEEE', label='Budget')  # Light Cyan
ax5.barh(top_5_budget['original_title'], top_5_budget['user_rating'] * 10000000, color='#FFB6C1', label='User Rating', alpha=0.6)  # Light Pink
ax5.set_title('Top 5 Movies by Budget and User Rating', fontsize=12)
ax5.set_xlabel('Value', fontsize=10)
ax5.set_ylabel('Original Title', fontsize=10)
ax5.grid(axis='x')
ax5.legend()
plt.tight_layout()
st.pyplot(fig5)

# Plot 6: Top 5 Movies by Popularity
st.title('Top 5 Movies by Popularity')

# Sort the movies by popularity and select the top 5
top_5_movies = unique_movies.sort_values(by='popularity', ascending=False).head(5)

# Plotting the top 5 movies as a horizontal bar chart
fig6, ax6 = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_5_movies['popularity'], y=top_5_movies['original_title'], ax=ax6, palette='Blues_r')
ax6.set_title('Top 5 Movies by Popularity', fontsize=16, pad=20)
ax6.set_xlabel('Popularity', fontsize=14)
ax6.set_ylabel('Original Title', fontsize=14)
plt.tight_layout()
st.pyplot(fig6)

# Plot 7: Top 10 Original Titles by Count (Pie Chart)
st.title("Top 10 Original Titles by Count")

# Pie Chart: Distribution of Original Titles
fig7, ax7 = plt.subplots(figsize=(10, 8))
top_titles = unique_movies['original_title'].value_counts()[:10]  # Get top 10 original titles
ax7.pie(top_titles, labels=top_titles.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
ax7.set_title('Top 10 Original Titles by Count')
st.pyplot(fig7)

# Plot 8: Top 5 Original Languages by Count (Pie Chart)
st.title("Distribution of Top 5 Original Languages")

# Pie Chart: Distribution of Top 5 Original Languages
fig8, ax8 = plt.subplots(figsize=(10, 8))
language_counts = unique_movies['original_language'].value_counts()[:5]  # Get top 5 original languages
ax8.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
ax8.set_title('Top 5 Original Languages by Count')
st.pyplot(fig8)

# Plot 9: Top 5 Production Countries by Film Count (Pie Chart)
st.title("Distribution of Top 5 Production Countries")

# Count occurrences of production countries
production_countries = unique_movies['production_countries'].apply(eval).explode()

# Count the number of films per country
country_counts = Counter(production_countries)

# Create a DataFrame from the counts and sort by 'film_count' to get the top 5
production_countries_df = pd.DataFrame(country_counts.items(), columns=['production_countries', 'film_count'])
top_5_countries_df = production_countries_df.nlargest(5, 'film_count')

# Pie Chart: Top 5 Production Countries Distribution
fig9, ax9 = plt.subplots(figsize=(8
