import {useEffect, useRef, useState} from "react";

function Odliczanie() {

    const [time, setTime] = useState(15);
    const [isDisabled, setIsDisabled] = useState(false);
    const [startStop, setStartStop] = useState("Start");
    const intervalID = useRef(0);

    useEffect(() => {
        if (startStop === "Stop") {
            intervalID.current = setInterval(() => {
                setTime( tprev => {
                    const newTime = Math.floor(10*tprev - 1)/10;
                    if (newTime === 0) {
                        setIsDisabled(true);
                        clearInterval(intervalID.current);
                        return 0;
                    }
                    return newTime;
                });
               // setTime( newTime); tak nie można bo potem setTime nie ma dostępu do time z poprzedniego rendera
                // i aktualizuje się po wciśnięciu przycisku start i stop bo jeszcze nie zdążył się zaktualizować
            }, 100);
        }

        return () => clearInterval(intervalID.current);
    }, [startStop]);


    function handleStartStop() {
        if (startStop === "Start") {
            setStartStop("Stop");
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

export default Odliczanie