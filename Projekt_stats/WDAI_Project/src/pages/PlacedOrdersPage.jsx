import {useEffect, useState} from "react";
import Order from "../components/Order.jsx";

function PlacedOrdersPage() {
    const token = localStorage.getItem("token");
    const [orders, setOrders] = useState([]);


    useEffect(() => {
        fetchOrders();
    }, []);

    const fetchOrders = async () => {
        try {
            const response = await fetch("http://localhost:5000/api/orders/userId", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                setOrders(data);
            }

        } catch (error) {
            console.error(error);
        }
    }

    return (
        <div>
            <ul>
                { orders.length > 0 ? orders.map((order, index) => (
                    <Order key={index} order={order} />
                )) : <h3>No orders placed</h3> }
            </ul>
        </div>
    );
}

export default PlacedOrdersPage;