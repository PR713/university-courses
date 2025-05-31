import { useLocation, useNavigate, useOutletContext } from "react-router-dom";
import Opinion from "../components/Opinion.jsx";
import AddOpinionForm from "../components/AddOpinionForm.jsx";
import { useEffect, useState } from "react";


function MovieDetailsPage() {
    const location = useLocation();
    const navigate = useNavigate();
    const [isInCart, setIsInCart] = useState(false);
    const [opinions, setOpinions] = useState([]);
    const movie = location.state?.movie;
    const token = localStorage.getItem("token");
    const { updateCartTotalPrice } = useOutletContext(); // Odbieramy funkcję z kontekstu
    const [averageRating, setAverageRating] = useState('');
    const [currentUserId, setCurrentUserId] = useState(null);
    const [isAdmin, setIsAdmin] = useState('user');



    if (!movie) {
        return (
            <div>
                <p>No movie data available.</p>
                <button onClick={() => navigate(-1)}>Go Back</button>
            </div>
        );
    }

    useEffect(() => {
        // Sprawdź, czy token jest obecny w localStorage
        if (token) {
            // Sprawdzenie userId na podstawie tokenu
            const fetchUserData = async () => {
                try {
                    const response = await fetch("http://localhost:5000/api/auth/user", {
                        headers: {
                            Authorization: `Bearer ${token}`,
                        },
                    });

                    if (response.ok) {
                        const userData = await response.json();
                        setCurrentUserId(userData.id);
                        setIsAdmin(userData.role);// Zakładając, że backend zwraca userId
                    } else {
                        console.error("Error fetching user data:", response.statusText);
                    }
                } catch (error) {
                    console.error("Error fetching user data:", error);
                }
            };

            fetchUserData();
        }
    }, []);//rendering only once when component is mounted



    useEffect(() => {
        // Sprawdź, czy film jest już w koszyku użytkownika
        const checkIfMovieIsInCart = async () => {
            try {
                const response = await fetch("http://localhost:5000/api/cart", {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                });

                if (response.ok) {
                    const cartItems = await response.json();

                    const isAlreadyInCart = cartItems.some((item) => item.id === movie.id);
                    setIsInCart(isAlreadyInCart);
                } else {
                    console.error("Error fetching cart items:", response.statusText);
                }
            } catch (error) {
                console.error("Error checking cart:", error);
            }
        };

        if (token) {
            checkIfMovieIsInCart();
        }
    }, []);//rendering only once when component is mounted


    const fetchOpinions = async () => {
        try {
            const response = await fetch(`http://localhost:5000/api/reviews/${movie.id}`);
            const data = await response.json();
            if (response.ok) {
                setOpinions(data);
                if (data.length > 0) {
                    const totalRating = data.reduce((sum, review) => sum + review.rating, 0);
                    const average = totalRating / data.length;
                    setAverageRating(average.toFixed(2));
                } else {
                    setAverageRating('');
                }
            } else {
                console.error("Error fetching opinions:", data.error);
            }
        } catch (error) {
            console.error("Error fetching opinions:", error);
        }
    };


    useEffect(() => {
        fetchOpinions();
    }, [movie.id]);




    const addOpinion = async (newOpinion) => {
        try {
            const response = await fetch("http://localhost:5000/api/reviews", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify(newOpinion),
            });

            const data = await response.json();
            if (response.ok) {
                setOpinions((prevOpinions) => [...prevOpinions, data]); // Dodaj nową opinię do stanu
                fetchOpinions(); // Pobierz opinie ponownie, aby zaktualizować średnią ocenę
            } else {
                alert("Error: " + data.error);
            }
        } catch (error) {
            console.error("Error submitting opinion:", error);
            alert("There was an error submitting your opinion.");
        }
    };

    const editOpinion = async (id, updatedOpinion) => {
        try {
            const response = await fetch(`http://localhost:5000/api/reviews/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify(updatedOpinion),
            });

            if (response.ok) {
                setOpinions((prevOpinions) =>
                    prevOpinions.map((opinion) =>
                        opinion.id === id ? { ...opinion, ...updatedOpinion } : opinion
                    )
                );
                fetchOpinions();
            } else {
                const error = await response.json();
                alert('Error: ' + error.message);
            }
        } catch (err) {
            console.error('Error updating opinion:', err);
            alert('There was an error updating the opinion.');
        }
    };

    const deleteOpinion = async (id) => {
        try {
            const response = await fetch(`http://localhost:5000/api/reviews/${id}`, {
                method: 'DELETE',
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            if (response.ok) {
                setOpinions((prevOpinions) => prevOpinions.filter((opinion) => opinion.id !== id));
                fetchOpinions();
            } else {
                const error = await response.json();
                alert('Error: ' + error.message);
            }
        } catch (err) {
            console.error('Error deleting opinion:', err);
            alert('There was an error deleting the opinion.');
        }
    };

    const handleAddToCart = async () => {
        if (!token) {
            alert("Please log in to add movies to your cart.");
            navigate("/login");
            return;
        }

        try {

            const response = await fetch("http://localhost:5000/api/cart", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({ movie: movie }),
            });

            if (response.ok) {
                setIsInCart(true);
                updateCartTotalPrice(); // Aktualizacja sumy cen po dodaniu filmu
            } else {
                const data = await response.json();
                alert("Error: " + data.error);
            }
        } catch (error) {
            console.error("Error adding movie to cart:", error);
            alert("There was an error adding the movie to your cart.");
        }
    };

    const handleGoToCart = () => {
        navigate("/cart");
    };

    return (
        <div className="container py-1">
            <div className="row g-4">
                <div className="col-md-4 text-center">
                    <img
                        src={movie.large_cover_image}
                        alt={movie.title}
                        className="img-fluid rounded shadow"
                        style={{
                            width: "750",
                            height: "auto",
                        }}
                    />
                </div>

                <div className="col-md-8">
                    <h2 className="mb-3">{movie.title_long}</h2>
                    <div className="row fs-6">
                        <div className="col-sm-6 mb-3">
                            <p><strong>Runtime:</strong> {movie.runtime || "N/A"} min</p>
                            <p><strong>Rating:</strong> {movie.rating || "N/A"}</p>
                            <p><strong>Year:</strong> {movie.year || "N/A"}</p>
                            <p><strong>Country:</strong> {movie.country || "N/A"}</p>
                        </div>
                        <div className="col-sm-6 mb-3">
                            <p><strong>Director:</strong> {movie.Director || "Unknown"}</p>
                            <p><strong>Summary:</strong> {movie.Plot || movie.summary || "No description available."}</p>
                            <p><strong>Awards:</strong> {movie.Awards || "N/A"}</p>
                            <br></br>
                        </div>
                    </div>

                    <p><strong>Price:</strong> {movie.price?.toFixed(2) || "N/A"} $</p>
                    <button
                        className="btn btn-primary mt-3"
                        onClick={isInCart ? handleGoToCart : handleAddToCart}
                    >

                        {isInCart ? "Go to Cart" : "Add to Cart"}
                    </button>

                    {movie.yt_trailer_code ? (
                        <div className="mt-2">
                            <h5>Trailer</h5>
                            <div className="ratio ratio-16x9">
                                <iframe
                                    src={`https://www.youtube.com/embed/${movie.yt_trailer_code}`}
                                    title="YouTube trailer"
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                    allowFullScreen
                                ></iframe>
                            </div>
                        </div>
                    ) : (
                        <p className="mt-4 text-muted">Trailer not available.</p>
                    )}
                </div>
            </div>

            <div className="container py-5">
                <h3>Opinions {averageRating}</h3>
                {token && <AddOpinionForm onAddOpinion={addOpinion} />}
                <div className="opinion-container mb-4">
                    {
                        opinions.map((opinion, index) => (
                            <Opinion
                                key={index}
                                currentUserId={currentUserId}
                                onEdit={editOpinion}
                                onDelete={deleteOpinion}
                                isAdmin={isAdmin}
                                {...opinion}
                            />
                        )
                    )}
                </div>
            </div>
            <div className="mt-4 text-center">
                <button
                    onClick={() => navigate(-1)}
                    className="btn btn-secondary"
                >
                    Go Back
                </button>
            </div>
        </div>
    );
}

export default MovieDetailsPage;