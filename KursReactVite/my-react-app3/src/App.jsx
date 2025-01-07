import UserGreeting from "./UserGreeting.jsx";

function App(){
    return(
        <>
            <UserGreeting isLoggedIn={true} username="Radek"/>
            <br></br>
            <UserGreeting isLoggedIn={false} username="PoweR"/>
            <br></br>
            <UserGreeting isLoggedIn={true} />
        </>
    );
}

export default App









//50:00:00
//
// // import Button from "./Button.jsx";
// import Student from "./Student.jsx"
//
// function App() {
//     return(
//         <>
//             <Student name="Spongebob" age={30} isStudent={true}/>
//             <Student name="Patrick" age={42} isStudent={false}/>
//             <Student name="Squidward" age='30' isStudent={false}/>
//             <Student name="Sandy" age={27} isStudent={true}/>
//             <Student name="Radek"/>
//         </>
//     );
//     // return(<Button/>);
// }
//
// export default App
