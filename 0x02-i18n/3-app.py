#!/usr/bin/env python3
"""Task 3. Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel  # type: ignore

app = Flask(__name__)


class Config:
    """Config class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Locale selector based on user preferences."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def default_route():
    """Default route, Hello world"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
