import {useState} from "react";


interface Student {
    imie: string;
    nazwisko: string;
    rocznik: number;
}

interface DodawanieProps {
    addStudent: (student: Student) => void;
}

function Dodawanie({addStudent}: DodawanieProps) {

    const [imie, setImie] = useState('');
    const [nazwisko, setNazwisko] = useState('');
    const [rocznik, setRocznik] = useState('');

    function handleClickButton() {
        if (imie === '' || nazwisko === '' || rocznik === '') {
            alert("Wszystkie pola muszą być wypełnione!");

        } else if (!isNaN(parseInt(rocznik)) && parseInt(rocznik) > 0) {
            addStudent({imie: imie, nazwisko: nazwisko, rocznik: parseInt(rocznik)});
            setImie('');
            setNazwisko('');
            setRocznik('');

        } else {
            alert("Rocznik musi być dodatnią liczbą!");
        }
    }

    return (<>
        <label>Imię:</label>
        <input type="text" id="imie" value={imie} onChange={(e) => setImie(e.target.value)}/>
        <br/>
        <label>Nazwisko:</label>
        <input type="text" id="nazwisko" value={nazwisko} onChange={(e) => setNazwisko(e.target.value)}/>
        <br/>
        <label>Rocznik:</label>
        <input type="text" id="rocznik" value={rocznik} onChange={(e) => setRocznik(e.target.value)}/>
        <br/>
        <button onClick={handleClickButton}>Dodaj</button>
    </>);
}

export default Dodawanie;