import pytest

#
# Integration tests for API endpoints
#

@pytest.fixture
def app():
    import progress_report
    progress_report.app.testing = True
    init_db(progress_report.views.db)

    return progress_report.app.test_client()

def init_db(db):
    # Temporary solution until we have proper database migrations and can
    # setup/teardown the database between tests
    records = [
        (1, 75, 25, 100),
        (2, 60,  0,  60),
        (2,  0, 40,  40),
        (3, 43, 57, 100),
        (4, 48, 52, 100),
        (5, 40, 50,  90),
        (5,  9,  1,  10),
    ]
    for d, dv, rv, tv in records:
        ins = db.ohio.insert().values(
            HOUSE_DISTRICT=d,
            ush_dvote_08=dv,
            ush_rvote_08=rv,
            ush_tvote_08=tv,
        )
        db.conn.execute(ins)



def test_api_root_endpoint(app):
    assert 'application/json' == app.get('/api/').content_type

def test_root_endpoint_without_trailing_slash(app):
    assert '301 MOVED PERMANENTLY' == app.get('/api').status
    # assert 'application/json' == app.get('/api').content_type

def test_states_endpoint(app):
    assert 'application/json' == app.get('/api/states/').content_type

def test_states_endpoint_without_trailing_slash(app):
    assert '301 MOVED PERMANENTLY' == app.get('/api/states').status
    # assert 'application/json' == app.get('/api/states').content_type

def test_ohio_endpoint(app):
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
def test_ohio_endpoint_fields(app):
    import json
    response_body = json.loads(app.get('/api/states/ohio').data)

    assert 'districts' in response_body['data']
    assert 'efficiency_gap' in response_body['data']
    assert 'wasted_votes' in response_body['data']

    assert 5 == len(response_body['data']['districts'])

    district_data = response_body['data']['districts']['1']
    assert 'd_votes' in district_data
    assert 'r_votes' in district_data
    assert 'total' in district_data
