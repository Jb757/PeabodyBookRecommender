from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd


class Recommender:
    def __init__(self):
        self.df = None
        self.model = None
        self.summary_tokenised = None
        self.documents = None
        self.vecs = None
        self.cosine_similarity_matrix = None

    def get_recommendations(self, title: str, results: int):
        indices = pd.Series(self.df.index, index=self.df['Title']).drop_duplicates()
        idx = indices[title]
        if type(idx) != np.int64:
            idx = idx[0]
        sim_scores = list(enumerate(self.cosine_similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:results+1]
        book_indices = [i[0] for i in sim_scores]
        recommendations = self.df.iloc[book_indices, [1, 2, 5]].reset_index(drop=True)
        recommendations.index = np.arange(1, len(recommendations)+1)
        return recommendations

    def _cosine_similarity_matrix(self):
        cosine_sim = cosine_similarity(self.vecs, self.vecs)
        return cosine_sim

    def load_df(self, path):
        self.df = pd.read_csv(path)

    def similarity_matrix(self):
        pass

    def _create_vecs(self):
        pass

    def load_model(self, path):
        pass

    def save_model(self, filename):
        pass

