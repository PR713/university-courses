let timeInSeconds = 0;
let timerInterval = null;

function formatTime(seconds) {
    if (seconds < 60) {
        return `${seconds}s`;
    }
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}min ${remainingSeconds}s`;
}

function updateTimeDisplay() {
    const timeDisplay = document.getElementById('display');
    timeDisplay.textContent = formatTime(timeInSeconds)
}

function startTimer() {
    if (timerInterval === null) {
        timerInterval = setInterval(() => {
            timeInSeconds++;
            updateTimeDisplay();
        }, 1000);
    }
}

function stopTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
}

function resetTimer() {
    stopTimer();
    timeInSeconds = 0;
    updateTimeDisplay();
}

document.getElementById('start').addEventListener('click', startTimer);
document.getElementById('stop').addEventListener('click', stopTimer);
document.getElementById('reset').addEventListener('click', resetTimer);