###################################################################
# ISINStore vector db class to store a collection of isin2words mapping and words (dict) into
###################################################################


import re
import numpy as np

from src.ml.query_retriever import QueryRetriever
from src.ml.vector_db import VectorStore


class ISINStore(VectorStore):

    def __init__(self):
        self.isin_data_map = {}
        self.vector_data = {}
        self.vector_index = {}
        self.vocabulary = set()
        self.word_to_index = {}

    def is_isin_format_valid(self, token):
        """Checks if a string conforms to the ISIN format."""
        pattern = r"^[a-z]{2}[a-z0-9]{9}\d$"
        return re.match(pattern, token) is not None

    def build_store_from_data(self, sentences):
        for sentence in sentences:
            tokens = sentence.lower().split()
            self.vocabulary.update(tokens)

        word_to_index = {word: i for i, word in enumerate(self.vocabulary)}

        sentence_vectors = {}
        for sentence in sentences:
            tokens = sentence.lower().split()
            vector = np.zeros(len(self.vocabulary))
            for token in tokens:
                if self.is_isin_format_valid(token):
                    value = self.isin_data_map.get(token)
                    if value is not None:
                        self.isin_data_map[token] = value + " " + sentence
                    else:
                        self.isin_data_map[token] = sentence

                vector[word_to_index[token]] += 1
            sentence_vectors[sentence] = vector

        for sentence, vector in sentence_vectors.items():
            self.add_vector(sentence, vector)


    def add_vector(self, vector_id, vector):
        self.vector_data[vector_id] = vector
        self.update_index(vector_id, vector)


    def get_vector(self, vector_id):
        return self.vector_data.get(vector_id)


    def update_index(self, vector_id, vector):
        for existing_id, existing_vector in self.vector_data.items():
            similarity = np.dot(vector, existing_vector) / (np.linalg.norm(vector) * np.linalg.norm(existing_vector))
            if existing_id not in self.vector_index:
                self.vector_index[existing_id] = {}
            self.vector_index[existing_id][vector_id] = similarity


    def query_language_store(self, query, num_results):
        query_vector = np.zeros(len(self.vocabulary))
        query_tokens = query.lower().split()
        for token in query_tokens:
            if token in self.word_to_index:
                query_vector[self.word_to_index[token]] += 1
        corr_languages = QueryRetriever.get_most_likely_vectors(query_vector, num_results)
        return corr_languages

    def query_isin_store(self, isin, query, num_results):
        pass
