from progress_report import app
from progress_report.state_voter_data import StateVoterData
from progress_report.datastore import Datastore

from flask import jsonify, url_for

# allow cross-origin requests to all api endpoints
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

db = Datastore(app)


@app.route('/api/')
def index():
    response = {
        'version' : 'v0.0',
        'greeting' : 'Welcome to the Scorecard API!',
        'links' : {
            'self' : url_for('index', _external=True),
            'states' : url_for('states', _external=True),
        },
    }
    return jsonify(response)



@app.route('/api/states/')
def states():
    response = {
        'version' : 'v0.0',
        'meta' : {
            'data_source' : {
                'name' : 'Harvard Dataverse',
                'url' : '#',
            },
        },
        'links' : {
            'self' : url_for('states', _external=True),
            'back' : url_for('index', _external=True),
            'states' : {
                'Ohio': url_for('show_ohio', _external=True),
            },
        }
    }
    return jsonify(response)


@app.route('/api/states/ohio')
def show_ohio():
    ohio_data = StateVoterData(
        'Ohio',
        data=db.get_ohio_district_voting_data(),
    )

    response = {
        'data' : ohio_data.serialize(),
        'links' : {
            'self' : url_for('show_ohio', _external=True),
            'back' : url_for('states', _external=True),
        },
        'version' : 'v0.0',
    }
    return jsonify(response)


#
# Error Handling
#

@app.errorhandler(404)
def page_not_found(ex):
    return jsonify(error=404, message=str(ex)), 404

@app.errorhandler(500)
def server_error(ex):
    return jsonify(error=500, message=str(ex)), 500




#
# Contains the data that we used during #UNHackTheVote2017 in case we need
# it for front-end development before the server is ready.
#
@app.route('/api/hackathon')
def hackathon():
    response = {
        "districts": [
            {
                "r_votes": 1364,
                "d_votes": 1000,
                "total": 2555
            },
            {
                "r_votes": 1803,
                "d_votes": 1000,
                "total": 2894
            },
            {
                "r_votes": 1000,
                "d_votes": 1655,
                "total": 2760
            },
            {
                "r_votes": 1165,
                "d_votes": 1000,
                "total": 2212
            },
            {
                "r_votes": 1241,
                "d_votes": 1000,
                "total": 2280
            },
            {
                "r_votes": 1348,
                "d_votes": 1000,
                "total": 2501
            },
            {
                "r_votes": 1828,
                "d_votes": 1000,
                "total": 2946
            },
            {
                "r_votes": 1240,
                "d_votes": 1000,
                "total": 2310
            },
            {
                "r_votes": 1000,
                "d_votes": 1838,
                "total": 2967
            },
            {
                "r_votes": 1477,
                "d_votes": 1000,
                "total": 2646
            },
            {
                "r_votes": 1000,
                "d_votes": 1550,
                "total": 2564
            },
            {
                "r_votes": 1590,
                "d_votes": 1000,
                "total": 2676
            },
            {
                "r_votes": 1000,
                "d_votes": 1395,
                "total": 2593
            },
            {
                "r_votes": 1130,
                "d_votes": 1000,
                "total": 2142
            },
            {
                "r_votes": 1321,
                "d_votes": 1000,
                "total": 2468
            },
            {
                "r_votes": 1327,
                "d_votes": 1000,
                "total": 2521
            }
        ],
        "efficiency_gap": {
            "democrats": -0.14864749603996585,
            "republicans": 0.2345741440233946
        }
    }
    return jsonify(response)
