###################################################################
# QueryRetriever vector db retriever to get the most closed results back
###################################################################


import numpy as np

class QueryRetriever:

    @staticmethod
    def get_most_likely_vectors(query_vector, src_vector, num_results=5):
        results = []
        for vector_id, vector in src_vector.items():
            similarity = np.dot(query_vector, vector) / (np.linalg.norm(query_vector) * np.linalg.norm(vector))
            results.append((vector_id, similarity))

        results.sort(key=lambda x: x[1], reverse=True)

        return results[:num_results]

