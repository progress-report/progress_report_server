require 'efficiency_gap'

# The purpose of this class is to aggregate the data stored in our database.
#
# This is not the best way to do this, but while we have data dumped in JSON
# columns, this will provide a single interface for the API.
class StateElectionData
  def initialize
    @state = StateVoterData.new(
      [
        DistrictVoterData.new({democrat:75, republican:25}, 100),
        DistrictVoterData.new({democrat:60, republican:40}, 100),
        DistrictVoterData.new({democrat:43, republican:57}, 100),
        DistrictVoterData.new({democrat:48, republican:52}, 100),
        DistrictVoterData.new({democrat:49, republican:51}, 100),
      ]
    )
  end

  def districts
    state.map do |district|
      {
        r_votes: district.votes[:republican],
        d_votes: district.votes[:democrat],
        total: district.total,
      }
    end
  end

  def efficiency_gap_for(party)
    state.efficiency_gap_for(party)
  end

  private

  attr_reader :state
end
