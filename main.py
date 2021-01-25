from peabody.models import Doc2VecRecommender, TfidfRecommender

file = "/Users/joshuabailey/PycharmProjects/bookrecommender/misc/data/all_book_summaries.csv"
model = Doc2VecRecommender()
model.load_df(file)
#model.load_model("doc2vecModel")
model.similarity_matrix()
recommendations = model.get_recommendations("The Hunt for Red October", results = 20)
print(recommendations)
