from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

from serializer import ArticleSerializer
from db_utils import get_count, config

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template('index.html', count=get_count())

# List article endpoint
class ArticleList(Resource):
    """Returns list of available articles"""
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start', type=int)
        args = parser.parse_args(strict=True)
        return ArticleSerializer.get_list(args['start'])

# Search article endpoint
class ArticleSearch(Resource):
    """Returns list of available articles with search keyword"""
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('query', type=str, required=True)
        parser.add_argument('start', type=int)
        args = parser.parse_args(strict=True)
        return ArticleSerializer.get_search(args['query'], args['start'])

# Article details endpoint
class Article(Resource):
    """Returns details of a single rticles"""
    def get(self, id):
        return ArticleSerializer.get_article(id)

# Add resources to API
api.add_resource(ArticleList, '/list')
api.add_resource(ArticleSearch, '/search')
api.add_resource(Article, '/article/<string:id>')

if __name__ == '__main__':
    app.run(debug=(True if config['DEBUG'] == 'True' else False))