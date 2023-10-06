from utilities.resume_ai import Sentence_Similarity, Scoring
import json
from fastapi import FastAPI

"""
data = {
    "input_sentences": ["I am a skilled data engineering professional", "I am also skilled in data science"], 
    "compare_sentences":  ["I am skilled in data science", "I am skilled in data engineering", "I am skilled in data"]
}
"""

app = FastAPI()

variables_file = open('utilities/variables.json')

variables = json.load(variables_file)

sen = Sentence_Similarity()



input_sentences = ["I am skilled in data engineering", "I am a data scientist"]

compare_sentences = ["I am skilled in data science", "I am skilled in data engineering", "I am skilled in data"]

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
    return {"message": "Data Received Successfully"}



@app.get('/results')
async def send_result():
    main_dict = {}
    global received_data
    data = received_data
    for input_sentence in data["input_sentences"]:
        calculated_scores = score_calculator(
                        input_sentence=input_sentence,
                        compare_sentences=data["compare_sentences"], 
                        model=variables["model"]
                        )


        scores = Scoring(results_dict=calculated_scores, threshold=variables["threshold"])

        main_dict[input_sentence] = scores.filter_dict()
    return main_dict
