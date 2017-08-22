import { geoPath, geoAlbersUsa, select, queue, json as d3JSON } from 'd3';
import { feature as topoFeature } from 'topojson';

let data = { districts: null, us: null };

class Map {
  constructor(el, actions){
    this.el = el;
    this.actions = actions;
    this.width = 960;
    this.height = 500;
    this.centered = null;
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
  }

  draw() {
    if(data.districts && data.us){
      this.drawDistricts(data.districts);
      this.drawStates(data.us);
      return this;
    }
    queue()
      .defer(d3JSON, 'data/us-congress-113.json')
      .defer(d3JSON, 'data/us.json')
      .await((error, districts, us) => {
        if(error) throw error;
        data.districts = districts;
        data.us = us
        this.drawDistricts(districts);
        this.drawStates(us);
      });
    return this;
  }

  drawDistricts(json){
    this.svg.append('g')
      .attr('class', 'districts')
      .selectAll('district')
      .data(topoFeature(json, json.objects.districts).features)
    .enter().append('path')
      .attr('class', 'district')
      .attr('d', this.path)
      ;
  }

  drawStates(json){
    this.svg.append('g')
      .attr('class', 'states')
      .selectAll('state')
      .data(topoFeature(json, json.objects.states).features)
    .enter().append('path')
      .attr('class', 'state')
      .attr('d', this.path)
      .on('click', this.clicked);
  }

  clicked = (d) => {
    let x, y, k;
    if (d && this.centered !== d) {
      let centroid = this.path.centroid(d);
      x = centroid[0];
      y = centroid[1];
      k = 4;
      this.centered = d;
    } else {
      x = this.width / 2;
      y = this.height / 2;
      k = 1;
      this.centered = null;
    }

    this.svg.transition()
        .duration(750)
        .attr("transform", "translate(" + this.width / 2 + "," + this.height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
        .style("stroke-width", 1.5 / k + "px");

    this.actions.showState('HEY!');
  }
}

export default Map;
