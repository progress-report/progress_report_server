module V0
  class DashboardController < ApplicationController
    def index
      @districts = {foo: 1, bar: 2}
      @efficiency_score = -0.34
    end
  end
end
