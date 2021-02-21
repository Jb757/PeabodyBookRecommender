from flask import Flask, render_template, request
from peabody.models.tfidf import TfidfRecommender
import os



app = Flask(__name__)
file = "https://raw.githubusercontent.com/JoshwaBail/PeabodyBookRecommender/master/misc/data/all_book_summaries.csv"
model = TfidfRecommender()
model.load_df(file)
model.load_model("model.pickle")
model.similarity_matrix()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods =['POST'])
def submit():
    
    book_name = request.form['book_name']

    if request.form['recommendations']:
        number_of_recommendations = int(request.form['recommendations'])
    else:
        number_of_recommendations = 10

    if request.form['genre']:
        genre = request.form['genre']
    else:
        genre = "None"
    df = model.get_recommendations(book_name, number_of_recommendations, genre)
    return render_template('submit.html',  tables=[df.to_html(classes='data', header="true")] )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("port", 5000)))
