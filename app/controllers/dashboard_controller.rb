class DashboardController < ApplicationController
  def index
    render json: [1, 2, 3, 4, 5]
  end
end
