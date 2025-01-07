import {Link} from "react-router-dom";

function Home(){

    return (
        <div>
            <h1>Home</h1>
            <p>Witaj na stronie startowej! Przejdź do<Link to="/blog">bloga,</Link>żeby zobaczyć artykuły!</p>
        </div>
    );
}

export default Home;