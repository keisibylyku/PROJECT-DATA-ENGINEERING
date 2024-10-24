import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Load the gold layer data files
gold_movies_path = r'C:\Users\user\Desktop\GOLD_MOVIES'  # Updated path

# Introductory text
st.title("Movie Dataset Visualization App")
st.write("This app shows various charts using the gold layer of the movie dataset.")

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

# Streamlit app layout for top genres
st.title('Top 5 Genres with Highest Movie Count')
st.write("This bar chart shows the top 5 genres with the highest movie count.")

# Plotting the top 5 genres as a horizontal bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=top_5_genres, y='genre_name', x='movie_count', hue='genre_name', palette='mako', legend=False)
plt.title('Top 5 Genres with Highest Movie Count')
plt.ylabel('Genre Name')
plt.xlabel('Movie Count')
plt.tight_layout()

# Display the plot in the Streamlit app
st.pyplot(plt)

# Sort the movies by popularity and select the top 5
top_5_movies = unique_movies.sort_values(by='popularity', ascending=False).head(5)

# Set the Seaborn style
sns.set(style='whitegrid')

# Streamlit app layout for top movies by popularity
st.title('Top 5 Movies by Popularity')
st.write("This bar chart displays the top 5 movies based on popularity.")

# Create a figure and axes for the popularity plot
plt.figure(figsize=(12, 6))
bars = plt.barh(top_5_movies['original_title'], top_5_movies['popularity'], color=sns.light_palette("skyblue", reverse=True, as_cmap=False))

plt.title('Top 5 Movies by Popularity', fontsize=16, pad=20)
plt.xlabel('Popularity', fontsize=14)
plt.ylabel('Original Title', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()  

# Display the popularity plot in the Streamlit app
st.pyplot(plt)

# Get the top 5 movies with the highest budget
top_5_budget = unique_movies.nlargest(5, 'budget')

# Streamlit app layout for budget and user rating
st.title('Top 5 Movies by Budget and User Rating')
st.write("This bar chart compares the budget and user rating for the top 5 movies.")

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

# Display the budget and user rating plot in the Streamlit app
st.pyplot(plt)

# Line Plot: Number of Films Produced per Year
st.title('Line Plot: Number of Films Produced per Year')
st.write("This line plot shows the number of films produced each year, smoothed with a 5-year rolling average.")

# Group by release year and count the number of films per year
films_per_year = unique_movies.groupby('release_year').size()

# Apply rolling average with a window of 5 years for smoothing
rolling_films_per_year = films_per_year.rolling(window=5).mean()

# Plot the smoothed line plot
plt.figure(figsize=(12, 6))
plt.plot(films_per_year.index, rolling_films_per_year.values, marker='s', linestyle='-', color='g')
plt.title('Number of Films Produced per Year (Smoothed with 5-year Rolling Average)')
plt.xlabel('Release Year')
plt.ylabel('Number of Films')
plt.grid(True)

# Display the films per year plot in the Streamlit app
st.pyplot(plt)

# Line Plot: Top 10 Actors by Film Count
st.title('Line Plot: Top 10 Actors by Film Count')
st.write("This line plot shows the top 10 actors by film count, excluding unknown actors.")

# Load the datasets
actor_count = pd.read_csv(f'{gold_movies_path}\\actor_count.csv')

# Filter out "Unknown" actors
actor_count_filtered = actor_count[actor_count['main_actor'] != 'Unknown']

# Sort the filtered DataFrame by film_count and select the top 10 actors
top_actors = actor_count_filtered.sort_values(by='film_count', ascending=False).head(10)

# Create a line plot for actor count vs film count
plt.figure(figsize=(14, 6))
sns.lineplot(x='main_actor', y='film_count', data=top_actors, marker='o')
plt.title('Top 10 Actors by Film Count (Excluding Unknown)', fontsize=16)
plt.xlabel('Main Actor', fontsize=14)
plt.ylabel('Film Count', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Display the actor count plot in the Streamlit app
st.pyplot(plt)

# Line Plot: Average Ratings Over Time
st.title('Line Plot: Average Ratings Over Time')
st.write("This line plot shows the average user ratings over time.")

# Load average ratings dataset
average_ratings = pd.read_csv(f'{gold_movies_path}\\average_ratings.csv')

# Merge average_ratings with unique_movies
avg_ratings_over_time = pd.merge(average_ratings, unique_movies[['id', 'release_year']], left_on='movie_id', right_on='id')

# Group by release_year and calculate mean rating
avg_rating_by_year = avg_ratings_over_time.groupby('release_year')['user_rating'].mean().reset_index()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(avg_rating_by_year['release_year'], avg_rating_by_year['user_rating'], marker='o')
plt.title('Average Ratings Over Time')
plt.xlabel('Release Year')
plt.ylabel('Average User Rating')
plt.xticks(rotation=45)
plt.grid()

# Display the average ratings plot in the Streamlit app
st.pyplot(plt)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from collections import Counter

# Set the style for seaborn
sns.set(style='whitegrid')

# Load the gold layer data files
gold_movies_path = r'C:\Users\user\Desktop\GOLD_MOVIES'

# Load the Unique Movies data
unique_movies = pd.read_csv(f'{gold_movies_path}\\unique_movies.csv')

# Title for the Streamlit app
st.title("Movie Data Visualizations")

# Pie Chart 1: Distribution of Original Titles
st.subheader('Top 10 Original Titles by Count')
top_titles = unique_movies['original_title'].value_counts()[:10]  # Get top 10 original titles
fig1, ax1 = plt.subplots()
ax1.pie(top_titles, labels=top_titles.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
ax1.set_title('Top 10 Original Titles by Count')
st.pyplot(fig1)

# Pie Chart: Distribution of Top 5 Original Languages
st.subheader('Top 5 Original Languages by Count')
language_counts = unique_movies['original_language'].value_counts()[:5]  # Get top 5 original languages
fig2, ax2 = plt.subplots()
ax2.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
ax2.set_title('Top 5 Original Languages by Count')
st.pyplot(fig2)

# Pie Chart: Top 5 Production Countries Distribution
st.subheader('Top 5 Production Countries Distribution')
# Count occurrences of production countries
production_countries = unique_movies['production_countries'].apply(eval).explode()
country_counts = Counter(production_countries)

# Create a DataFrame from the counts and sort by 'film_count' to get the top 5
production_countries_df = pd.DataFrame(country_counts.items(), columns=['production_countries', 'film_count'])
top_5_countries_df = production_countries_df.nlargest(5, 'film_count')

fig3, ax3 = plt.subplots()
ax3.pie(top_5_countries_df['film_count'], labels=top_5_countries_df['production_countries'], 
         autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax3.set_title('Top 5 Production Countries Distribution')
st.pyplot(fig3)

# Other Chart Types

# Histogram: Show the distribution of average user ratings across all movies
average_ratings = pd.read_csv(f'{gold_movies_path}\\average_ratings.csv')  # Load average ratings data
st.subheader('Distribution of Average User Ratings')
fig4, ax4 = plt.subplots()
ax4.hist(average_ratings['user_rating'], bins=20, color='lightblue', edgecolor='black')
ax4.set_title('Distribution of Average User Ratings')
ax4.set_xlabel('User Rating')
ax4.set_ylabel('Frequency')
ax4.grid(axis='y')
st.pyplot(fig4)

# Correlation Matrix Heatmap
st.subheader('Correlation Matrix Heatmap')
correlation_data = unique_movies[['budget', 'popularity', 'vote_average', 'user_rating']]
correlation_matrix = correlation_data.corr()

fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True, ax=ax5)
plt.title('Correlation Matrix Heatmap', fontsize=16)
st.pyplot(fig5)

# Box Plot: Distribution of Movie Ratings by Release Year (2011-2020)
st.subheader('Distribution of Movie Ratings by Release Year (2011-2020)')
unique_movies_filtered = unique_movies.dropna(subset=['release_year', 'vote_average'])
unique_movies_filtered = unique_movies_filtered[(unique_movies_filtered['release_year'] >= 2011) &
                                                (unique_movies_filtered['release_year'] <= 2020)]

fig6, ax6 = plt.subplots(figsize=(12, 6))
sns.boxplot(x='release_year', y='vote_average', data=unique_movies_filtered, palette="Set2", ax=ax6)
ax6.set_title('Distribution of Movie Ratings by Release Year (2011-2020)', fontsize=16)
ax6.set_xlabel('Release Year', fontsize=14)
ax6.set_ylabel('Average Vote', fontsize=14)
plt.xticks(rotation=45)
st.pyplot(fig6)




