from peabody.models.recommender import Recommender

from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


class TfidfRecommender(Recommender):
    def similarity_matrix(self):
        if self.model == None:
            self.vecs = self._create_vecs()
            self.save_model("model.pickle")
            self.cosine_similarity_matrix = self._cosine_similarity_matrix()
            return self.cosine_similarity_matrix
        else:
            self.vecs = self._create_vecs()
            self.cosine_similarity_matrix = self._cosine_similarity_matrix()

    def _create_vecs(self):
        if self.model == None:
            self.model = TfidfVectorizer()
            vecs = self.model.fit_transform(self.df["Soup"])
            return vecs
        else:
            vecs = self.model.fit_transform(self.df["Soup"])
            return vecs

    def load_model(self, path):
        with open(path, 'rb') as f:
            self.model = pickle.load(f)

    def save_model(self, filename):
        pickle.dump(self.model, open(filename, "wb"))