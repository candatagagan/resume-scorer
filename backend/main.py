from utilities.resume_ai import Sentence_Similarity
import json
from fastapi import FastAPI

app = FastAPI()

variables_file = open('utilities/variables.json')

variables = json.load(variables_file)

sen = Sentence_Similarity()

input_sentence = "I am skilled in data engineering"

compare_sentences = ["I am skilled in data science", "I am skilled in data engineering", "I am skilled in data"]

def score_calculator(input_sentence, compare_sentences, model) -> dict:
    input_embeddings = sen.calculate_embedding([input_sentence], model)
    output_embeddings = [sen.calculate_embedding([i], model) for i in compare_sentences]
    output_embeddings_dict = dict(zip(compare_sentences, output_embeddings))
    score = [sen.cosine_similarity(input_embeddings, i) for i in output_embeddings_dict.values()]
    score_dict = dict(zip(compare_sentences, score))
    return score_dict  


@app.get('/results')
async def send_result():
    result = score_calculator(
                    input_sentence=input_sentence,
                    compare_sentences=compare_sentences, 
                    model=variables["model"]
                    )
    return result