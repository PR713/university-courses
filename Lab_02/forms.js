const emailForm = document.getElementById('emailform');
const emailInput = document.getElementById('email');
const emailErrorMessage = document.getElementById('email-error-message')
const messageTextArea = document.getElementById('message');
const errorTextArea = document.getElementById('text-error-message');
const subject = document.getElementById('subject');

const emailPattern = /^[^\s@]+@[^\s@]+\.[a-zA-z]{2,}$/;

function validateEmail() {
    const emailValue = emailInput.value.trim();

    if (emailValue === '') {
        emailErrorMessage.textContent = 'Proszę podać adres e-mail.'
        emailErrorMessage.style.display = 'block';
        emailInput.classList.add('invalid');
    } else if (!emailValue.includes('@')) {
        emailErrorMessage.textContent = 'Adres e-mail musi zawierać znak "@"';
        emailErrorMessage.style.display = 'block';
        emailInput.classList.add('invalid');
    } else if (emailValue.startsWith('@')) {
        emailErrorMessage.textContent = 'Adres e-mail nie może zaczynać się od "@"';
        emailErrorMessage.style.display = 'block';
        emailInput.classList.add('invalid');
    } else if (!emailValue.includes('.') || emailValue.split('@')[1].startsWith('.')){
        emailErrorMessage.textContent = 'Adres e-mail musi zawierać domenę po znaku "@" i przed "."';
        emailErrorMessage.style.display = 'block';
        emailInput.classList.add('invalid');
    } else if (!emailPattern.test(emailValue)) {
        emailErrorMessage.textContent = 'Proszę podać poprawny adres e-mail (np. example@domain.com).';
        emailErrorMessage.style.display = 'block';
        emailInput.classList.add('invalid');
    } else {
        emailErrorMessage.style.display = 'none';
        emailInput.classList.remove('invalid');
    }
}

function validateText() {
    if (messageTextArea.value === ''){
        errorTextArea.textContent = 'Proszę wprowadzić jakiś tekst';
        errorTextArea.style.display = 'block';
        messageTextArea.classList.add('invalid');
    } else if (subject.value === ''){
        errorTextArea.textContent = 'Proszę wybrać temat';
        errorTextArea.style.display = 'block';
        messageTextArea.classList.add('invalid');
    } else {
        errorTextArea.style.display = 'none';
        messageTextArea.classList.remove('invalid');
    }
}

emailInput.addEventListener('input', validateEmail);

emailForm.addEventListener('submit', function (event) {
    validateEmail();
    validateText();

    if (emailInput.classList.contains('invalid') || messageTextArea.classList.contains('invalid')) {
        event.preventDefault();
    }
});