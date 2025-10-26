import {useEffect, useRef, useState} from "react";
//wersja elegancka, z new Date()

function Odliczanie2() {

    const [time, setTime] = useState(15);
    const [isDisabled, setIsDisabled] = useState(false);
    const [startStop, setStartStop] = useState("Start");
    const intervalIdRef = useRef<NodeJS.Timeout | null>(null);
    const startTimeRef = useRef<number>(0);

    useEffect(() => {
        if (startStop === "Stop") {
            intervalIdRef.current = setInterval(() => {
                const remainingTime = (startTimeRef.current - Date.now()) / 1000;
                setTime(Math.max(remainingTime, 0));
                if (remainingTime <= 0) {
                    setIsDisabled(true);
                    clearInterval(intervalIdRef.current);
                }
            }, 100);
        }

        return () => clearInterval(intervalIdRef.current);
    }, [startStop]);


    function handleStartStop() {
        if (startStop === "Start") {
            setStartStop("Stop");
            startTimeRef.current = Date.now() + time * 1000;
        } else {
            setStartStop("Start")
        }
    }

    return (<>
        <div>
            Licznik: {time.toFixed(1)}
        </div>
        <button disabled={isDisabled} onClick={handleStartStop}>{startStop}</button>
    </>);
}

export default Odliczanie2