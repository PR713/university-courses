import PropTypes from "prop-types";
import {useNavigate} from "react-router-dom";

function Order({ order }) {

    const navigate = useNavigate();

    const handleMovieClick = (movie) => {
        window.scrollTo({ top: 0, behavior: "smooth" });
        navigate(`/movies/${movie.id}`, { state: { movie } });
    };

    const pasteIconPayment = order.paymentMethod === 'paypal' ? " 📦" : order.paymentMethod === 'credit_card' ? " 💳" :" 📲";

    return (
        <div className="container py-4">
            <div className="card shadow-sm">
                <div className="card-header">
                    <h4 className="mb-0 bold">Order Details nr {order.id}</h4>
                </div>
                <div className="card-body">
                    <div className="row">
                        <div className="col-md-6">
                            <p><strong>Address:</strong> {order.address}</p>
                            <p><strong>Payment Method: </strong>{order.paymentMethod}{pasteIconPayment}</p>
                            <p><strong>Date: </strong> {order.date}</p>
                            <p><strong>Total Price: </strong> {order.totalPrice.toFixed(2)}$</p>
                            <p><strong>Status: </strong>
                                <span className={`badge ${order.status === 'Completed' ? 'bg-success' : order.status === 'Pending' ? 'bg-warning' : 'bg-danger'}`}>
                                    {order.status}
                                </span>
                            </p>
                        </div>
                    </div>

                    <div className="mt-4">
                        <h4>Cart Items:</h4>
                        <ul className="list-group">
                            {JSON.parse(order.cartItems).map((item, index) => (
                                <li key={index} className="list-group-item" onClick={() => handleMovieClick(item)}
                                        style={{ cursor: "pointer" }}>
                                    <img
                                        src={item.medium_cover_image}
                                        alt={item.title_long}
                                        style={{
                                            width: "70px",
                                            height: "auto",
                                            marginRight: "10px",
                                        }}/>
                                    <strong>{item.title_long}</strong>
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
}

Order.propTypes = {
    order: PropTypes.shape({
        id: PropTypes.number.isRequired,
        userId: PropTypes.number.isRequired,
        address: PropTypes.string.isRequired,
        paymentMethod: PropTypes.string.isRequired,
        date: PropTypes.string.isRequired,
        totalPrice: PropTypes.number.isRequired,
        status: PropTypes.string.isRequired,
        cartItems: PropTypes.string.isRequired,
    }).isRequired,
};


export default Order;


