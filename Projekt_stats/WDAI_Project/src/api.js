const API_URL = 'http://localhost:5000/api';

export const fetchUsers = async () => {
    const response = await fetch(`${API_URL}/users`);
    return await response.json();
};

//analogicznie możn filmy z backendu i zamówienia