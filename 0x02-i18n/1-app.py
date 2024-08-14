#!/usr/bin/env python3
"""Task 0.basic Flask app"""

from flask import Flask, render_template
from flask_babel import Babel  # type: ignore

app = Flask(__name__)


class Config:
    """Config class for Babel"""
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def default_route():
    """Default route, Hello world"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
