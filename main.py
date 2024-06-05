from flask import Flask
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def home():
    return "<h2>Hello world from Flask</h2>"


@app.route('/setimento/<frase>')
def setimento(frase):

    tb = TextBlob(frase)
    polaridade = tb.sentiment.polarity
    return "Polaridade:{}".format(polaridade)


app.run(debug=True)
