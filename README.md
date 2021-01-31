# Peabody Book Recommender 
Named Peabody after to the famous and beautiful George Peabody library at The John Hopkins University in Baltimore.

In this repo you will find a work in progress library (and soon to be web app) which will allow a user to query from a database 
(for now, a `csv` file) and find book recommendations based on the content of a summary of the book queried.

### Peabody library
This is a library which contains the `models` and `utils` necessary to produce the recommendations. I will be adding more complex models to this
as the idea will be to have multiple models which cater to different types of recommendations. Right now there is a Doc2Vec
and TF-IDF implementation for the models. 

### `main.py`

`main.py` is now obsolete and is only really used for debugging Peabody locally.

### `app.py`

`app.py` is now the main file to run (will go through this in installation below). This is now where the code for the web 
app resides.

## Installation

- First run `pip install -r requirements.txt` to install all of the required dependencies
- You must have the spacy small language model, if you do not, run `python -m spacy download en_core_web_sm`
- The web app now works with the TFIDFRecommender module. This is the basic version of the recommender but now once `app.py`
is run the web app locallu will use the `model.pickle` vectors in order to fetch recommendations
- I will be deploying this soon once a couple more features have been built in.

## Future plans 

- Create a Flask API/Web app that will allow a user to query a recommendation from the front end.
- Hook this web app up to a database rather than a csv - having a REST API will also allow us to update the database 
with more books
- Implement a way in which to get different types of recommendations e.g. more exploratory or thematic models - more research to be done here
- Remove all traces of the pandas library. I've used it so far for convenience but it isn't efficient.
- Get ratings for all books in future so users can change how recommendations are ranked instead of most similar.