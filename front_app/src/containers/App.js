import React from 'react';
import '../App.css';
import logo from '../logo.svg';
import TestContainer from './TestContainer'
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { NavigationBar } from '../components/NavigationBar';
import { Home } from '../Home';
import { Data } from '../Data';
import { Transformations } from '../Transformations';



function App() {
  return (
    <React.Fragment>
      <Router>
        <NavigationBar />
        <React.Component/>
      </Router>
    </React.Fragment>
  );
}


export default App;
