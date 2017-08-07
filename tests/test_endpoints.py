import pytest

def client():
    import progress_report
    progress_report.app.testing = True
    return progress_report.app.test_client()


def test_api_root_endpoint():
    app = client()
    assert 'application/json' == app.get('/api').content_type

def test_states_endpoint():
    app = client()
    assert 'application/json' == app.get('/api/states').content_type

def test_ohio_endpoint():
    app = client()
    assert 'application/json' == app.get('/api/states/ohio').content_type


#
# We expect it to be in the following form:
#
#   {
#       'districts': {
#           '1' : {
#               'd_votes' : 1000,
#               'r_votes' : 999,
#               'total' : 2100,
#               ...
#           },
#           ...
#       },
#       'efficiency_gap' : 0.109,
#       ...
#   }
#
def test_ohio_endpoint_fields():
    import json
    app = client()
    response_body = json.loads(app.get('/api/states/ohio').data)
    assert 'districts' in response_body
    assert 'efficiency_gap' in response_body

    assert 5 == len(response_body['districts'])

    assert 'd_votes' in response_body['districts']['1']
    assert 'r_votes' in response_body['districts']['1']
    assert 'total' in response_body['districts']['1']
