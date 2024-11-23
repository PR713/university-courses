const canvas = document.getElementById('gameCanvas');
const context = canvas.getContext('2d');

let score = 0;
let lives = 3;
let zombies = [];
let gameOver = false;
let mouseX = 0;
let mouseY = 0;

const aimImage = new Image();
aimImage.src = 'aim.png';

const zombieImage = new Image();
zombieImage.src = 'walkingdead.png';

const numberOfFrames = 10;
const frameRate = 150;
let currentFrame = 0;

const heartFull = new Image();
heartFull.src = 'full_heart.png';

const heartEmpty = new Image();
heartEmpty.src = 'empty_heart.png';

const sadMusic = new Audio('sad-music.mp3');
sadMusic.loop = true;

function start() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    sadMusic.pause();
    sadMusic.currentTime = 0;
    score = 0;
    lives = 3;
    zombies = [];
    gameOver = false;
    spawnZombie();
    gameLoop();
}


canvas.addEventListener('mousemove', (event ) => {
    mouseX = event.clientX;
    mouseY = event.clientY;
});


setInterval(() => {
    currentFrame = (currentFrame + 1) % numberOfFrames;
}, frameRate);


function draw() {
    context.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < 3; i++) {
        if (i < lives) {
            context.drawImage(heartFull, 20 + i * 80, 20, 60, 45);
        } else {
            context.drawImage(heartEmpty, 20 + i * 80, 20, 60, 45);
        }
    }

    context.fillStyle = '#FFF';
    context.font = '40px Arial';
    const formattedScore = String(score).padStart(5, '0');
    context.fillText(formattedScore, canvas.width - 150, 55);

    zombies.forEach(zombie => {
        const frameWidth = zombieImage.width / numberOfFrames;
        const frameHeight = zombieImage.height;
        const frameX = currentFrame * frameWidth;
        context.drawImage(
            zombieImage,
            frameX, 0,
            frameWidth, frameHeight,
            zombie.x, zombie.y,
            zombie.width, zombie.height
        );
    })
    const aimSize = 140;
    context.drawImage(aimImage, mouseX - aimSize / 2, mouseY - aimSize / 2, aimSize, aimSize);
}


function update() {
    if (gameOver) return;
    zombies.forEach((zombie, index) => {
        zombie.x -= zombie.speed;

        if (zombie.x + zombie.width < 0) {
            zombies.splice(index, 1);
            lives--;
            if (lives === 0) {
                context.drawImage(heartEmpty, 20, 20, 70, 50);
                endGame();
            }
        }
    })
}


function spawnZombie() {
    if (gameOver) return;

    const width = Math.random() * 60 + 40;
    const height = 1.5*width;

    const zombie = {
        x: window.innerWidth,
        y: 2/7 *canvas.height + Math.random() * 3.7/7 * canvas.height,
        width: width,
        height: height,
        speed: Math.random() * 10 + 3,
    };
    zombies.push(zombie);
    setTimeout(spawnZombie, Math.random() * 400 + 500);
}


function gameLoop() {
    draw();
    update();
    if (!gameOver) {
        requestAnimationFrame(gameLoop)
    }
}


function endGame() {
    gameOver = true;
    sadMusic.play();
    canvas.style.cursor = 'default';

    document.getElementById('gameOver').style.display = 'block';
    document.getElementById('finalScore').textContent = score;


}


canvas.addEventListener('click', (event) => {
    if (gameOver) return;

    const mouseX = event.clientX;
    const mouseY = event.clientY;
    let hit = false;

    zombies.forEach((zombie, index) => {
        if (
            mouseX >= (zombie.x-15) &&
            mouseX <= (zombie.x + zombie.width + 15) &&
            mouseY >= (zombie.y -15) &&
            mouseY <= zombie.y + zombie.height + 15
        ) {
            zombies.splice(index, 1);
            score += 20;
            hit = true; /*Można kilka na raz*/
        }
    });

    if (!hit && score >= 5) {
        score -= 5;
    }
})


document.getElementById('restartButton').addEventListener('click', () => {
    document.getElementById('gameOver').style.display = 'none';
    start();
});


window.onload = start;