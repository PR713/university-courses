
// import Button from "./Button.jsx";
import Student from "./Student.jsx"

function App() {
    return(
        <>
            <Student name="Spongebob" age={30} isStudent={true}/>
            <Student name="Patrick" age={42} isStudent={false}/>
            <Student name="Squidward" age='30' isStudent={false}/>
            <Student name="Sandy" age={27} isStudent={true}/>
            <Student name="Radek"/>
        </>
    );
    // return(<Button/>);
}

export default App
