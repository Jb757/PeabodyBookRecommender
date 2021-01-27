# Peabody Book Recommender 
Named Peabody after to the famous and beautiful George Peabody library at The John Hopkins University in Baltimore.

In this repo you will find a work in progress library (and soon to be web app) which will allow a user to query from a database 
(for now, a `csv` file) and find book recommendations based on the content of a summary of the book queried.

### Peabody library
This is a library which contains the `models` and `utils` necessary to produce the recommendations. I will be adding more complex models to this
as the idea will be to have multiple models which cater to different types of recommendations. Right now there is a Doc2Vec
and TF-IDF implementation for the models. 

### main.py

`main.py` right now only has a few lines of code which when run will output to the terminal the top most similar `results`
to the terminal. In future this will be used to create the web app as well as produce the recommendations. 

### Installation

- First run `pip install -r requirements.txt` to install all of the required dependencies
- You must have the spacy small language model, if you do not, run `python -m spacy download en_core_web_sm`
- running the main.py file with line 7 commented out will train a model for the recommender model you have
selected at the time `Doc2VecRecommender` will create a file called `doc2vecModel` and the `TfidRecommender` will create
 a file called `model.pickle`. 
- Once the models are trained then you can uncomment line 7 and they will be significantly quicker to find 
recommendations printed to your terminal.





## Future plans 

- Create a Flask API/Web app that will allow a user to query a recommendation from the front end.
- Hook this web app up to a database rather than a csv - having a REST API will also allow us to update the database 
with more books
- Implement a way in which to get different types of recommendations e.g. more exploratory or thematic models - more research to be done here
- Remove all traces of the pandas library. I've used it so far for convenience but it isn't efficient.
- Get ratings for all books in future so users can change how recommendations are ranked instead of most similar.