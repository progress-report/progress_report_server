import pytest
from progress_report.state_voter_data import StateVoterData


class TestStateVoterData(object):
    @pytest.fixture
    def ohio(self):
        data = [
            (1, 75, 25, 100),
            (2, 60, 40, 100),
            (3, 43, 57, 100),
            (4, 48, 52, 100),
            (5, 49, 51, 100),
        ]
        return StateVoterData('ohio', data=data)

    def test_name(self, ohio):
        assert ohio.name == 'Ohio'

    def test_districts(self, ohio):
        assert len(ohio.districts) == 5
        assert 'serialize' in dir(ohio.districts[0])

    def test_net_wasted_votes(self, ohio):
        assert ohio.wasted_votes() == 101 # pos. numbers benefit repubs

    def test_efficiency_gap(self, ohio):
        assert ohio.efficiency_gap() == 0.202

    def test_serialize(self, ohio):
        subject = ohio.serialize()

        # just test keys to ensure this test isn't too brittle
        assert 'name' in subject
        assert 'districts' in subject
        assert len(subject['districts']) is 5
        assert 'efficiency_gap' in subject
        assert 'wasted_votes' in subject
