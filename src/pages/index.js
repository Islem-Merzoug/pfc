import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {

  state = {
    image: null
  };

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value
    })
  };

  handleImageChange = (e) => {
    this.setState({
      image: e.target.files[0]
    })
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('image', this.state.image, this.state.image.name);
    // let url = 'http://localhost:8000/api/posts/';
    let url = 'http://localhost:8000/image';
    axios.post(url, form_data, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
        .then(res => {
          console.log(res.data);
        })
        .catch(err => console.log(err))
  };

  handleExecute = (e) => {

    let url = 'http://localhost:8000/execute';
    axios.post(url)
        .then(res => {
          console.log(res.data);
        })
        .catch(err => console.log(err))
  };

  handleDownload = (e) => {

    let url = 'http://localhost:8000/download';
    axios.post(url)
        .then(res => {
          console.log(res.data);
        })
        .catch(err => console.log(err))
  };

  render() {
    return (
      <div className="App">
        <form onSubmit={this.handleSubmit}>

          <p>
            <input type="file"
                   id="image"
                   onChange={this.handleImageChange} required/>
          </p>
          <input type="submit"/>
        </form>

        <button onClick={this.handleExecute}> Execute </button>
        <button onClick={this.handleDownload}> Download </button>
      </div>
    );
  }
}

export default App;