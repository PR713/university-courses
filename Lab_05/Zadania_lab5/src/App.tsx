import './App.css';
//1
import Koszyk from "./components/koszyk/Koszyk.tsx";
import Produkt from "./components/koszyk/Produkt.tsx";
import NowyKoszyk from "./components/koszyk/NowyKoszyk.tsx";
//2
import Licznik from "./components/liczniki/Licznik.tsx";
import NowyLicznik from "./components/liczniki/NowyLicznik.tsx";
//3
import Formularz from "./components/formularze/Formularz.tsx";
import Haslo from "./components/formularze/Haslo.tsx";
import Logowanie from "./components/formularze/Logowanie.tsx";
//4
import Ternary from "./components/inne/Ternary.tsx";


import Aktualizacja from "./components/inne/Aktualizacja.tsx";
import Studenci from "./components/studenci/Studenci.tsx";
import StudentManager from "./components/studenci/StudentManager.tsx";

function App() {
    return (
        <div>
            {/*1.1*/}
            <Koszyk>
                <Produkt name='apple'/>
                <Produkt name='pear'/>
                <Produkt name='banana'/>
                <Produkt name='ananas'/>
                <Produkt name='grape'/>
            </Koszyk>
            <br/><br/><br/>
            {/*1.2*/}
            <NowyKoszyk/>
            <br/><br/><br/>


            {/*2.1*/}
            <Licznik/>
            <br/><br/><br/>
            {/*2.2*/}
            <NowyLicznik/>
            <br/><br/><br/>

            {/*3.1*/}
            <Formularz/>
            <br/><br/><br/>
            {/*3.2*/}
            <Haslo/>
            <br/><br/><br/>
            {/*3.3*/}
            <Logowanie/>
            <br/><br/><br/>

            {/*4.1*/}
            <Ternary/>
            <br/><br/><br/>
            {/*4.2*/}
            <Aktualizacja/>
            <br/><br/><br/>

            {/*5.1*/}
            <Studenci/>
            <br/><br/><br/>
            {/*5.2*/}
            <StudentManager/>
            <br/><br/><br/>
        </div>
    );
}

export default App
