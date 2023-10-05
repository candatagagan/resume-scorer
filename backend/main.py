from utilities.resume_ai import Sentence_Similarity
import json

variables_file = open('/workspace/resume-scorer/backend/utilities/variables.json')

variables = json.load(variables_file)

sen = Sentence_Similarity()

input_sentence = "I am skilled in data engineering"

compare_sentences = ["I am skilled in data science", "I am skilled in data engineering", "I am skilled in data"]


if __name__ == "__main__":
    input_embeddings = sen.calculate_embedding([input_sentence], variables["model"])
    output_embeddings = [sen.calculate_embedding([i], variables["model"]) for i in compare_sentences]
    output_embeddings_dict = dict(zip(compare_sentences, output_embeddings))
    #print(output_embeddings_dict)

    score = [sen.cosine_similarity(input_embeddings, i) for i in output_embeddings_dict.values()]
    score_dict = dict(zip(compare_sentences, score))
    print(score_dict)    