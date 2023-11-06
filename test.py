import requests

age_point = "https://api.agify.io"
gender_point = "https://api.genderize.io"

name = 'Aymir'

params = {
    'name': name
}

age_data = requests.get(age_point, params=params)
gender_data = requests.get(gender_point,params=params)

print(age_data.json())
print(gender_data.json())
