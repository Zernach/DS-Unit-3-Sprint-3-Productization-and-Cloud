"""OpenAQ Air Quality Dashboard with Flask."""

from flask import Flask
import openaq

APP = Flask(__name__)


@APP.route('/')
def root():
    """Base view."""
    message = "[{'location': '21 de mayo', 'parameter': 'pm25', 'date': {'utc': '2019-12-20T15:00:00.000Z', 'local': '2019-12-20T12:00:00-03:00'}, 'value': 5, 'unit': 'µg/m³', 'coordinates': {'latitude': -37.471182288689, 'longitude': -72.36146284977}, 'country': 'CL', 'city': 'Los Angeles'}, {'location': 'Los Ángeles Oriente', 'parameter': 'pm25', 'date': {'utc': '2019-12-20T15:00:00.000Z', 'local': '2019-12-20T12:00:00-03:00'}, 'value': 3, 'unit': 'µg/m³', 'coordinates': {'latitude': -37.463035064801, 'longitude': -72.324575155457}, 'country': 'CL', 'city': 'Los Angeles'}]"
    return message


from flask_sqlalchemy import SQLAlchemy

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)


#greater10 = session.query(Record).filter(Record.value >= 10)


@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    DB.session.commit()
    return 'Data refreshed!'
