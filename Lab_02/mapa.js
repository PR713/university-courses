//Inicjalizacja mapy
const map = L.map('map').setView([0,0], 5); //Współrzędne, poziom powiększenia
const bounds = [[40.0, 36.0], [56.0, -10.0]]
//Dodanie warstwy z mapą
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    minZoom: 4,
    attribution: '© OpenStreetMap'
}).addTo(map);
map.setMaxBounds(bounds);

const places = [
    { name: "Brela", coords: [43.37, 16.93] },
    { name: "Makarska", coords: [43.2967, 17.0178] },
    { name: "Dubrovnik", coords: [42.6507, 18.0944] },
    { name: "Mostar", coords: [43.3438, 17.8078] },
    { name: "Medjugorje", coords: [43.1889, 17.6774] },
    { name: "Wodospady Kravica", coords: [43.1562, 17.6094] },
    { name: "Plitwickie Jeziora", coords: [44.8802, 15.6168] },
    { name: "Paryż", coords: [48.8566, 2.3522] },
    { name: "Wersal", coords: [48.8049, 2.1204] },
    { name: "Tatry", coords: [49.2772, 20.0498] },
    { name: 'Gdańsk', coords: [54.3520, 18.6466]},
    { name: 'Wrocław' ,coords: [51.1079, 17.0385]}];

//znaczniki dla każdego miejsca
places.forEach(place => {
    const marker = L.marker(place.coords).addTo(map);
    marker.bindPopup(place.name);
});