from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np
from numpy.linalg import norm
import pandas as pd

class Sentence_Similarity:

    def __init__(self):
        pass

    def cosine_similarity(self, input_sentences, calculate_sentence) -> float:
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
        return skill_list

    def similarity_scores(self, input_skill: list, comparison_skills: list, model) -> dict:
        classifier = pipeline("zero-shot-classification",
                      model=model)
        result = classifier(input_skill, comparison_skills, multi_label=True)
        return result


class Scoring_Experience:

    def __init__(self, results_dict, threshold):
        self.results_dict = results_dict
        self.threshold = threshold


    def filter_dict(self):
        for scores in self.results_dict.values():
            new_dict = {key:value for key, value in scores.items() if value > self.threshold}
            return new_dict

class Scoring_Skills:
    def __init__(self, scores, threshold):
        self.scores = scores
        self.threshold = threshold

    def filter_dict(self):
        new_dict = {key:value for key, value in self.scores.items() if value > self.threshold}
        return new_dict
        
        
            


