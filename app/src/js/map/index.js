import { geoPath, geoAlbersUsa, select, queue, json as d3JSON } from 'd3';
import { feature as topoFeature } from 'topojson';

let data = { districts: null, us: null, fips: null, state2fips: {}, statesData: {} };

class Map {
  constructor(el, actions){
    this.el = el;
    this.actions = actions;
    this.width = 960;
    this.height = 500;
    this.centered = { id: -1 };
    this.projection = geoAlbersUsa()
      .scale(1070)
      .translate([this.width / 2, this.height / 2]);;
    this.path = geoPath(this.projection);
    this.svg = select(el).append('svg')
      .attr('viewBox', `0 0 ${this.width} ${this.height}`)
      .append('g');

    this.svg.append('rect')
      .attr('height', this.height)
      .attr('width', this.width)
      .on('click', this.clicked);

    this.districts = null;
    this.states = null;
  }

  draw(stateName) {
    if(data.districts && data.us){
      this.drawDistricts(data.districts, data.us);
      this.drawStates(data.us);
      if(stateName) this.fetchData(stateName);
      return this;
    }
    queue()
      .defer(d3JSON, '/data/us-congress-113.json')
      .defer(d3JSON, '/data/us.json')
      .defer(d3JSON, '/data/fips2state.json')
      .await((error, districts, us, fips) => {
        if(error) throw error;
        data.districts = districts;
        data.us = us
        data.fips = fips;
        for(let k in fips)
          data.state2fips[fips[k].toLowerCase()] = k;
        this.drawDistricts(districts, us);
        this.drawStates(us);
        if(stateName) this.fetchData(stateName);

      });
    return this;
  }

  drawDistricts(json, us){
    this.svg.append('defs').append('path')
      .attr('id', 'land')
      .datum(topoFeature(us, us.objects.land))
      .attr('d', this.path);

    this.svg.append('clipPath')
        .attr('id', 'clip-land')
      .append('use')
        .attr('xlink:href', '#land');

    this.districts = this.svg.append('g')
      .attr('class', 'districts')
      .attr("clip-path", "url(#clip-land)")
      .selectAll('district')
      .data(topoFeature(json, json.objects.districts).features)
    .enter().append('path')
      .attr('class', 'district')
      .attr('d', this.path);
  }

  drawStates(json){
    this.states = this.svg.append('g')
      .attr('class', 'states')
      .selectAll('state')
      .data(topoFeature(json, json.objects.states).features)
    .enter().append('path')
      .attr('class', 'state')
      .attr('d', this.path)
      .on('click', this.clicked);
      //.on('mouseenter', (d)=>{console.log(d);});
  }

  clicked = (d) => {
    let stateName = data.fips[d.id].toLowerCase();
    if(this.centered.id == d.id){
      this.actions.showState('', false);
    } else if(stateName=='ohio'){
      this.fetchData(stateName);
    } else {
      this.actions.showState(stateName, false);
    }
  }

  fetchData = (stateName) => {
    d3JSON(`/api/states/${stateName}`, (error, json) => {
      console.log(json);
      this.actions.showState(stateName, json ? json.data : false);
    });
  }

  zoomTo(stateName) {
    let fip = data.state2fips[stateName];
    let d = topoFeature(data.us, data.us.objects.states).features.find((_d)=>(_d.id==fip));
    queue().defer(()=>{this._zoomTo(d);})
  }

  _zoomTo = (d) => {
    let x, y, k;
    if (d && this.centered.id !== d.id) {

      let centroid = this.path.centroid(d);
      x = centroid[0];
      y = centroid[1];
      k = 4;
      this.centered = d;
      this.states.classed('inactive', (_d)=>(_d.id!=d.id))
        .classed('active', (_d)=>(_d.id==d.id));
    } else {

      x = this.width / 2;
      y = this.height / 2;
      k = 1;
      this.centered = { id: -1 };
      this.states.classed('inactive', false)
        .classed('active', false);
    }

    this.svg.transition()
        .duration(750)
        .attr('transform', 'translate(' + this.width / 2 + ',' + this.height / 2 + ')scale(' + k + ')translate(' + -x + ',' + -y + ')')
        .style('stroke-width', 1.5 / k + 'px');
  }
}

export default Map;
