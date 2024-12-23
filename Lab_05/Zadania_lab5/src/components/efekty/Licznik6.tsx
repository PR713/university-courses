import {useEffect, useState} from "react";


function Licznik6() {

    const [count, setCount] = useState(0);

    useEffect(() => {
        console.log("Hello world");
    }, []);

    // useEffect(() => {
    //     console.log(`Licznik zwiększył się do ${count}`);
    // }, [count]);

    function handleIncrement() {
        setCount(c => c + 1);
        console.log(`Licznik zwiększył się do ${count + 1}`);
    }


    return (<div>
        <p> Licznik: {count} </p>
        <button onClick={handleIncrement}>Dodaj</button>
    </div>);
}

export default Licznik6;