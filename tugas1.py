import requests
import csv

response = requests.get('https://dummyjson.com/users')

data = response.json()

cleaned_data = []

for user in data ['users']:
    cleaned_data.append([user['firstName'], user['lastName'], user['age'], user['gender']])

with open ('tugasPython1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['First Name', 'Last Name', 'Age', 'Gender'])
    writer.writerows(cleaned_data)