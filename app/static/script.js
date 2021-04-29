function warnUser(){
    alert("You pushed a button!")
}

// function createNewPlace() {
//     const form_data = new FormData(document.getElementById("create-place-form"));
//     console.log(form_data)
//     fetch("/place", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         Accept: "application/json",
//       },
//       body: JSON.stringify(form_data),
//     })
//       .then(
//         //same basic code as above - catch errors if there are any.
//         function (response) {
//           // if the response is not a 201 OK (resource created), log it.
//           if (response.status !== 201) {
//             // this is the equivalent to a python print() statement, and it will print to the browser console
//             console.log(
//               "Looks like there was a problem. Status Code: " + response.status
//             );
//           }
//         }
//       )
//       .catch(function (err) {
//         console.log("Fetch Error, booo!", err);
//       });
// }
// fetch('/place')
//       .then(res => res.json())
//       .then(data => console.log(data))  

const create_place_Form = document.getElementById("create-place");
if(create_place_Form) {
create_place_Form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const form_data = new FormData(create_place_Form)
  const form_data_serialized = Object.fromEntries(form_data)
  const jsonObject = {...form_data_serialized, sendToSelf: form_data_serialized.sendToSelf ? true : false,};

  try {
    const response = await fetch("/api/place", {
      method: 'POST',
      headers: {
        'Content-Type' : 'application/json'
      },
      body: JSON.stringify(jsonObject),
      
    });
    const json = await response.json();
    console.log(json);

  } catch(e) {
    console.log("Error");
  }

})
}
/*Get place */ 

const places = document.getElementById('places')
const container = document.createElement('div')
container.setAttribute('class', 'container')
places.appendChild(container)

fetch('/api/place')
  .then(
    function (response) {
      if (response.status !== 200) {
        // this is the equivalent to a python print() statement, and it will print to the browser console
        console.log(
          "Looks like there was a problem. Status Code: " + response.status
        );
        return
      }
      response.json().then(function (data) {
        data.places.forEach((place) => {
          // Create a div with a card class
          const card = document.createElement('div')
          var a = document.createElement('a');
          a.setAttribute('href','/place/link');
          link = place.id
          card.setAttribute('class', "card border border-black m-4")
        
          const h1 = document.createElement('h1')
          h1.textContent = place.name
          const p = document.createElement('p')
          const div = document.createElement('div')
          place.address = place.street_house_number
          place.postcode = place.postcode
          p.textContent = place.address 
          div.textContent = place.postcode
        
          // Append the cards to the container element
          container.appendChild(a)
          container.appendChild(card)
        
          // Each card will contain an h1 and a p
          card.appendChild(h1)
          card.appendChild(p)
          card.appendChild(div)
        });
      });
  })
    // })
  .catch((err) => {
    // Do something for an error here
  });
