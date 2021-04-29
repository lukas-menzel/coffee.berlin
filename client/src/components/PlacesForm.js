import React, { useState } from "react";
import { Form, Input, Button } from "semantic-ui-react";

export const PlacesForm = ({ onNewPlace }) => {
  const [ name, setName] = useState("");

  return (
    <Form>
      <Form.Field>
        <Input
          placeholder="Place name"
          value={name}
          onChange={e => setName(e.target.value)}
        />
      </Form.Field>
      <Form.Field>
        <Button
          onClick={async () => {
            const place = { name };
            const response = await fetch("/api/place", {
              method: "POST",
              headers: {
                "Content-Type": "application/json"
              },
              body: JSON.stringify(place)
            });

            if (response.ok) {
              console.log("response worked!");
              onNewPlace(place);
              setName("");
            }
          }}
        >
          submit
        </Button>
      </Form.Field>
    </Form>
  );
};
