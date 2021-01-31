from peabody.models import Doc2VecRecommender, TfidfRecommender

file = "/misc/data/all_book_summaries.csv"
model = TfidfRecommender()
model.load_df(file)
model.load_model("model.pickle")
model.similarity_matrix()
recommendations = model.get_recommendations("The Hunt for Red October", results = 10)
#print(recommendations)
print(recommendations.to_html(classes='data'))