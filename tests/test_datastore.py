import pytest
from progress_report.datastore import Datastore


@pytest.fixture
def db():
    # Temporary solution until we have proper database migrations and can
    # setup/teardown the database between tests
    db = Datastore(conn_string='sqlite:///:memory:')
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
    return db


def test_get_ohio_district_voting_data(db):
    results = db.get_ohio_district_voting_data()
    expected = [
        (1, 75, 25, 100),
        (2, 60, 40, 100),
        (3, 43, 57, 100),
        (4, 48, 52, 100),
        (5, 49, 51, 100),
    ]
    assert results == expected
