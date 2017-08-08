import pytest
from progress_report.district_voter_data import DistrictVoterData


class TestDistrictVoterData(object):
    @pytest.fixture
    def district_2(self):
        return DistrictVoterData(2, d_votes=60, r_votes=40, total=100)

    def test_district(self, district_2):
        assert district_2.district is 2

    def test_wasted_votes(self, district_2):
        assert district_2.wasted_votes() == -31 # neg. numbers benefit dems

    def test_serialize(self, district_2):
        expected = {
            'd_votes' : 60,
            'r_votes' : 40,
            'wasted_votes' : {'d_votes': 9, 'net': -31, 'r_votes': 40},
            'total' : 100,
        }
        assert district_2.serialize() == expected
