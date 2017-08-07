import pytest
from progress_report.district_voter_data import DistrictVoterData


class TestDistrictVoterData(object):
    def test_district(self):
        subject = DistrictVoterData(1, d_votes=60, r_votes=40, total=100)
        assert subject.district is 1

    def test_wasted_votes(self):
        subject = DistrictVoterData(1, d_votes=60, r_votes=40, total=100)
        assert subject.wasted_votes() == -31 # neg. numbers benefit dems

    def test_serialize(self):
        subject = DistrictVoterData(1, d_votes=60, r_votes=40, total=100)
        expected = {
            'd_votes' : 60,
            'r_votes' : 40,
            'wasted_votes' : {'d_votes': 9, 'net': -31, 'r_votes': 40},
            'total' : 100,
        }
        assert subject.serialize() == expected
