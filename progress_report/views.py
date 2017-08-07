from progress_report import app
from flask import jsonify, url_for

STATES = ['Ohio', 'Michigan', 'Wisconsin']


@app.route('/api')
def index():
    response = {
        'version' : 'v0.0',
        'greeting' : 'Welcome to the Scorecard API!',
        'states' : url_for('states'),
    }
    return jsonify(response)


@app.route('/api/states')
def states():
    response = {
        'back' : url_for('index'),
        'version' : 'v0.0',
        'states' : {state: url_for('show_state', state=state.lower()) for state in STATES},
        'data_source' : {
            'name' : 'Harvard Dataverse',
            'url' : '#'
        },
    }
    return jsonify(response)


@app.route('/api/states/<state>')
def show_state(state):
    response = {
        'back' : url_for('states'),
        'version' : 'v0.0',
        'name' : state.title(),
    }
    return jsonify(response)


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
