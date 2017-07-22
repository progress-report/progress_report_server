class DashboardController < ApplicationController
  def index
    @state_data = StateElectionData.new
  end
end
