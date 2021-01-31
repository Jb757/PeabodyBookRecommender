from peabody.models.recommender import Recommender
from peabody.utils.preprocessing import tokenised_summary

import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


class Doc2VecRecommender(Recommender):
    def similarity_matrix(self):
        self.summary_tokenised = self._create_tokenised_summary()
        self.documents = self._create_documents()
        if self.model == None:
            self.model = Doc2Vec(vector_size=250, window=2, min_count=1, workers=16, epochs=60)
            self.model.build_vocab(self.documents)
            self.model.train(self.documents, total_examples=self.model.corpus_count, epochs=self.model.epochs)
            self.save_model("doc2vecModel")
            self.vecs = self._create_vecs()
            self.cosine_similarity_matrix = self._cosine_similarity_matrix()
            return self.cosine_similarity_matrix
        else:
            self.vecs = self._create_vecs()
            self.cosine_similarity_matrix = self._cosine_similarity_matrix()
            return self.cosine_similarity_matrix

    def _create_tokenised_summary(self):
        summary_tokenised = tokenised_summary(self.df)
        return summary_tokenised

    def _create_documents(self):
        documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(self.summary_tokenised)]
        return documents

    def _create_vecs(self):
        vec = [self.model.docvecs[i].tolist() for i in range(len(self.model.docvecs))]
        vec = np.array(vec)
        return vec

    def load_model(self, path):
        self.model = Doc2Vec.load(path)

    def save_model(self, filename):
        self.model.save(filename)


