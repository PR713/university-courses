import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
interface Article {
    id: number;
    title: string;
    content: string;
}

function AddArticle() {
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const navigate = useNavigate();

    function handleTitleChange(event: React.ChangeEvent<HTMLInputElement>) {
        setTitle(event.target.value);
    }

    function handleContentChange(event: React.ChangeEvent<HTMLTextAreaElement>) {
        setContent(event.target.value);
    }

    function handleAddArticle(event: React.FormEvent) {
        event.preventDefault(); //blokuje przeładowanie strony

        const existingArticles: Article[] = JSON.parse(localStorage.getItem("articles") || "[]");

        const newArticle: Article = {
            id: existingArticles.length + 1,
            title,
            content,
        };

        localStorage.setItem("articles", JSON.stringify([...existingArticles, newArticle]));
        navigate("/blog");
    }

    return (
        <div>
            <h1>Dodaj artykuł</h1>
            <form id="form" onSubmit={handleAddArticle}>
                <div>
                    <label>Tytuł:</label>
                    <br/>
                    <input type="text" value={title} name="title" onChange={handleTitleChange} required/>
                </div>
                <div>
                    <label>Treść:</label>
                    <br/>
                    <textarea value={content} name="content" onChange={handleContentChange} required/>
                </div>{/*event jest automatycznie przekazywany w onChange ^*/}
                <button type="submit">Dodaj</button>
            </form>
        </div>
    );
}

export default AddArticle;
