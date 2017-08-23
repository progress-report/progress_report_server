import { Component } from 'react';
import { format } from 'd3';
import Map from '../map/index';

const State = ({ data: { name, districts, efficiency_gap, wasted_votes }}) => (
  <div className="state-tooltip__data">
    <h1>{name}</h1>
    <div className="row">
      <label>Efficiency Gap</label>
      <span className="value">{format('.2%')(efficiency_gap)}</span>
    </div>
    <div className="row wasted-votes--dem">
      <label>Wasted Democratic Votes</label>
      <span className="value">{format(',')(wasted_votes.d_votes)}</span>
    </div>
    <div className="row wasted-votes--rep">
      <label>Wasted Republican Votes</label>
      <span className="value">{format(',')(wasted_votes.r_votes)}</span>
    </div>
  </div>
);

class Report extends Component {
  constructor(props){
    super(props);
    this.stateData = null;
    this.el = null;
    this.map = null;
  }

  showState = (stateName, d) => {
    this.stateData = d;
    this.linkToState(stateName);
  }

  linkToState = (stateName) => {
    this.props.history.push(`/report/${stateName}`);
  }

  componentDidMount(){
    let { stateName } = this.props.match.params;
    this.map = new Map(this.el, { showState: this.showState }).draw(stateName);
  }

  componentWillReceiveProps(nextProps){
    // zoom on history update to use back/forward buttons
    let { stateName } = nextProps.match.params;
    this.map.zoomTo(stateName);
  }

  render(){
    return (
      <section id="report">
        <div id="map" ref={(el)=>{this.el=el;}}/>
        <div className="state-tooltip">
          {this.stateData && <State data={this.stateData} />}
        </div>
      </section>
    );
  }
}

export default Report;
