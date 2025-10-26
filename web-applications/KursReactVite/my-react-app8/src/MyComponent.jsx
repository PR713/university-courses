import React, { useState, useEffect, useRef } from 'react';

function MyComponent(){

    //let [number, setNumber] = useState(0);
    const inputRef1 = useRef(null);
    const inputRef2 = useRef(null);
    const inputRef3 = useRef(null);
    //useRef return an object with a property called current
    //this property can be used to store any value
    //and it won't be affected by re-renders

    useEffect(() => {
        console.log("Component Rendered");
    });

    function handleClick1(){
        //setNumber(n => n + 1);
        //ref.current++;
        //console.log(ref.current);
        inputRef1.current.focus();
        inputRef1.current.style.backgroundColor = "yellow";
        inputRef2.current.style.backgroundColor = "";
        inputRef3.current.style.backgroundColor = "";
    }

    function handleClick2(){
        inputRef2.current.focus();
        inputRef1.current.style.backgroundColor = "";
        inputRef2.current.style.backgroundColor = "yellow";
        inputRef3.current.style.backgroundColor = "";
    }

    function handleClick3(){
        inputRef3.current.focus();
        inputRef3.current.style.backgroundColor = "yellow";
        inputRef1.current.style.backgroundColor = "";
        inputRef2.current.style.backgroundColor = "";
    }

    return(<div>
        <button onClick={handleClick1}>
            Click me1!
        </button>
        <input ref={inputRef1}/>

        <button onClick={handleClick2}>
            Click me2!
        </button>
        <input ref={inputRef2}/>

        <button onClick={handleClick3}>
            Click me3!
        </button>
        <input ref={inputRef3}/>
    </div>);

}

export default MyComponent;