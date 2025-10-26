
function Ternary(){

    let a: boolean = true;
    let b: boolean = false;

    return (
        <>
            {a ? <div>Stwierdzenie a jest prawdziwe</div> : <div>Stwierdzenie a jest fałszywe</div>}
            {b ? <div>Stwierdzenie b jest prawdziwe</div> : <div>Stwierdzenie b jest fałszywe</div>}
        </>
    );
}

export default Ternary;