from flask import Flask, render_template, request, g
from flask_sqlalchemy import SQLAlchemy
from peabody.models import TfidfRecommender



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = "BookSummaries.sql"
file = "/Users/joshuabailey/PycharmProjects/bookrecommender/misc/data/all_book_summaries.csv"
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
    number_of_recommendations = int(request.form['recommendations'])
    print(book_name, number_of_recommendations)
    df = model.get_recommendations(book_name, number_of_recommendations)
    return render_template('submit.html',  tables=[df.to_html(classes='data', header="true")] )


git p
if __name__ == '__main__':
    app.run()