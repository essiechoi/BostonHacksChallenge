import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [getMessage, setGetMessage] = useState({})
  const [userVal, setUserVal] = useState("")


const getInputValue = (event)=>{
    // show the user input value to console
    setUserVal(event.target.value)
};

const handleSubmit = () =>{
  axios.post('http://127.0.0.1:5000/update', {
    message: userVal,
    type: "create"
  }).then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })
}

const handleDelete = () => {
  axios.delete('http://127.0.0.1:5000/update', {
    data: {
      message: userVal,
      type: "delete"
    }
  }).then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })
}
  

  return (
    <div className="App">
      <input type="text" onChange={getInputValue} />
      <button onClick={handleSubmit}>Submit</button>
      <button onClick = {handleDelete}>Delete</button>
      <div>
        {getMessage.status === 200 ? 
        <h3>{JSON.stringify(getMessage.data.message)}</h3>
        :
        <h3>LOADING</h3>}

      </div>
    </div>
  );
}

export default App;