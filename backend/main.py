from utilities.resume_ai import Sentence_Similarity, Scoring_Experience, Skill_Similarity, Scoring_Skills
from utilities.score_calculator import Score_Calculator
import json
from fastapi import FastAPI, Depends
import requests
from datetime import datetime


"""
data = {
    "name": "John Doe",
    "input_sentences": ["I am a skilled data engineering professional", "I am also skilled in data science"], 
    "compare_sentences":  ["I am skilled in data science", "I am skilled in data engineering", "I am skilled in data"],
    "jd_skills": ["Data Engineering", "Data Science", "Database Management"],
    "talent_skills": ["mechanic", "database administrator", "science"]
}
"""

app = FastAPI()

variables_file = open('utilities/variables.json')

variables = json.load(variables_file)

sen = Sentence_Similarity()

skill = Skill_Similarity(variables['skills_data'], variables["skill_column"])

sc = Score_Calculator()

port = "https://8000-candatagaga-resumescore-yaougqcaufh.ws-us105.gitpod.io"

def score_calculator(input_sentence, compare_sentences, model) -> dict:
    input_embeddings = sen.calculate_embedding([input_sentence], model)
    output_embeddings = [sen.calculate_embedding([i], model) for i in compare_sentences]
    output_embeddings_dict = dict(zip(compare_sentences, output_embeddings))
    score = [sen.cosine_similarity(input_embeddings, i) for i in output_embeddings_dict.values()]
    score_dict = dict(zip(compare_sentences, score))
    return {input_sentence: score_dict}  

@app.post('/input_sentences')
async def receive_sentences(data: dict):
    global received_data
    received_data = data
    return received_data



@app.get('/results_experience')
async def send_result_exp():
    main_dict = {}
    data = received_data
    for input_sentence in data["input_sentences"]:
        calculated_scores = score_calculator(
                        input_sentence=input_sentence,
                        compare_sentences=data["compare_sentences"], 
                        model=variables["model_sentence_similarity"]
                        )


        scores = Scoring_Experience(results_dict=calculated_scores, 
                                    threshold=variables["threshold_sentence_similarity"])

        main_dict[input_sentence] = scores.filter_dict()
    return main_dict

@app.get('/results_skills')
async def send_results_skill():
    data = received_data
    main_dict_skills = {}
    main_dict = skill.similarity_scores(data["jd_skills"], data["talent_skills"], 
                            model=variables["model_zero_shot"])

    for i in main_dict:
        semi_dict_key = i["sequence"]
        semi_dict_key_semi = i["labels"]
        semi_dict_value = i["scores"]

        semi_dict_values = dict(zip(semi_dict_key_semi, semi_dict_value))
        scores = Scoring_Skills(scores=semi_dict_values, threshold=variables["threshold_zero_shot"])
        main_dict_skills[semi_dict_key] = scores.filter_dict()


    return main_dict_skills

@app.get('/jd_experience')
async def jd_experience(experience_dict: dict=Depends(send_result_exp)):
    jd_experience = sc.jd_wise_score(experience_dict)
    return jd_experience

@app.get('/jd_skills')
async def jd_skills(skill_dict: dict=Depends(send_results_skill)):
    jd_skill = sc.jd_wise_score(skill_dict)
    return jd_skill


@app.get('/processed_profile_data')
async def complete_processed(
                experience_dict: dict=Depends(send_result_exp),
                skill_dict: dict=Depends(send_results_skill),
                jd_experience: dict=Depends(jd_experience),
                jd_skill: dict=Depends(jd_skills)
                ):
    data = received_data
    overall = sc.overall_score(jd_experience, jd_skill)

    overall_dict = {
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

    return overall_dict
