import {ChangeEvent, useEffect, useState} from "react";


function Tytul() {

    const [tytul, setTytul] = useState('');

    function tytulHandle(e: ChangeEvent<HTMLInputElement>){
        setTytul(e.target.value);
    }

    useEffect(() => {
        document.title = `${tytul}`;
    },[tytul]);

    return (<>
        <input type="text"
               name="tytul"
               onChange={(e) => tytulHandle(e)}/>
    </>);
}

export default Tytul