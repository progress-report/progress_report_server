DistrictVoterData = Struct.new(:votes, :total) do
  def republican_win?
    votes[:republican] > votes[:democrat]
  end

  def democratic_win?
    !republican_win?
  end
end

class StateVoterData
  include Enumerable

  attr_reader :districts

  def each(&block)
    districts.each(&block)
  end

  def initialize(districts)
    @districts = districts
  end

  def efficiency_gap_for(party)
    (seat_margin_for(party) - 0.5) - 2 * (vote_margin_for(party) - 0.5)
  end

  def vote_margin_for(party)
    total_votes_for(party) * 1.0 / total_votes
  end

  def seat_margin_for(party)
    total_wins = districts.count do |district|
      case party
      when :republican then district.republican_win?
      when :democrat   then district.democratic_win?
      end
    end

    total_wins * 1.0 / districts.count
  end

  private

  def total_votes
    districts.sum { |d| d.total }
  end

  def total_votes_for(party)
    districts.sum { |d| d.votes[party] }
  end
end
