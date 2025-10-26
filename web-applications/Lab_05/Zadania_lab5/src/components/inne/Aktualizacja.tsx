import {useState} from "react";

function Aktualizacja(){

    const [produkt, setProdukt] = useState({nazwa: "Pomidor", cena:50});

    function handleDetails(){
        setProdukt(p => ( {...p, cena: 100}));
    }

    return(
        <div>
            <div>Aktualnie {produkt.nazwa} kosztuje {produkt.cena}</div>
            <button onClick={handleDetails}>Zmień cenę</button>
        </div>
    )
}

export default Aktualizacja;