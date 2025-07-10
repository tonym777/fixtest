###################################################################
# Generic vector db interface
###################################################################


class VectorStore:

    def build_store_from_data(self, sentences):
        pass

    def add_vector(self, vector_id, vector):
        pass

    def get_vector(self, vector_id):
        pass

    def update_index(self, vector_id, vector):
        pass

    def query_store(self, query, num_results):
        pass

