import React, {Component} from 'react';
import axios from 'axios'
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
    axios.get('http://192.168.1.4:8083/',{
      params: {
        m : 5000,
        k : 10000,
        n : 10000
      }
    })
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
          <div>
            {this.state.cuda}
          </div>
        </header>
      </div>
    );
  }
}

export default App;
