# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st  # Only needed if you're using Streamlit


# Display a message in the app
st.write("This app deploys different charts using gold layer files")

# Display a heading for the bar charts
st.write("### Below are various bar charts using data from the gold layer")

# Load the gold layer files
individual_summary = pd.read_csv(r'C:\Users\user\Desktop\GOLDIMDB\cleaned_individual_summary.csv')
title_category_summary = pd.read_csv(r'C:\Users\user\Desktop\GOLDIMDB\gold_title_category_summary.csv')

# Set the plot style
sns.set(style="whitegrid")

# Chart 1: Top 10 Categories by Number of Titles
st.write("#### Top 10 Categories by Number of Titles")
top_10_categories = title_category_summary.nlargest(10, 'number_of_titles')

# Set the figure size for the first chart
plt.figure(figsize=(10, 6))

# Create the first bar plot
sns.barplot(x='category', y='number_of_titles', data=top_10_categories, palette='Blues_d', legend=False)
plt.title('Top 10 Categories by Number of Titles')
plt.xticks(rotation=45)
plt.ylabel('Number of Titles')

# Display the first plot in Streamlit
st.pyplot(plt)

# Chart 2: Top 10 Individuals with Most Titles
st.write("#### Top 10 Individuals with Most Titles")
top_10_individuals = individual_summary.nlargest(10, 'total_titles')

# Set the figure size for the second chart
plt.figure(figsize=(10, 6))

# Create the second bar plot
sns.barplot(data=top_10_individuals, x='primaryName', y='total_titles', palette='Blues_d', legend=False)
plt.title('Top 10 Individuals with Most Titles')
plt.xticks(rotation=45)
plt.ylabel('Number of Titles')
plt.xlabel('Individuals')

# Display the second plot in Streamlit
st.pyplot(plt)

# Chart 3: Top 5 Most Common Professions
st.write("#### Top 5 Most Common Professions")
# Split the primaryProfession into individual professions and count the occurrences
profession_counts = individual_summary['primaryProfession'].str.split(',').explode().value_counts().nlargest(5)

# Set the figure size for the third chart
plt.figure(figsize=(10, 8))

# Create the third bar plot
sns.barplot(x=profession_counts.index, y=profession_counts.values, color='lightblue')
plt.title('Top 5 Most Common Professions')
plt.xticks(rotation=45)
plt.ylabel('Frequency')
plt.xlabel('Profession')

# Display the third plot in Streamlit
st.pyplot(plt)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set plot style for Seaborn
sns.set(style="whitegrid")

# Load the gold layer files
individual_summary = pd.read_csv(r'C:\Users\user\Desktop\GOLDIMDB\cleaned_individual_summary.csv')
title_category_summary = pd.read_csv(r'C:\Users\user\Desktop\GOLDIMDB\gold_title_category_summary.csv')

# Display a message for line plots
st.write("### Below are various line plots using data from the gold layer")

# Line Plot 1: Top 10 Individuals by Number of Titles
st.write("#### Top 10 Individuals by Number of Titles")
top_10_individuals = individual_summary.nlargest(10, 'total_titles')

# Set figure size and create the line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=top_10_individuals, x='primaryName', y='total_titles', marker='o')
plt.title('Top 10 Individuals by Number of Titles')
plt.xticks(rotation=45)
plt.ylabel('Total Titles')

# Display the line plot in Streamlit
st.pyplot(plt)

# Line Plot 2: Number of Titles by Top 10 Categories
st.write("#### Number of Titles by Top 10 Categories")
top_categories = title_category_summary.nlargest(10, 'number_of_titles')

# Set figure size and create the line plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=top_categories, x='category', y='number_of_titles', marker='o', color='lightgreen')
plt.title('Number of Titles by Top 10 Categories')
plt.xticks(rotation=45)
plt.ylabel('Number of Titles')

# Display the line plot in Streamlit
st.pyplot(plt)

# Display a message for pie charts section
st.write("### Below are various pie charts using data from the gold layer")

# Pie Chart 1: Top 5 Categories by Number of Titles
st.write("#### Top 5 Categories by Number of Titles")
top_5_categories = title_category_summary.nlargest(5, 'number_of_titles')

# Set figure size and create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(top_5_categories['number_of_titles'], labels=top_5_categories['category'], autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Categories by Number of Titles')

# Display the pie chart in Streamlit
st.pyplot(plt)

# Pie Chart 2: Distribution of Titles for Archive Categories
st.write("#### Distribution of Titles for Archive Categories")
archive_categories = title_category_summary[title_category_summary['category'].str.contains('archive')]

# Set figure size and create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(archive_categories['number_of_titles'], labels=archive_categories['category'], autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Titles for Archive Categories')

# Display the pie chart in Streamlit
st.pyplot(plt)

# Pie Chart 3: Top 5 Professions by Title Contribution
st.write("#### Top 5 Professions by Title Contribution")

# Generate profession_summary by counting total titles per profession
profession_summary = individual_summary['primaryProfession'].str.split(',').explode().value_counts().reset_index()
profession_summary.columns = ['primaryProfession', 'total_titles']

# Get the top 5 professions
top_5_professions = profession_summary.nlargest(5, 'total_titles')

# Set figure size and create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(top_5_professions['total_titles'], labels=top_5_professions['primaryProfession'], autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Professions by Title Contribution')

# Display the pie chart in Streamlit
st.pyplot(plt)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import streamlit as st

# Display a message for histogram
st.write("### Below is a histogram and a Q-Q plot using data from the gold layer")

# Load the gold layer files
title_category_summary = pd.read_csv(r'C:\Users\user\Desktop\GOLDIMDB\gold_title_category_summary.csv')
cleaned_summary = pd.read_csv(r'C:\Users\user\Desktop\GOLDIMDB\cleaned_individual_summary.csv')

# Histogram: Distribution of Number of Titles by Category
st.write("#### Distribution of Number of Titles by Category (Histogram)")

plt.figure(figsize=(8, 6))
sns.histplot(data=title_category_summary, x='number_of_titles', bins=10, kde=True, color='blue')

# Add titles and labels
plt.title('Distribution of Number of Titles by Category')
plt.xlabel('Number of Titles')
plt.ylabel('Frequency')

# Display the histogram in Streamlit
st.pyplot(plt)

# Q-Q Plot: Total Titles
st.write("#### Q-Q Plot of Total Titles")

# Creating a Q-Q plot for the 'total_titles' column
plt.figure(figsize=(10, 8))
plt.ticklabel_format(style='plain')
stats.probplot(cleaned_summary['total_titles'].dropna(), dist="norm", plot=plt)

# Add titles and labels
plt.title('Q-Q Plot of Total Titles')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.grid(True)

# Display the Q-Q plot in Streamlit
st.pyplot(plt)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Display a message for the count plot
st.write("### Count Plot: Total Number of Titles by Top 5 Primary Professions")

# Load the cleaned individual summary dataset
cleaned_summary = pd.read_csv(r'C:\Users\user\Desktop\GOLDIMDB\cleaned_individual_summary.csv')

# Determine the top 5 categories based on total titles
top_categories = cleaned_summary.groupby('primaryProfession')['total_titles'].sum().nlargest(5).index

# Filter the data for the top categories
top_categories_data = cleaned_summary[cleaned_summary['primaryProfession'].isin(top_categories)]

# Set the style of the visualization
sns.set(style='whitegrid')

# Create a count plot
plt.figure(figsize=(12, 8))
sns.barplot(data=top_categories_data, x='primaryProfession', y='total_titles', palette='Set2')

# Formatting the plot
plt.title('Total Number of Titles by Top 5 Primary Professions')
plt.xlabel('Primary Profession')
plt.ylabel('Total Titles')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Display the count plot in Streamlit
st.pyplot(plt)
