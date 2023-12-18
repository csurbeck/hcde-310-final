import functions

from flask import Flask, render_template, request

# Create an instance of Flask
app = Flask(__name__)


# Create a view function for /
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        new_quote = functions.get_quote()
        quote = new_quote[0]['content']
        speaker = new_quote[0]['author']
        quote_longest_word = functions.get_longest_word(new_quote)
        longest_word_info = functions.get_word_info(quote_longest_word)
        return render_template("results.html", quote=quote, speaker=speaker,
                               quote_longest_word=quote_longest_word, longest_word_info=longest_word_info)
    else:
        return "Error: wrong HTTP method, was expecting a POST request", 400
