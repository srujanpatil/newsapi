# News API for theguardian.com

**Note**: _Run all commands from root directory as shown below as relative filepaths might get affected._

## Setup
```
# clone repo
$ git clone https://github.com/srujanpatil/newsapi.git
$ cd newsapi

# Setup a virtual environment
$ python3 -m venv env

# Activate env
$ source env/bin/activate

# Install requirements
(env) $ pip install -r requirements.txt
```
You will also need a MongoDB database to connect to. I had used a MongoDB instance on [MongoDB Atlas](https://www.mongodb.com/atlas/database) so you can either use that, or connect to your own instance.

Add conifg file to root (newsapi/config.json)
```
{   
    "DEBUG": "True",
    "DB": "DB_NAME",
    "Id": "USER_ID",
    "Password": "USER_PASSWORD",
    "Paginate": 5,
    "rss": ["https://www.theguardian.com/au/rss","https://www.theguardian.com/business/economics/rss"]
}
```
- The "rss" list contains valid theguardian.com rss urls.
- The "Paginate" parameter determines the length of the page. Example, here it's 5, so each page will contain max of 5 articles.
- Note here the "mongodb+srv" protocol is used to connect to the DB. You can find the above DB params in the [connection string](https://docs.mongodb.com/manual/reference/connection-string/). If you want connect by any other means, you can tweak [this](https://github.com/srujanpatil/newsapi/blob/6635dd2d1839e9afae019ff33141afcbe427c6cf/api/db_utils.py#L10).
---
## API
You can view the API docs at the homepage ('/') or [here](docs.md).

Start API at http://127.0.0.1:5000
```
(env) $ python3 api/app.py 
```

---
## News Scrapper
The news scrapper polls this [rss feed](https://www.theguardian.com/au/rss) to find the latest news.

```
(env) $ python3 api/scrapper.py
```
- **Note**: Command line logs (stream) are only active when DEBUG is set to "True". With DEBUG set to "False" logging level is set to INFO and logs are generated in the respective folder.

---
## Test
Testing API endpoints
(make sure the Flask DEV server is on before running tests)
```
(env) $ python3 api/test_api.py
```

---
## Todo
- Write test for `scrapper.py`, `serializer.py` and `db_utils.py`
- Explore mongoengine flask extension
- Scrape individual article pages
- Add SwaggerUI to standardize docs
- Run tests with Github Actions (CI)

---
## Shortcomings and possible improvements
These are some self-assessed shortcomings of my code which I didn't have time to work on and improve.

- The tests in `test_api.py` aren't decoupled.
    - Use Fixtures and Mock.
    - Use Flask Testing instead of simple request-response.

- Refactor scapper code.
    - Validate for current date (to avoid non-unique inserts)
    - Wrap it under a class.
    - Decouple DB inserts.

- Package Api and Scrapper and their tests seperately.
