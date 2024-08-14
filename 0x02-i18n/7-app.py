#!/usr/bin/env python3
"""Task 7. Infer appropriate time zone"""

from flask import g, Flask, render_template, request
from flask_babel import Babel  # type: ignore
from typing import Union
import pytz

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


def get_user(user_id: str) -> Union[dict, None]:
    """Get user dictionary"""
    if not user_id.isnumeric():
        return None

    return users.get(int(user_id), None)


@app.before_request
def before_request():
    """Get user from url and set it as global."""
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(user_id)
    else:
        g.user = {}


@babel.localeselector
def get_locale():
    """Locale selector with priory"""
    # 1. Locale from URL parameters
    locale = request.args.get('locale', None)
    # 2. Locale from user settings
    if not locale:
        locale = g.user['locale'] if g.user else None
        locale = locale if locale in app.config['LANGUAGES'] else None
    # 3. Locale from request header
    if not locale and request.headers.get('Accept-Language'):
        locale = request.accept_languages.best_match(app.config['LANGUAGES'])
        locale = locale if locale in app.config['LANGUAGES'] else None
    # 4. Default locale
    if not locale:
        locale = app.config['BABEL_DEFAULT_LOCALE']

    return locale


@babel.timezoneselector
def get_timezone():
    """Timezone selector for appropriate time zone"""
    # 1.Timezone from URL parameters
    tz = request.args.get('timezone', None)
    # 2. Timezone from user settings
    if not tz:
        tz = g.user.get('timezone', None)
    try:
        pytz.timezone(tz)
    except pytz.exceptions.UnknownTimeZoneError:
        tz = None
    # 3. Default timezone
    if not tz:
        tz = app.config['BABEL_DEFAULT_TIMEZONE']

    return tz


@app.route('/')
def default_route():
    """Default route, Hello world"""
    username = g.user['name'] if g.user else None
    return render_template('6-index.html', username=username)


if __name__ == "__main__":
    app.run()
