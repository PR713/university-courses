
import {useState} from "react";
import Przycisk from "./Przycisk.tsx";


function NowyLicznik(){

    const [count, setCount] = useState(0);

    function handleIncrement(){
        setCount(c => c + 1);
    }


    return(<div>
        <p> Licznik: {count} </p>
        <Przycisk fun = {handleIncrement}/>
    </div>);
}

export default NowyLicznik;