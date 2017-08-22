import './scss/index.scss';

import * as React from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Header from './js/components/Header';
import Homepage from './js/page/Homepage';
import Report from './js/page/Report';

window.React = React;

class App extends React.Component {
  render(){
    return (
      <Router>
        <main>
          <Header />
          <Route exact path="/" component={Homepage} />
          <Route path="/report" component={Report} />
        </main>
      </Router>
    );
  }
}

if(document.readyState != 'loading') init();
else document.addEventListener('DOMContentLoaded', init);

function init(){
  render(<App />, document.getElementById('progressreport'));
}
