import {useState} from "react";


function Licznik(){

    const [count, setCount] = useState(0);

    function handleIncrement(){
        setCount(c => c + 1);
    }


    return(<div>
        <p> Licznik: {count} </p>
        <button onClick={handleIncrement}>Dodaj</button>
    </div>);
}

export default Licznik;