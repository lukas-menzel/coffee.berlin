import React from "react";
import { List, Header } from "semantic-ui-react";

export const Places = ({ places }) => {
  return (
    <List>
      {places.map(place => {
        return (
          <List.Item key={place.name}>
            <Header>{place.name}</Header>
            <div>{place.street_house_number}</div>
            
          </List.Item>
        );
      })}
    </List>
  );
};
