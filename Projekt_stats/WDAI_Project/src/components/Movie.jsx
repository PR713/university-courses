import {useNavigate} from "react-router-dom";
import PropTypes from "prop-types";

function Movie({ movie }) {
    const navigate = useNavigate();

    const handleMovieClick = () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
        navigate(`/movies/${movie.id}`, { state: { movie } });
    };

    return (
        <div className="col-md-4 mb-4">
            <div className="card h-100" onClick={handleMovieClick} style={{ cursor: "pointer" }}>
                <img
                    src={movie.large_cover_image}
                    alt={movie.title_long}
                    className="card-img-top"
                    style={{
                        width: "100%",
                        height: "auto",
                    }}
                />
                <div className="card-body">
                    <h5 className="card-title">{movie.title_long}</h5>
                    <p className="card-text">
                        <strong>Rating:</strong> {movie.rating}
                    </p>

                    <p className="card-text d-flex">
                        {movie.genres?.[0] || "Genre not available"}
                    </p>

                    {/* Wyświetlanie ceny */}
                    <p className="card-text">
                        <strong>Price:</strong> {movie.price?.toFixed(2) || "N/A"} $
                    </p>
                </div>
            </div>
        </div>
    );
}

Movie.propTypes = {
    movie: PropTypes.shape({
        id: PropTypes.oneOfType([PropTypes.number]).isRequired,
        large_cover_image: PropTypes.string.isRequired,
        title_long: PropTypes.string.isRequired,
        rating: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
        genres: PropTypes.arrayOf(PropTypes.string),
        price: PropTypes.number, // Dodana właściwość `price`
    }).isRequired,
};

export default Movie;
