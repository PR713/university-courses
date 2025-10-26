import {useState, useEffect} from "react";
import "./komentarz.css";
import Komentarz from "./Komentarz.tsx";

interface User {
    id: number;
    username: string;
    fullName: string;
}

interface KomentarzProps {
    id: number;
    body: string;
    postId: number;
    likes: number;
    user: User;
}

function Komentarze() {
    const [komentarze, setKomentarze] = useState<KomentarzProps[]>([]);

    useEffect(() => {
        fetch("https://dummyjson.com/comments")
            .then(response => response.json())
            .then(data => {
                setKomentarze(data.comments);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    return (
        <div id="komentarze-container">
            {komentarze.map((comment) => (
                <Komentarz
                    id={comment.id}
                    body={comment.body}
                    postId={comment.postId}
                    likes={comment.likes}
                    user={comment.user}/>
            ))}
        </div>
    );
}

export default Komentarze;