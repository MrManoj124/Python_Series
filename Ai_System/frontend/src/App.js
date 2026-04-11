import { useState } from  "react";
import axios from "axios";

function App(){
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");

  const calculate = async () => {
    try{
      const res = await axios.post("http://127.0.0.1:8000/calculate",{
        expr: input,
      });
      setResult(res.data.result);
    }
    catch{
      setResult("Error");
    }
  };
  
  const chat = async () => {
    const res = await axios.post("http://127.0.0.1:8000/chat",{
      expr : input,
    });
    setResult(res.data.response);
  }

  //Add Voice input
  const startVoice = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.onresult= (event) => {
      setInput(event.results[0][0].transcript);
    };
    recognition.start();
  };

  const speak = (text) => {
    const speech = new SpeechSynthesisUtterance(text);
    
  }
  return (
    <div style = {{ textAlign: "center", marginTop : "50px"}}>
      <h1>Smart Calculator</h1>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter Expression"
      />
      <br/> <br/>
      <button onClick={calculate}>Calculate</button>
      <button onClick={startVoice}>VoiceInput</button>
       <h2>Result:{result}</h2>
      </div>
  );
}

export default App;