import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
# url="https://www.espncricinfo.com/records/tournament/team-highest-innings-totals/icc-men-s-t20-world-cup-2024-15946"
team_data = {'TEAM':['India','USA','Australia','England','Afganistan','West Indies','South Africa','Bangladesh'],
 'NRR_In_1st_group_stage':[+1.137,+0.127,+2.791,+3.611,+4.230,+2.596,+0.470,+0.616],'NRR_In_2nd_group_stage':[0,0,0,0,0,0,0,0]}
# venue_data={'VENUE':['Dallas','Bridgetown','Providence','New York','Lauderhill','North Sound','Gros Islet','Kingstown','Tarouba'],
# 'average_first_inning_score_before_tournament':[150,156,129,77,147,124,161,143.5]}
csv_file_path = 'example.csv'

# Open the file in write mode
with open(csv_file_path, mode='w', newline='') as file:
	# Create a csv.writer object
	writer = csv.writer(file)
	# Write data to the CSV file
	writer.writerows(data)
file_path = 'WC24_DATA.xlsx'
sheet_name = 'Sheet1'
df1 = pd.read_excel(file_path,sheet_name=sheet_name)
df2 = pd.read_csv('example.csv')
print(df)  # Display the first few rows of the DataFrame
X=[['Team','Overs','Opposition','Ground']]
Y=['Score']
LR=LinearRegression()
RF=RandomForestRegressor()
