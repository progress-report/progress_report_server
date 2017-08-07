from progress_report.district_voter_data import DistrictVoterData

class StateVoterData():
    __name = ''
    __districts = []

    def __init__(self, name, data):
        self.__name = name.title()
        self.__districts = [
            DistrictVoterData(district, d_votes, r_votes, total)
            for (district, d_votes, r_votes, total) in data
        ]

    #
    # PROPERTIES
    #

    @property
    def name(self): return self.__name

    @property
    def districts(self): return self.__districts

    #
    # METHODS
    #

    def serialize(self):
        return {
            'name' : self.name,
            'districts' : {d.district:d.serialize() for d in self.districts},
            'efficiency_gap' : self.efficiency_gap(),
            'wasted_votes' : {
                'd_votes' : self.wasted_d_votes(),
                'r_votes' : self.wasted_r_votes(),
                'net' : self.wasted_votes(),
            },
        }

    ##
    # The efficiency_gap and wasted_vote formulas are from:
    #
    #       https://www.brennancenter.org/sites/default/files/legal-work/\
    #           How_the_Efficiency_Gap_Standard_Works.pdf
    #
    # For the following calculations, remember:
    #
    #   D advantage   (-1.0) <------------+------------> (+1.0)   R advantage
    #
    def efficiency_gap(self):
        return (self.wasted_d_votes() - self.wasted_r_votes()) / self._total_votes()

    def wasted_votes(self):
        return sum([d.wasted_votes() for d in self.districts])

    def wasted_d_votes(self):
        return sum([d.wasted_d_votes() for d in self.districts])

    def wasted_r_votes(self):
        return sum([d.wasted_r_votes() for d in self.districts])

    def _total_votes(self):
        return sum([d.total for d in self.districts])
