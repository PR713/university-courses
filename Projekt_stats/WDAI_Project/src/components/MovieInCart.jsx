import PropTypes from "prop-types";
import { useNavigate } from "react-router-dom";

function MovieInCart({ movie, onRemove }) {
    const navigate = useNavigate();



    const handleMovieClick = () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
        navigate(`/movies/${movie.id}`, { state: { movie } });
    };

    const handleRemoveClick = (e) => {
        e.stopPropagation();
        onRemove();
    };

    return (
        <div
            className="card h-100"
            onClick={handleMovieClick}
            style={{ cursor: "pointer" }}
        >
            <img
                src={movie.medium_cover_image}
                alt={movie.title_long}
                className="card-img-top"
                style={{ width: "100%", height: "400px", objectFit: "cover" }}
            />
            <div className="card-body p-3 d-flex flex-column flex-grow-1">
                <div className="flex-grow-1">
                    <h5 className="card-title mb-3">{movie.title_long}</h5>
                    <div className="text-start"> {/* Wyrównanie tekstu do lewej */}
                        <p className="card-text mb-1">
                            <span className="fw-medium">Rating:</span> {movie.rating}
                        </p>
                        <p className="card-text mb-1">
                            <span className="fw-medium">Director:</span>{" "}
                            {movie.Director || "Unknown"}
                        </p>
                        <p className="card-text mb-3">
                            <span className="fw-medium">Price:</span>{" "}
                            {movie.price?.toFixed(2) || "N/A"} $
                        </p>
                    </div>
                </div>

                <div className="d-flex justify-content-center">
                    <button
                        className="btn btn-danger btn-sm"
                        onClick={handleRemoveClick}
                    >
                        Remove from Cart
                    </button>
                </div>
            </div>
        </div>
    );
}

MovieInCart.propTypes = {
    movie: PropTypes.shape({
        id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
        medium_cover_image: PropTypes.string.isRequired,
        title_long: PropTypes.string.isRequired,
        rating: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
        genres: PropTypes.arrayOf(PropTypes.string),
        Director: PropTypes.string,
        price: PropTypes.number,
    }).isRequired,
    onRemove: PropTypes.func.isRequired,
};

export default MovieInCart;