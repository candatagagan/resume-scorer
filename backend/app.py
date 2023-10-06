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

port = "https://8000-candatagaga-resumescore-cpa35dk4y0m.ws-us105.gitpod.io"

requests.post(f"{port}/input_sentences", json=data)

experience_dict = requests.get(f"{port}/results_experience").json()

skill_dict = requests.get(f"{port}/results_skills").json()

score_calculator = Score_Calculator()

jd_experience = score_calculator.jd_wise_score(experience_dict)

print(jd_experience)


jd_skill = score_calculator.jd_wise_score(skill_dict)

print(jd_skill)

overall = score_calculator.overall_score(jd_experience, jd_skill)


mongo.insert_json(
    {
        "id": data["name"]+str(datetime.now()),
        "index": 1,
        "score_breakup": {
            "experience": experience_dict,
            "skill": skill_dict
        },
        "jd_scores": {
            "experience": jd_experience,
            "skill": jd_skill
        }, 
        "overall": str(overall),
        "date": datetime.now()
    }
)


print("completed")