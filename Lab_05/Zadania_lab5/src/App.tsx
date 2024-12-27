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
//5
import Studenci from "./components/studenci/Studenci.tsx";
import StudentManager from "./components/studenci/StudentManager.tsx";
//6
import Licznik6 from "./components/efekty/Licznik6.tsx"
import Tytul from "./components/efekty/Tytul.tsx";
import Odliczanie from "./components/efekty/Odliczanie.tsx";
import Komentarz from "./components/produkty/Komentarz.tsx";
import Odliczanie2 from "./components/efekty/Odliczanie2.tsx";
import Odliczanie3 from "./components/efekty/Odliczanie3-bezRef.tsx";
import Odliczanie3BezRef from "./components/efekty/Odliczanie3-bezRef.tsx";

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
            {/*6.1*/}
            <Licznik6/>
            <br/><br/><br/>
            {/*6.2*/}
            <Tytul/>
            <br/><br/><br/>
            {/*6.3*/}
            <Odliczanie/>
            <Odliczanie2/>
            <Odliczanie3BezRef/>
            <br/><br/><br/>
            {/*7.1*/}
            <Komentarz id={10} body={'Film zaskakuje wciągającą fabułą i znakomitą grą aktorską, która trzyma w napięciu od początku do końca. Mimo kilku przewidywalnych momentów, całość pozostawia pozytywne wrażenie dzięki świetnemu obrazowi i emocjonalnej głębi.'}
                       postId={111} likes={20} user={{id: 4, username: "Radek", fullName:"Kedar" }}/>
            <br/><br/><br/>
        </div>
    );
}

export default App
