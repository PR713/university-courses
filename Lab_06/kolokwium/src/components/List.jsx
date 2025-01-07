import Square from "./Square.jsx";
import {useEffect, useState} from "react";
import Rectangle from "./Rectangle.jsx";
import Circle from "./Circle.jsx";
import {useNavigate} from "react-router-dom";
import {v4 as uuidv4} from "uuid";

function List() {
    const initialList = [
        {id: uuidv4(), type: "square"},
        {id: uuidv4(), type: "rectangle"},
        {id: uuidv4(), type: "circle"},
    ];


    const [list, setList] = useState(() => {
        const storedList = localStorage.getItem("list");
        return storedList ? JSON.parse(storedList) : initialList;
    });
    const [filter, setFilter] = useState("all");
    const navigate = useNavigate();


    useEffect(() => {
        localStorage.setItem("list", JSON.stringify(list));
    }, [list]);


    useEffect(() => {
        const timeout = setTimeout(() => {
            const elements = document.querySelectorAll(".square, .rectangle, .circle");
            elements.forEach((el) => {
                el.style.transition = "transform 0.5s ease";
                el.style.transform = "scale(0.5)";
                setTimeout(() => {
                    el.style.transform = "scale(1)";
                }, 500);
            });
        }, 1000); //po 1 s

        return () => clearTimeout(timeout);
    });


    function handleDeleteShape(index) {
        setList(list.filter((shape) => shape.id !== index));
    }


    function handleAddShape(type) {
        setList([...list, { id: uuidv4(), type }]);
    }


    const filteredList = filter === "all"
        ? list : list.filter((shape) => shape.type === filter);

    //wszystko git, jeśli dodamy/usuniemy to list (stan) się aktualizuje więc
    //ponownie się komponent renderuje i dzięki temu też filteredList się aktualizuje,
    // a useEffect na zmianę [list] aktualizuje localStorage
    // ale co jeśli zmienimy filter? filteredList się zmienia, ale useEffect nie zadziała
    // więc localStorage się nie zaktualizuje i po powrocie z detali do listy
    // znowu zobaczymy wszystkie elementy bez aktywnego filtra, trzeba by
    // dodać drugi useEffect na zmianę [filter] i tam zaktualizować localStorage
    // na filteredList ale znów, to nie jest najlepsze rozwiązanie, bo
    // jeśli potem chcemy wrócić do all to wetnie nam poprzednie elementy
    // bo przy renederowaniu komponentu List, list jest aktualizowany na wartość
    // z localStorage więc trzeba by nowe pole "listFiltered" w localStorage i jakoś
    // to zarządzać w zależności od filtra wybierać "list" lub pole "filtered",
    // więc najlepiej przetrzymywać po prostu dodatkowo wartość filter oprócz pola "list" w
    // localStorage i przy renderowaniu komponentu List, ustawić wartość filter
    // a nie defaultowo na "all" podobnie jak ustawianie useState dla list jeśli istnieje wartość
    // zapisana w localStorage... 
    //
    // I lepiej ID robić za pomocą uuid bo jeśli usuniemy element to
    // id może się powtórzyć i będą głupoty, teoretycznie i tak mogą się powtórzyć
    // bo uuid jest generowane nie w 100% unikalnie, najlepiej przechowywać np najwyższy
    // id w localStorage i przy dodawaniu nowego elementu zwiększać o 1

    return (
        <>
            <div className="list">
                <button onClick={() => handleAddShape("square")}>Dodaj kwadrat</button>
                <button onClick={() => handleAddShape("rectangle")}>Dodaj prostokąt</button>
                <button onClick={() => handleAddShape("circle")}>Dodaj koło</button>
                <button onClick={() => {
                    setList(initialList)
                }}>Reset
                </button>
                <select
                    value={filter}
                    onChange={(e) => setFilter(e.target.value)}
                >
                    <option value="all">Wszystko</option>
                    <option value="square">Kwadrat</option>
                    <option value="rectangle">Prostokąt</option>
                    <option value="circle">Koło</option>
                </select>
            </div>
            <div className="list">
                {filteredList.map((shape) => (
                    <div>
                        <div key={shape.id} onClick={() =>
                            navigate(`/shape/${shape.id}`)}>

                            {shape.type === "square" && <Square/>}
                            {shape.type === "rectangle" && <Rectangle/>}
                            {shape.type === "circle" && <Circle/>}
                        </div>
                        <button className="delete-button" onClick={() => handleDeleteShape(shape.id)}>usuń</button>
                    </div>
                ))}
            </div>
        </>
    );
}

export default List;
