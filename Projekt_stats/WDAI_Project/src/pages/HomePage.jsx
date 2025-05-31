import SearchBar from "../components/SearchBar.jsx";
import {useEffect, useState} from "react";
import Movie from "../components/Movie.jsx";

function HomePage() {
    const [movies, setMovies] = useState([]);
    const [filteredMovies, setFilteredMovies] = useState([]);
    const [loading, setLoading] = useState(false);
    const [sortOption, setSortOption] = useState("default");

    const enrichMoviesWithOMDb = async (movies) => {// Funkcja do wzbogacania filmów o dane z OMDb
        return Promise.all(
            movies.map(async (movie) => {
                if (movie.imdb_code) {
                    const omdbResponse = await fetch(
                        `https://www.omdbapi.com/?i=${movie.imdb_code}&apikey=e23afbb8`
                    );

                    if (omdbResponse.ok) {
                        const omdbData = await omdbResponse.json();
                        return {...movie, ...omdbData, price: calculatePrice(movie.id)};
                    }
                }
                return {...movie, price: calculatePrice(movie.id)};
            })
        );
    };


    const fetchInitialMovies = async () => {// Pobieranie filmów domyślnych (pierwsze ładowanie strony)
        try {
            setLoading(true);
            const response = await fetch(`https://yts.mx/api/v2/list_movies.json?page=${getRandomInt()}&limit=30`);
            await checkIfResponseOk(response);
        } catch (error) {
            console.error("Error fetching initial movies:", error);
        } finally {
            setLoading(false);
        }
    };


    const fetchMoviesBySearch = async (searchValue) => {// Pobieranie filmów według zapytania użytkownika
        try {
            setLoading(true);
            await new Promise(resolve => setTimeout(resolve, 500));
            const response = await fetch(`https://yts.mx/api/v2/list_movies.json?query_term=${searchValue}`);
            if (!await checkIfResponseOk(response)) {
                setMovies([]);
                setFilteredMovies([]);
            }
        } catch (error) {
            console.error("Error fetching searched movies:", error);
        } finally {
            setLoading(false);
        }
    };


    const checkIfResponseOk = async (response) => {
        if (!response.ok) throw new Error("Network response was not ok");
        const data = await response.json();
        if (data && data.data && Array.isArray(data.data.movies)) {
            const enrichedMovies = await enrichMoviesWithOMDb(data.data.movies);
            setMovies(enrichedMovies);
            setFilteredMovies(enrichedMovies);
            return true;
        }
        return false;
    }


    const handleSearch = (searchValue) => {
        if (searchValue.trim() === "" || searchValue === " " || searchValue === null) {
            fetchInitialMovies();
            setFilteredMovies(movies); // Resetuje filtry
        } else {
            fetchMoviesBySearch(searchValue);
        }
    };

    // Pierwsze ładowanie filmów
    useEffect(() => {
        fetchInitialMovies();
    }, []);

    const handleSortChange = (e) => {
        const value = e.target.value;
        setSortOption(value);
        sortMovies(value);
    };

    const sortMovies = (option) => {
        let sortedMovies = [...filteredMovies];

        switch (option) {
            case "default":
                sortedMovies = [...movies];
                break;
            case "yearAsc":
                sortedMovies.sort((a, b) => a.year - b.year);
                break;
            case "yearDesc":
                sortedMovies.sort((a, b) => b.year - a.year);
                break;
            case "ratingAsc":
                sortedMovies.sort((a, b) => a.rating - b.rating);
                break;
            case "ratingDesc":
                sortedMovies.sort((a, b) => b.rating - a.rating);
                break;
            default:
                break;
        }

        setFilteredMovies(sortedMovies);
    };

    function getRandomInt() {
        return Math.floor(Math.random() * 100) + 1;
    }

    const calculatePrice = (id) => {
        return (12 + 2 * Math.log(id) + 4 * Math.sin(id))/4;
    }

    return (
        <>
            <SearchBar searchingFor={handleSearch}/>
            <div className="container mt-4">
                <div className="mb-3">
                    <div className="d-flex align-items-center me-auto" style={{maxWidth: '250px'}}>
                        <label htmlFor="sortSelect" className="form-label mb-0 me-2">
                            Sort&nbsp;by
                        </label>
                        <select
                            id="sortSelect"
                            className="form-select"
                            value={sortOption}
                            onChange={handleSortChange}
                        >
                            <option value="default">Default</option>
                            <option value="yearAsc">Year (Ascending)</option>
                            <option value="yearDesc">Year (Descending)</option>
                            <option value="ratingAsc">Rating (Ascending)</option>
                            <option value="ratingDesc">Rating (Descending)</option>
                        </select>
                    </div>

                </div>
                {loading ? (
                    <p className="text-center">Loading...</p>
                ) : filteredMovies.length > 0 ? (
                    <div className="row">
                        {filteredMovies.map((movie) => (
                            <Movie key={movie.id} movie={movie}/>
                        ))}
                    </div>
                ) : (
                    <p className="text-center">No movies found...</p>
                )}
            </div>
        </>
    );
}

export default HomePage;