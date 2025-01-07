import {BrowserRouter, Route, Routes} from "react-router-dom";
import HomePage from "./pages/HomePage.jsx";
import ProductDetails from "./components/ProductDetails.jsx";

function App() {
    return (
        <>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/product/:id" element={<ProductDetails/>}/>
            </Routes>
        </BrowserRouter>
        </>

    )
}

export default App
