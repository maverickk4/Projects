from flask import Flask, request, render_template
import requests

app = Flask(__name__)
api_key = "553ad8b749104d99b6aa7de7a2928614"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term')
    url = f"https://newsapi.org/v2/top-headlines?q={search_term}&pageSize=5&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return render_template('index.html', articles=articles, search_term=search_term)

if __name__ == '__main__':
    app.run()
