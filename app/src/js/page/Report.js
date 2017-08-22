import { Component } from 'react';
import Map from '../map/index';

const State = ({ data }) => (
  <div className="state-tooltip">{data}</div>
);

class Report extends Component {
  el = null;
  constructor(props){
    super(props);
    this.state = {
      stateData: null
    };
  }

  showState = (d) => {
    this.setState({ stateData: d });
  }

  componentDidMount(){
    new Map(this.el, {showState: this.showState}).draw();
  }

  render(){
    return (
      <section id="report">
        <div id="map" ref={(el)=>{this.el=el;}}/>
        {this.state.stateData && <State data={this.state.stateData} />}
      </section>
    );
  }
}

export default Report;
