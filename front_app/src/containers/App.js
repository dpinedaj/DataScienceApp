import React from 'react';
import '../App.css';
import logo from '../logo.svg';
import TestContainer from './TestContainer'
import MySideBar from './SideBar'

function App() {
  return (
    <div className="App">
      <body className="App-body">
      <img src={logo} className="App-logo" alt="logo" />
        <MySideBar className= "Nav-bar" />
        <TestContainer />
      </body>
    </div>
  );
}

export default App;
