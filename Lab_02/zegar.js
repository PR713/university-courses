function timer(){
    var dzisiaj = new Date();
    var dzien = dzisiaj.getDate();
    var miesiac = dzisiaj.getMonth();
    var rok = dzisiaj.getFullYear();

    var godzina = dzisiaj.getHours();
    if (godzina < 10) godzina = "0" + godzina

    var minuta = dzisiaj.getMinutes()
    if (minuta < 10) minuta = "0" + minuta

    var sekunda = dzisiaj.getSeconds();
    if (sekunda < 10) sekunda = "0" + sekunda

    const zegary = document.getElementsByClassName("zegar");
    for (let i = 0; i < zegary.length; i++) {
        zegary[i].innerHTML =
            dzien + "/" + miesiac + "/" + rok + " | " + godzina + ":" + minuta + ":" + sekunda;
        setTimeout("timer()", 1000);
    }
}
