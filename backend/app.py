import requests
from utilities.mongo_operations import Mongo_Actions 
from utilities.score_calculator import Score_Calculator
import json
import pandas as pd
from datetime import datetime


variables_file = open('backend/utilities/variables.json')

variables = json.load(variables_file)

mongo = Mongo_Actions()

data = {
    "name": "John Doe",
    "input_sentences": ["I am a skilled data engineering professional", "I am also skilled in data science"], 
    "compare_sentences":  ["I am skilled in data science", "I am skilled in data engineering", "I am skilled in data"],
    "jd_skills": ["Data Engineering", "Data Science", "Database Management"],
    "talent_skills": ["mechanic", "database administrator", "science"]
}

port = "https://8000-candatagaga-resumescore-yaougqcaufh.ws-us105.gitpod.io"


requests.post(f"{port}/input_sentences", json=data)
print("DOne")

experience_dict = requests.get(f"{port}/processed_profile_data").json()
print(experience_dict)