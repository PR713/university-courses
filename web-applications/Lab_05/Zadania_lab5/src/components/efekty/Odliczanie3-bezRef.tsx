import {useEffect, useState} from "react";
//wersja z new Date() ale bez useRef

function Odliczanie3() {

    const [time, setTime] = useState(15);
    const [isDisabled, setIsDisabled] = useState(false);
    const [startStop, setStartStop] = useState("Start");
    const [intervalId, setIntervalId] = useState<number | null>(null);
    const [startTime, setStartTime] = useState<number>(0);

    useEffect(() => {
        if (startStop === "Stop") {
            const newIntervalId = setInterval(() => {
                const remainingTime = (startTime - Date.now()) / 1000;
                setTime(Math.max(remainingTime, 0));
                if (remainingTime <= 0) {
                    setIsDisabled(true);
                    clearInterval(newIntervalId);
                    setIntervalId(null);
                }
            }, 100);
            setIntervalId(newIntervalId);
        } else if (intervalId) {
            // Zatrzymanie interwału gdy kliknięto Stop
            clearInterval(intervalId);
            setIntervalId(null);
        }

        return () => { // to się wykonuje dopiero przed kolejnym renderem
            if (intervalId) {
                clearInterval(intervalId);
            }
        }
    }, [startStop]);



    function handleStartStop() {
        if (startStop === "Start") {
            setStartStop("Stop");
            setStartTime(Date.now() + time * 1000);
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

export default Odliczanie3