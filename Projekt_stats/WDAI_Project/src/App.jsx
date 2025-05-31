import HomePage from "./pages/HomePage.jsx";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Layout from "./components/Layout.jsx";
import MovieDetailsPage from "./pages/MovieDetailsPage.jsx";
import CartPage from "./pages/CartPage.jsx";
import CreateAccountPage from "./pages/CreateAccountPage.jsx";
import LoginPage from "./pages/LoginPage.jsx";
import PlacedOrdersPage from "./pages/PlacedOrdersPage.jsx";
import {DarkModeProvider} from "./components/DarkModeContext.jsx";


function App() {

    return (
        <Router>
            <DarkModeProvider>
                <Routes>

                    <Route path="/" element={<Layout/>}>
                        <Route index element={<HomePage/>}/>
                        <Route path="cart" element={<CartPage/>}/>
                        <Route path="movies/:movieId" element={<MovieDetailsPage/>}/>
                        <Route path="register" element={<CreateAccountPage/>}/>
                        <Route path="login" element={<LoginPage/>}/>
                        <Route path="placedOrders" element={<PlacedOrdersPage/>}/>
                        <Route path="*" element={<h1>404 - Not Found</h1>}/>
                    </Route>


                </Routes>
            </DarkModeProvider>
        </Router>
    )
}

export default App
