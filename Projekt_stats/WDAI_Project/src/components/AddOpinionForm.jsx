import React, { useState } from "react";
import { Button, Form } from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';
import { useParams } from "react-router-dom";
import {useDarkMode} from "./DarkModeContext.jsx";

function AddOpinionForm({ onAddOpinion }) {
    const [name, setName] = useState("");
    const [rating, setRating] = useState(0);
    const [hovered, setHovered] = useState(0);
    const [text, setText] = useState("");
    const [isSubmitting, setIsSubmitting] = useState(false);
    const { movieId } = useParams();
    const {darkMode} = useDarkMode(); //setter niepotrzebny

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newOpinion = {
            movieId,
            name,
            rating,
            text,
            date: new Date().toLocaleDateString(),
        };

        setIsSubmitting(true);
        onAddOpinion(newOpinion); // Przekaż odpowiedź z backendu


        setIsSubmitting(false);
        setName("");
        setRating(0);
        setText("");
    };

    const handleClick = (value) => {
        setRating(value);
    };

    const handleMouseEnter = (value) => {
        setHovered(value);
    };

    const handleMouseLeave = () => {
        setHovered(0);
    };

    return (
        <div className="add-opinion-form py-4">
            <h6>Add your opinion</h6>
            <Form onSubmit={handleSubmit} className="p-3 border rounded shadow-sm">
                <Form.Group className="mb-3">
                    <Form.Label>Name</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter your name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Label>Rating</Form.Label>
                    <div style={{ fontSize: "2rem", cursor: "pointer" }}>
                        {[1, 2, 3, 4, 5].map((rate) => (
                            <span
                                key={rate}
                                onClick={() => handleClick(rate)}
                                onMouseEnter={() => handleMouseEnter(rate)}
                                onMouseLeave={handleMouseLeave}
                                className={`${rate <= (hovered || rating) ?
                                    "text-warning" : darkMode ? "text-light" : "text-muted"}`}
                            >
                                ★
                            </span>
                        ))}
                    </div>
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Label>Text</Form.Label>
                    <Form.Control
                        as="textarea"
                        rows={3}
                        placeholder="Write your opinion here"
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                        required
                    />
                </Form.Group>
                <Button variant="primary" type="submit" disabled={isSubmitting}>
                    {isSubmitting ? 'Submitting...' : 'Submit Opinion'}
                </Button>
            </Form>
        </div>
    );
}

export default AddOpinionForm;