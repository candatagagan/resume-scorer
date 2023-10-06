from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np
from numpy.linalg import norm
import pandas as pd

class Sentence_Similarity:

    def __init__(self):
        pass

    def cosine_similarity(self, input_sentences, calculate_sentence) -> int:
        cosine = np.dot(input_sentences,calculate_sentence.T)/(norm(input_sentences)*norm(calculate_sentence))
        return float(cosine[0])

    def calculate_embedding(self, sentences: list, model_name: str) -> list:
        model = SentenceTransformer(model_name)
        return model.encode(sentences)

class Skill_Similarity:

    def __init__(self, path, skill_column):
        self.path = path
        self.skill_column = skill_column

    def get_skills_data(self) -> list:
        skill_data = pd.read_csv(self.path)
        skill_list = list(skill_data[self.skill_column])
        print(skill_list)
        return skill_list

    def similarity_scores(self, input_sentence: str, skills: list) -> dict:
        classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
        sequence_to_classify = "one day I will see the world"
        candidate_labels = get_skills_data()
        result = classifier(sequence_to_classify, candidate_labels, multi_label=True)
        print(result)


class Scoring_Experience:

    def __init__(self, results_dict, threshold):
        self.results_dict = results_dict
        self.threshold = threshold


    def filter_dict(self):
        for scores in self.results_dict.values():
            new_dict = {key:value for key, value in scores.items() if value > self.threshold}
            return new_dict

class Scoring_Skills:
    def __init__(self):
        pass

    def filter_dict(self):
        skill_data = pd.read_csv(skill_csv)
        skills_list = list(skill_data['text'])
        
            


