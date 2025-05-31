import { Dropdown, Modal, Button, Form } from 'react-bootstrap';
import { useState } from 'react';
import PropTypes from "prop-types";
import {useDarkMode} from "./DarkModeContext.jsx";

function Opinion({ id, name, date, rating, text, avatar, currentUserId, userId, onEdit, onDelete, isAdmin }) {
    const [isEditing, setIsEditing] = useState(false);
    const [editedText, setEditedText] = useState(text);
    const [editedRating, setEditedRating] = useState(rating);
    const [hovered, setHovered] = useState(0);
    const {darkMode} = useDarkMode();

    const handleEdit = () => {
        setIsEditing(true);
    };

    const handleSave = () => {
        onEdit(id, { text: editedText, rating: editedRating }); // Call parent function
        setIsEditing(false);
    };

    const handleDelete = () => {
        if (window.confirm("Are you sure you want to delete this opinion?")) {
            onDelete(id); // Call parent function
        }
    };

    return (
        <div className="opinion-card p-3 mb-3 border rounded shadow-sm">
            <div className="d-flex align-items-center mb-2">
                <img
                    src={avatar || "https://avatar.iran.liara.run/public"}
                    alt={name}
                    className="rounded-circle me-2"
                    style={{ width: '50px', height: '50px' }}
                />
                <div>
                    <h5 className="mb-0">{name}</h5>
                    <small className="text-muted">{date}</small>
                </div>
            </div>
            <div className="mb-2">
                <strong>Rating: </strong>
                {[...Array(5)].map((_, index) => (
                    <span
                        key={index}
                        className={index < rating ? "text-warning" : darkMode ? "text-light" : "text-muted"}
                    >
                        ★
                    </span>
                ))}
            </div>
            <p>{text}</p>

            {(currentUserId === userId) && (
                <div className="d-flex justify-content-end">
                    <Dropdown>
                        <Dropdown.Toggle variant="secondary" id="dropdown-custom-components">
                            Opcje
                        </Dropdown.Toggle>
                        <Dropdown.Menu>
                            <Dropdown.Item onClick={handleEdit}>Edytuj</Dropdown.Item>
                            <Dropdown.Item onClick={handleDelete} className="text-danger">Usuń</Dropdown.Item>
                        </Dropdown.Menu>
                    </Dropdown>
                </div>
            )}

            {(isAdmin === 'admin' && (currentUserId !== userId)) && (
                <div className="d-flex justify-content-end">
                    <Dropdown>
                        <Dropdown.Toggle variant="secondary" id="dropdown-custom-components">
                            Opcje
                        </Dropdown.Toggle>
                        <Dropdown.Menu>
                            <Dropdown.Item onClick={handleDelete} className="text-danger">Usuń</Dropdown.Item>
                        </Dropdown.Menu>
                    </Dropdown>
                </div>
            )}


            {/* Edit Modal */}
            <Modal show={isEditing} onHide={() => setIsEditing(false)}>
                <Modal.Header closeButton>
                    <Modal.Title>Edit Opinion</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form>
                        <Form.Group className="mb-3">
                            <Form.Label>Text</Form.Label>
                            <Form.Control
                                as="textarea"
                                rows={3}
                                value={editedText}
                                onChange={(e) => setEditedText(e.target.value)}
                            />
                        </Form.Group>
                        <Form.Group className="mb-3">
                            <Form.Label>Rating</Form.Label>
                            <div style={{ fontSize: "2rem", cursor: "pointer" }}>
                                {[1, 2, 3, 4, 5].map((rate) => (
                                    <span
                                        key={rate}
                                        onClick={() => setEditedRating(rate)}
                                        onMouseEnter={() => setHovered(rate)}
                                        onMouseLeave={() => setHovered(0)}
                                        className={`${
                                            rate <= (hovered || editedRating)
                                                ? "text-warning" : "text-muted"
                                        }`}
                                    >
                            ★
                        </span>
                                ))}
                            </div>
                        </Form.Group>
                    </Form>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={() => setIsEditing(false)}>
                        Cancel
                    </Button>
                    <Button variant="primary" onClick={handleSave}>
                        Save Changes
                    </Button>
                </Modal.Footer>
            </Modal>

        </div>
    );
}

Opinion.propTypes = {
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    date: PropTypes.string.isRequired,
    rating: PropTypes.number.isRequired,
    text: PropTypes.string.isRequired,
    avatar: PropTypes.string,
    currentUserId: PropTypes.number,
    userId: PropTypes.number.isRequired,
    onEdit: PropTypes.func.isRequired,
    onDelete: PropTypes.func.isRequired,
    isAdmin: PropTypes.string.isRequired,
}

export default Opinion;