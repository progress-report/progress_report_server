import pytest

def client():
    import progress_report
    progress_report.app.testing = True
    return progress_report.app.test_client()


def test_api_root_endpoint():
    app = client()
    assert 'application/json' == app.get('/api/').content_type

def test_root_endpoint_without_trailing_slash():
    app = client()
    assert '301 MOVED PERMANENTLY' == app.get('/api').status
    # assert 'application/json' == app.get('/api').content_type

def test_states_endpoint():
    app = client()
    assert 'application/json' == app.get('/api/states/').content_type

def test_states_endpoint_without_trailing_slash():
    app = client()
    assert '301 MOVED PERMANENTLY' == app.get('/api/states').status
    # assert 'application/json' == app.get('/api/states').content_type

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
    assert 'districts' in response_body['data']
    assert 'efficiency_gap' in response_body['data']
    assert 'wasted_votes' in response_body['data']

    assert 17 == len(response_body['data']['districts'])

    district_data = response_body['data']['districts']['1']
    assert 'd_votes' in district_data
    assert 'r_votes' in district_data
    assert 'total' in district_data
