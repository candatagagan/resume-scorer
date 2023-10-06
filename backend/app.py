import requests
from utilities.dynamo_operations import Dynamo_Actions
from utilities.score_calculator import Score_Calculator
import json
import pandas as pd
variables_file = open('backend/utilities/variables.json')

variables = json.load(variables_file)

dynamo = Dynamo_Actions(table_name=variables["dynamo_table_name"])

data = {
    "name": "John Doe",
    "input_sentences": ["I am a skilled data engineering professional", "I am also skilled in data science"], 
    "compare_sentences":  ["I am skilled in data science", "I am skilled in data engineering", "I am skilled in data"],
    "jd_skills": ["Data Engineering", "Data Science", "Database Management"],
    "talent_skills": ["mechanic", "database administrator", "science"]
}

requests.post("https://8000-candatagaga-resumescore-5mpyh2khpcd.ws-us105.gitpod.io/input_sentences", json=data)

experience_scores = requests.get("https://8000-candatagaga-resumescore-5mpyh2khpcd.ws-us105.gitpod.io/results_experience").json()

skill_scores = requests.get("https://8000-candatagaga-resumescore-5mpyh2khpcd.ws-us105.gitpod.io/results_skills").json()

x = Score_Calculator.overall_score(result=experience_scores)

print(pd.DataFrame(experience_scores))
print(skill_scores)