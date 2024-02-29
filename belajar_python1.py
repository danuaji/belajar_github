import requests
import csv

# Mengirim permintaan untuk mendapatkan data dari URL
response = requests.get('https://dummyjson.com/users')

# Mendapatkan data JSON dari respons
data = response.json()

# Menyiapkan list untuk menyimpan data yang diinginkan
cleaned_data = []

# Iterasi melalui setiap pengguna
for user in data['users']:
    # Mendapatkan informasi yang diinginkan dan menambahkannya ke dalam list
    cleaned_data.append([user['firstName'], user['lastName'], user['age'], user['gender']])

# Menyimpan data ke dalam file CSV
with open('users.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Menulis header
    writer.writerow(['First Name', 'Last Name', 'Age', 'Gender'])
    # Menulis setiap baris data
    writer.writerows(cleaned_data)

print("Data telah disimpan dalam format CSV.")
