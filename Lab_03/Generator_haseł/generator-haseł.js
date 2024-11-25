function generatePassword() {
    const minLength = parseInt(document.getElementById('minLength').value);
    const maxLength = parseInt(document.getElementById('maxLength').value);

    if (isNaN(minLength) || isNaN(maxLength)) {
        alert('Proszę podać minimalną i maksymalną długośc hasła!');
        return;
    }

    if (minLength > maxLength) {
        alert('Minimalna długość nie może być większa od maksymalnej!');
        return;
    }

    const length = Math.floor(Math.random() * (maxLength - minLength + 1)) + minLength;
    const lowercase = 'abcdefghijklmnopqrstuvwxyz';
    const digits = '0123456789';
    let allChars = lowercase + digits;

    const includeUppercase = document.getElementById('includeUpper').checked;
    const includeSpecial = document.getElementById('includeSpecial').checked;

    if (includeUppercase) {
        allChars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    }

    if (includeSpecial) {
        allChars += '!@#$%^&*()_+[]{}|;:,.<>?'
    }

    let password = '';
    let array = Array(allChars.length).fill(0);
    for (let i = 0; i <= length - 1; i++) { //random [0,1)
        const randomIndex = Math.floor(Math.random() * (allChars.length));
        password += allChars[randomIndex];
        array[randomIndex] += 1;
    }
    if (length > 2) {
        let flag = false;
        for (let j = 0; j <= allChars.length - 1; j++) {
            if (array[j] > (length - 1) / 3) {
                flag = true;
                break;
            }
        }
        if (flag === true) {
            generatePassword(); //zabezpieczenie przed zbyt trywialnym hasłem
            return;
        }
    }
    //document.getElementById('generatedPassword').value = password;
    alert(password)
}

document.getElementById('generateButton').addEventListener('click', generatePassword);


