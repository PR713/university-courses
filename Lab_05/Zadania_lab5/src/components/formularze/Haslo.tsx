import {ChangeEvent, useState} from 'react';

function Haslo(){
    
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    
    function handlePasswordChange(event: ChangeEvent<HTMLInputElement>) {
        setPassword(event.target.value);
    }

    function handleConfirmPasswordChange(event: ChangeEvent<HTMLInputElement>) {
        setConfirmPassword(event.target.value);
    }

    let message = "";
    if(password === "" && confirmPassword === ""){
        message = "Proszę wprowadzić hasło";
    } else if(password !== confirmPassword){
        message = "Hasła nie są zgodne";
    }

    return (
        <div>
            <label>Hasło</label>
            <input type="text" id="password" name="Hasło" value={password}
                   onChange={handlePasswordChange}/>
            <br/>
            <br/>
            <label>Powtórz Hasło</label>
            <input type="text" name="Powtórz Hasło" value={confirmPassword}
                   onChange={handleConfirmPasswordChange} />
            
            <div>{message}</div>
        </div>
    );
}

export default Haslo;