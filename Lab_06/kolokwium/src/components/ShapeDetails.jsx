import {useParams} from "react-router-dom";

function ShapeDetails() {

    const {id} = useParams();
    const storedShapes = localStorage.getItem("list");
    const shapes = storedShapes ? JSON.parse(storedShapes) : [];

    const shape = shapes.find( shape => shape.id === String(id));

    return (
        <div>
            {shape ? <p>Kształt: {shape.type},  ID: {shape.id}</p>
                : <p>Shape not found</p>}
        </div>
    );
}

export default ShapeDetails;