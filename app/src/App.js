import React, {Component} from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';


class App extends Component{

  constructor(props){
    super(props)
    this.fetch_content()
    this.state ={
      cuda : "abc"
    }
  }

  fetch_content(){
    axios.get('http://192.168.1.4:8083/')
    .then(response => {
          this.setState({
            cuda : "Single Precision - " + response.data["Single"] + " Double Precision - " + response.data["Double"]
          })
      })
  }
  render(){
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          <div>
            {this.state.cuda}
          </div>
        </header>
      </div>
    );
  }
}

export default App;
