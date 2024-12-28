//import Licznik from "./Licznik.tsx";
import {BrowserRouter, Routes, Route, Link} from "react-router-dom";
import BlogPage from "./pages/BlogPage.tsx";
import HomePage from "./pages/HomePage.tsx";
import ArticlePage from "./pages/ArticlePage.tsx";
import DodajPage from "./pages/DodajPage.tsx";

function App() {
    // return (<>
    //         <Licznik />
    //     </>);

    return (<>
        <BrowserRouter>
            <div>
                <nav>
                    <Link to='/'>Home</Link> |
                    <Link to='/blog'>Blog</Link> |
                    <Link to='/dodaj'>Add Article</Link>
                </nav>
                <Routes>
                    <Route path="/" element={<HomePage/>}/>
                    <Route path="/blog" element={<BlogPage/>}/>
                    <Route path="/article/:id" element={<ArticlePage/>}/>
                    <Route path="/dodaj" element={<DodajPage/>}/>
                </Routes>
            </div>
        </BrowserRouter>
    </>);
}


export default App
