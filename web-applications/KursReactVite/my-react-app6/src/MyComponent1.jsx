import React, {useState, useEffect} from "react";

function MyComponent1(){
    const [width, setWidth] = useState(window.innerWidth);
    const [height, setHeight] = useState(window.innerHeight);

    function handleResize(){
        setWidth(window.innerWidth);
        setHeight(window.innerHeight);
    }

    useEffect(() => {
        window.addEventListener("resize", handleResize);
        console.log("EVENT LISTENER ADDED");

        return () => {
            window.removeEventListener("resize", handleResize);
            console.log("EVENT LISTENER REMOVED");
        } //that invokes when Component unmounts
        //how to unmount? - change the route

    }, []); //[] only when Component mounts
    //}, [width, height]); //when Component mounts and when width or height changes
    // empty when Component mounts and unmounts (every re-render)

    useEffect(() => {
        document.title = `Size: ${width}x${height}`;
    }, [width, height]);

    return(<>
        <p>Window Width: {width}px</p>
        <p>Window Height: {height}px</p>
        </>);
}

export default MyComponent1