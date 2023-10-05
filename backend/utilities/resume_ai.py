from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.linalg import norm

class Sentence_Similarity:

    def __init__(self):
        pass

    def cosine_similarity(self, input_sentences, calculate_sentence) -> int:
        cosine = np.dot(input_sentences,calculate_sentence.T)/(norm(input_sentences)*norm(calculate_sentence))
        return float(cosine[0])

    def calculate_embedding(self, sentences: list, model_name: str) -> list:
        model = SentenceTransformer(model_name)
        return model.encode(sentences)