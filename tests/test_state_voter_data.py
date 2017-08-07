import pytest
from progress_report.state_voter_data import StateVoterData


class TestStateVoterData(object):
    # @pytest.fixture
    def ohio(self):
        data = [
            (1, 75, 25, 100),
            (2, 60, 40, 100),
            (3, 43, 57, 100),
            (4, 48, 52, 100),
            (5, 49, 51, 100),
        ]
        return StateVoterData('ohio', data=data)


    def test_name(self):
        subject = self.ohio()
        assert subject.name == 'Ohio'

    def test_districts(self):
        subject = self.ohio()
        assert len(subject.districts) == 5
        assert 'serialize' in dir(subject.districts[0])

    def test_net_wasted_votes(self):
        subject = self.ohio()
        assert subject.wasted_votes() == 101 # pos. numbers benefit repubs

    def test_efficiency_gap(self):
        subject = self.ohio()
        assert subject.efficiency_gap() == 0.202

    def test_serialize(self):
        subject = self.ohio().serialize()

        # just test keys to ensure this test isn't too brittle
        assert 'name' in subject
        assert 'districts' in subject
        assert len(subject['districts']) is 5
        assert 'efficiency_gap' in subject
        assert 'wasted_votes' in subject
