require 'efficiency_gap'

# The purpose of this class is to aggregate the data stored in our database.
#
# This is not the best way to do this, but while we have data dumped in JSON
# columns, this will provide a single interface for the API.
class StateElectionData
  def initialize
    @state = Marshal.load "\x04\bo:\x13StateVoterData\x06:\x0F@districts[\x15S:\x16DistrictVoterData\a:\n" +
      "votes{\a:\x0Frepublicani\x02T\x05:\rdemocrati\x02\xE8\x03:\n" +
      "totali\x02\xFB\tS;\a\a;\b{\a;\ti\x02\v\a;\n" +
      "i\x02\xE8\x03;\vi\x02N\vS;\a\a;\b{\a;\n" +
      "i\x02w\x06;\ti\x02\xE8\x03;\vi\x02\xC8\n" +
      "S;\a\a;\b{\a;\ti\x02\x8D\x04;\n" +
      "i\x02\xE8\x03;\vi\x02\xA4\bS;\a\a;\b{\a;\ti\x02\xD9\x04;\n" +
      "i\x02\xE8\x03;\vi\x02\xE8\bS;\a\a;\b{\a;\ti\x02D\x05;\n" +
      "i\x02\xE8\x03;\vi\x02\xC5\tS;\a\a;\b{\a;\ti\x02$\a;\n" +
      "i\x02\xE8\x03;\vi\x02\x82\vS;\a\a;\b{\a;\ti\x02\xD8\x04;\n" +
      "i\x02\xE8\x03;\vi\x02\x06\tS;\a\a;\b{\a;\n" +
      "i\x02.\a;\ti\x02\xE8\x03;\vi\x02\x97\vS;\a\a;\b{\a;\ti\x02\xC5\x05;\n" +
      "i\x02\xE8\x03;\vi\x02V\n" +
      "S;\a\a;\b{\a;\n" +
      "i\x02\x0E\x06;\ti\x02\xE8\x03;\vi\x02\x04\n" +
      "S;\a\a;\b{\a;\ti\x026\x06;\n" +
      "i\x02\xE8\x03;\vi\x02t\n" +
      "S;\a\a;\b{\a;\n" +
      "i\x02s\x05;\ti\x02\xE8\x03;\vi\x02!\n" +
      "S;\a\a;\b{\a;\ti\x02j\x04;\n" +
      "i\x02\xE8\x03;\vi\x02^\bS;\a\a;\b{\a;\ti\x02)\x05;\n" +
      "i\x02\xE8\x03;\vi\x02\xA4\tS;\a\a;\b{\a;\ti\x02/\x05;\n" +
      "i\x02\xE8\x03;\vi\x02\xD9\t"
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
