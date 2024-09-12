from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_headlines(category):
    url = f"https://www.bbc.com/{category}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = soup.find_all(name='h2', class_="sc-9ea79d00-16 jhCgGk")
    return [headline.getText() for headline in headlines]


@app.route('/', methods = ['GET'])
def home():
    news_headlines = get_headlines('live')
