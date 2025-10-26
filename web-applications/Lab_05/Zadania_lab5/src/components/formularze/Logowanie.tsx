import {ChangeEvent, useState} from 'react';

function Logowanie() {

    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [nazwaUzytkownika, setNazwaUzytkownika] = useState('');

    function handlePasswordChange(event: ChangeEvent<HTMLInputElement>) {
        setPassword(event.target.value);
    }

    function handleConfirmPasswordChange(event: ChangeEvent<HTMLInputElement>) {
        setConfirmPassword(event.target.value);
    }


    function handleUsernameChange(event: ChangeEvent<HTMLInputElement>) {
        setNazwaUzytkownika(event.target.value);
    }

    const isButtonDisabled = !password || !confirmPassword || !nazwaUzytkownika;

    // useEffect(() => {
    //     if (!isButtonDisabled) {
    //         if (password === confirmPassword) {
    //             alert("Zalogowano poprawnie");
    //         } else {
    //             alert("Hasla nie są zgodne");
    //         }
    //     }
    // }, [password, confirmPassword, nazwaUzytkownika, isButtonDisabled]);
    //raczej o to nie chodziło w skrypcie... tylko o to, żeby sprawdzać czy
    // hasła są takie same po kliknięciu przycisku, niefunkcjonalne XD

    function handleLogin(){
        if (!isButtonDisabled && password === confirmPassword) {
            alert("Zalogowano poprawnie");
        } else {
            alert("Hasla nie są zgodne");
        }
    }

    return (
        <div>
            <label>Nazwa Użytkownika</label>
            <input type="text" id="username" name="Username" value={nazwaUzytkownika}
                   onChange={handleUsernameChange}/>
            <br/><br/>
            <label>Hasło</label>
            <input type="text" id="password" name="Hasło" value={password}
                   onChange={handlePasswordChange}/>
            <br/><br/>

            <label>Powtórz Hasło</label>
            <input type="text" id="repeatpassword" name="Powtórz Hasło" value={confirmPassword}
                   onChange={handleConfirmPasswordChange}/>
            <br/>
            <button id = "logowanie" disabled={isButtonDisabled} onClick={handleLogin}>Logowanie</button>
        </div>
    );
}

export default Logowanie;