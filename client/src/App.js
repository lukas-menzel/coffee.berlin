import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import { Places } from "./components/Places";
import { PlacesForm } from "./components/PlacesForm";
import { Container } from "semantic-ui-react";
import { Header } from "./components/Navigation"

function App() {
  const [places, setPlaces] = useState([]);

  useEffect(() => {
    fetch("/place").then(response =>
      response.json().then(data => {
        setPlaces(data.places);
      })
    );
  }, []);

  return (
    <Container style={{ marginTop: 40 }}>

      <PlacesForm
        onNewPlace={place =>
          setPlaces(currentPlaces => [place, ...currentPlaces])
        }
      />
      <Places places={places} />
    </Container>
  );
}

export default App;
