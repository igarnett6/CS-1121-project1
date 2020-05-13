let resp = fetch("http://localhost:5000/Classmates/add", {
  headers: {
    'token': this.state.token,
    'Content-Type': 'application/json',
  },
  method: 'POST',
  body: JSON.stringify(//Example body goes here { code: 'xyz' })
}).then(function(resp) { //Do stuff with the response }
