
function Przycisk(props : {fun : () => void}){

    return (
        <button onClick={props.fun}>Dodaj</button>
    );
}

export default Przycisk;