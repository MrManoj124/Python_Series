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

  
}