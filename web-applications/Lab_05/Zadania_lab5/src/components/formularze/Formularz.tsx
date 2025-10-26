import {ChangeEvent, useState} from "react";

function Formularz() {

    const [text, setText] = useState("");

    function handleText(event: ChangeEvent<HTMLInputElement>) {
        setText(event.target.value);
    }

    return (
        <>
                <input type="text" value={text} onChange={handleText}
                    placeholder="Napisz coś :P"/>
                <div>{text}</div>
        </>
    );
}

export default Formularz;