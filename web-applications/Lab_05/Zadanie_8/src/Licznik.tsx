import {useEffect, useState} from "react";

function Licznik() {

    const [count, setCount] = useState(() => {
        const count = localStorage.getItem('count');
        return count ? parseInt(count, 10) : 0;
    });

    function handleIncrement() {
        setCount(c => c + 1);
    }

    useEffect(() => {
        localStorage.setItem('count', `${count}`);
    }, [count]);

    return (<div style={{marginLeft: '20px'}}>
        <p> Licznik: {count} </p>
        <button onClick={handleIncrement}>Dodaj</button>
    </div>);
}

export default Licznik;