#Nathanael Gonzalez
#CS-487
#January 29th, 2025

"""
This program is to parse through the penguins dataset and perform some basic data analysis tasks using Pandas library
The generative AI used on this task was Chatgpt used to help me download pandas and get it running as well as figure out how to find the penguins.csv file since I thought that would be interesting to learn
Copilot was also used to help me with the syntax of the code and to help me understand how to use the pandas library to perform the tasks. For example, I had a table of all of pandas functions and I asked copilot
what they meant and did Copilot also helped me saving me time by understanding what I was going to write so I could just press tab and it would input the code that I wanted.
"""


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Get the current directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

#Create the path to the csv file located in the same folder as the script
csv_file_path = os.path.join(script_dir, 'penguins.csv')

#Task 1
#Read the dataset using Pandas and remove rows with missing values
penguins_df = pd.read_csv(csv_file_path).dropna()

#Task 2
#Caclculate and print the number of rows and columns
num_rows, num_columns = penguins_df.shape
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")

#Task 3
#Get all the values of the species column and print the distince values
species = penguins_df['species']
distinct_species = species.unique()

#Print the distinct species values
print("Distinct Species Values:")
print(distinct_species)

#Task 4
#Calculate and print the frequency of instances in every penguin species
species_counts = penguins_df['species'].value_counts()
print("\nFrequency of each species:")
print(species_counts)

#Task 5
#Group the data by species and calculate the mean of the numerical columns
species_means = penguins_df.groupby('species').mean(numeric_only= True)
print("\nMean values for numeric columns grouped by species:")
print(species_means)

#Task 6
#Calculate the amount of male and female penguins in the dataset
sex_distribution = penguins_df.groupby('species')['sex'].value_counts()
print("\nDistribution of Sex Column by Species:")
print(sex_distribution)

#Task 7
species_sex_means = penguins_df.groupby(['species','sex']).mean(numeric_only= True)

print("\nMean values fro numeric columns grouped by species and sex:\n")
print(species_sex_means)

#Task 8
#Filter data for "Adelie"
adelie_penguins = penguins_df[penguins_df['species'] == 'Adelie']

#Calculate required statistics
adelie_count = adelie_penguins.shape[0]
adelie_avg_bill_length = adelie_penguins['bill_length_mm'].mean()
adelie_max_bill_length = adelie_penguins['bill_length_mm'].max()
adelie_min_flipper_length = adelie_penguins['flipper_length_mm'].min()

#Print the results
print("\nAdelie Species Statistics:")
print(f"Number of Rows: {adelie_count}")
print(f"Average Bill Length (mm): {adelie_avg_bill_length:.2f}")
print(f"Max Bill Depth(mm): {adelie_max_bill_length:.2f}")
print(f"Min flipper length (mm): {adelie_min_flipper_length:.2f}")

#Task 9
#Create a scatter plot of bill length(x) and bill depth(y)
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=penguins_df,
    x='bill_length_mm',
    y='bill_depth_mm',
    hue='species', #Use different colors for each species
    style='species', #Different markers for each species
    palette='deep', #Use deep color palette
    s=100 #Size of points
)

#add labels and title
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.title("Penguin Bill Length vs Bill Depth")

#show legend
plt.legend(title="Species")

#Display the plot
plt.show()