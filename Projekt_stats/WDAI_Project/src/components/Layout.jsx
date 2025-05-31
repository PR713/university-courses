import { Outlet, Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import logo from '../assets/logo.png';
import avatar from '../assets/avatar.png';
import logout from '../assets/logout.png';
import cart from '../assets/cart.png';
import home from '../assets/home.png';
import login from '../assets/login.png';
import loginDark from '../assets/loginDark.png';
import logoutDark from '../assets/logoutDark.png';
import cartDark from '../assets/cartDark.png';
import homeDark from '../assets/homeDark.png';
import {useDarkMode} from './DarkModeContext';

function Layout() {
    const getYear = new Date().getFullYear();
    const navigate = useNavigate();
    const token = localStorage.getItem("token");
    const [cartTotalPrice, setCartTotalPrice] = useState(0);
    const { darkMode, toggleDarkMode } = useDarkMode();

    const updateCartTotalPrice = async () => {
        if (token) {
            const response = await fetch("http://localhost:5000/api/cart", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                const totalPrice = data.reduce((sum, movie) => sum + movie.price, 0);
                setCartTotalPrice(totalPrice);
            } else {
                console.error("Failed to fetch cart items");
            }
        }
    };

    useEffect(() => {
        updateCartTotalPrice();
    }, [token]);

    const handleLogout = () => {
        localStorage.removeItem("token");
        setCartTotalPrice(0);
        alert("You have been logged out.");
        navigate("/login");
    };

    const isTokenGiven = () => {
        return !!localStorage.getItem("token");
    }

    return (
        <div className={`d-flex flex-column min-vh-100 ${darkMode ? "bg-dark text-light" : "bg-light text-dark"}`}>
            <header className={`sticky-top shadow-lg ${darkMode ? "bg-dark" : "bg-light"}`}>
                <nav className="navbar navbar-expand-lg py-1">
                    <div className="container d-flex justify-content-between align-items-center">
                        <Link className={`navbar-brand fs-3 fw-bold ${darkMode ? "text-light" : "text-dark"}`} to="/">
                            <img src={logo} alt="Logo" width="55px" style={{ borderRadius: 5 }} />
                        </Link>

                        <button
                            className={`navbar-toggler ${darkMode ? "navbar-dark" : "navbar-light"}`}
                            type="button"
                            data-bs-toggle="collapse"
                            data-bs-target="#navbarNav"
                            aria-controls="navbarNav"
                            aria-expanded="false"
                            aria-label="Toggle navigation"
                        >
                            <span className="navbar-toggler-icon"></span>
                        </button>

                        <div className="collapse navbar-collapse justify-content-between" id="navbarNav">
                            <ul className="navbar-nav d-flex align-items-center">
                                <li className="nav-item mx-2">
                                    <Link className={`nav-link fs-5 ${darkMode ? "text-light" : "text-dark"} d-flex align-items-center`} to="/">
                                        {darkMode ? <img src={homeDark} width="25px" height="25px" title="Home" alt="Home by srip" /> :
                                        <img src={home} width="25px" height="25px" title="Home" alt="Home by srip" />}
                                    </Link>
                                </li>
                                <li className="nav-item mx-2">
                                    <Link className={`nav-link fs-5 ${darkMode ? "text-light" : "text-dark"} d-flex align-items-center`} to="/cart">
                                        {darkMode ? <img src={cartDark} width="30px" height="30px" title="Cart" alt="Cart by Freepik" /> :
                                        <img src={cart} width="30px" height="30px" title="Cart" alt="Cart by Hada Studio" /> }
                                        <span className="d-flex align-items-center">
                                            <span
                                                className={`badge rounded-pill ms-2 ${cartTotalPrice > 0 ? "bg-success" : "bg-secondary"}`}
                                                style={{ fontSize: "1.1rem", display: isTokenGiven() ? "inline" : "none" }}
                                            >
                                                ${cartTotalPrice.toFixed(2)}
                                            </span>
                                        </span>
                                    </Link>
                                </li>
                            </ul>

                            <ul className="navbar-nav d-flex align-items-center">
                                {token && (
                                    <li className="nav-item mx-2">
                                        <Link className={`nav-link fs-5 ${darkMode ? "text-light" : "text-dark"}`} to="/placedOrders">
                                            <img src={avatar} width="29px" height="29px" title="My Orders" alt="Avatar by Freepik" className="rounded-circle" />
                                        </Link>
                                    </li>
                                )}
                                <li className="nav-item mx-2">
                                    <button
                                        className="btn btn-link nav-link fs-5"
                                        onClick={toggleDarkMode}
                                        style={{ textDecoration: "none" }}
                                    >
                                        {darkMode ? "🌙" : "☀️"}
                                    </button>
                                </li>
                                {token ? (
                                    <li className="nav-item mx-2">
                                        <button
                                            className={`btn btn-link nav-link fs-5 ${darkMode ? "text-light" : "text-dark"}`}
                                            onClick={handleLogout}
                                            style={{ textDecoration: "none" }}
                                        >
                                            {darkMode ? <img src={logoutDark} width="29px" height="29px" title="Logout" alt="Logout by Pixel perfect" />
                                             : <img src={logout} width="29px" height="29px" title="Logout" alt="Logout by Pixel perfect" />}
                                        </button>
                                    </li>
                                ) : (
                                    <li className="nav-item mx-2">
                                        <Link className={`nav-link fs-5 ${darkMode ? "text-light" : "text-dark"}`} to="/login">
                                            {darkMode ? <img src={loginDark} width="29px" height="29px" title="Login" alt="Login by Pixel perfect" />
                                                : <img src={login} width="29px" height="29px" title="Login"
                                                             alt="Login by Pixel"/>}

                                        </Link>
                                    </li>
                                )}
                            </ul>
                        </div>
                    </div>
                </nav>
            </header>

            <main className="flex-grow-1">
                <div className="container py-4">
                    <Outlet context={{ updateCartTotalPrice }} />
                </div>
            </main>

            <footer className={`text-center py-3 mt-auto ${darkMode ? "bg-dark text-light" : "bg-light text-dark"}`}>
                <p className="mb-0">
                    &copy;{getYear} All Rights Reserved, data from yts.mx & omdb
                </p>
            </footer>
        </div>
    );
}

export default Layout;
