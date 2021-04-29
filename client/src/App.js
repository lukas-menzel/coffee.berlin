import React, { useState, useEffect } from 'react';
import { BrowserRouter, Link, Switch, Route } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import { Places } from "./components/Places";
import { PlacesForm } from "./components/PlacesForm";
import { Container } from "semantic-ui-react";
import { Header } from "./components/Navigation"

function App() {
  const [places, setPlaces] = useState([]);

  useEffect(() => {
    fetch("/api/place").then(response =>
      response.json().then(data => {
        setPlaces(data.places);
      })
    );
  }, []);

  return (
    <Container style={{ marginTop: 40 }}>
<BrowserRouter>
          <div>
            <Link className="App-link" to="/">Home</Link>
            &nbsp;|&nbsp;
            <Link className="App-link" to="/page2">Page2</Link>
          </div>
          <Switch>
            <Route exact path="/">
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
                <PlacesForm
        onNewPlace={place =>
          setPlaces(currentPlaces => [place, ...currentPlaces])
        }
      />
      <Places places={places} />
            </Route>
            <Route path="/page2">
                <p>This is page 2!</p>
            </Route>
          </Switch>
        </BrowserRouter>
     
    </Container>
    
  );
}

export default App;
