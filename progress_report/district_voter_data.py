class DistrictVoterData():
    __district = 0
    __d_votes = 0
    __r_votes = 0
    __total = 0

    def __init__(self, district, d_votes, r_votes, total):
        self.__district = district
        self.__d_votes = d_votes
        self.__r_votes = r_votes
        self.__total = total

    #
    # PROPERTIES
    #

    @property
    def district(self): return self.__district

    @property
    def d_votes(self): return self.__d_votes

    @property
    def r_votes(self): return self.__r_votes

    @property
    def total(self): return self.__total

    #
    # METHODS
    #

    def serialize(self):
        return {
            'd_votes' : self.d_votes,
            'r_votes' : self.r_votes,
            'wasted_votes' : {
                'd_votes' : self.wasted_d_votes(),
                'r_votes' : self.wasted_r_votes(),
                'net' : self.wasted_votes(),
            },
            'total' : self.total,
        }

    ##
    # The efficiency_gap and wasted_vote formulas are from:
    #
    #       https://www.brennancenter.org/sites/default/files/legal-work/\
    #           How_the_Efficiency_Gap_Standard_Works.pdf
    #
    #
    # For the following calculations, remember:
    #
    #   D advantage   (-1.0) <------------+------------> (+1.0)   R advantage
    #
    def wasted_votes(self):
        return self.wasted_d_votes() - self.wasted_r_votes()

    def _min_required_votes(self): return int(self.total / 2) + 1

    def wasted_r_votes(self):
        if self.r_votes > self.d_votes:
            return self.r_votes - self._min_required_votes()
        else:
            return self.r_votes

    def wasted_d_votes(self):
        if self.d_votes > self.r_votes:
            return self.d_votes - self._min_required_votes()
        else:
            return self.d_votes
