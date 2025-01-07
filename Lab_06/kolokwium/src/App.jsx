import {BrowserRouter, Route, Routes} from "react-router-dom";
import List from "./components/List.jsx";
import ShapeDetails from "./components/shapeDetails.jsx";


function App() {
    //można tutaj zrobić initialList i przekazać do List jako props
    // list i setList lub localStorage lub wgl wszystko w localStorage
    return(
        <BrowserRouter>
            <div className="container">
                <Routes>
                    <Route path="/" element={<List/>}/>
                    <Route path="/shape/:id" element={<ShapeDetails/>}/>
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App
