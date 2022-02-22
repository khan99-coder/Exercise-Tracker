import requests
from datetime import datetime
import os


today = datetime.now()
formatted_date = today.date().strftime("%d/%m/%Y")
formatted_time = today.time().strftime("%X")

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")


GENDER = "male"
WEIGHT = 77
HEIGHT = 160
AGE = 26

TOKEN = "sgggghgjhklkfhhw"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
exercise_text = input("Tell me what you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
exercise_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
result = exercise_response.json()
print(result)

for exercise in result["exercises"]:
    exercise_name = exercise["user_input"].title()
    exercise_duration = round(exercise["duration_min"])
    calories_burned = round(exercise["nf_calories"])

    sheet_params = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": calories_burned,
        }

    }
    

    bearer_header = {
        "Authorization": "Bearer dsagadshfjdzfrcvghjkvhjrghrweymy"
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_params, headers=bearer_header)
    #print(sheet_response.text)






