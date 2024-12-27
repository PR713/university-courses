import {useState, useEffect} from "react";
import "./komentarz.css";

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

function Komentarze(){
    const [komentarze, setKomentarze] = useState<KomentarzProps[]>([]);
    const [loading, setLoading] = useState(true);


    return (
        <div id="komentarze-container">
            
        </div>
    );
}