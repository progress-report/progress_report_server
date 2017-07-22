json.districts @state_data.districts
json.efficiency_gap do
  json.democrats @state_data.efficiency_gap_for(:democrat)
  json.republicans @state_data.efficiency_gap_for(:republican)
end
