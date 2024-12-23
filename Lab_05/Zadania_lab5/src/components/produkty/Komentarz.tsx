import {useState} from "react";
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

//lub const Komentarz: React.FC<KomentarzProps> = ({ id, body, postId, likes, user }) => {...
function Komentarz({id, body, postId, likes, user}: KomentarzProps) {

    const [likesCount, setLikesCount] = useState(likes);

    function handleLikesCountUp() {
        setLikesCount(l => l + 1);
    }

    function handleLikesCountDown() {
        if (likesCount > 0) {
            setLikesCount(l => l - 1);
        }
    }

    return (
        <div id="komentarz-container">
            <div id="userinfo">
                <p className="pinfo">#{id}</p>
                <p className="pinfo">{user.username}</p>
                <p className="pinfo">{user.fullName}</p>
            </div>
            <div id="generalinfopost">
                <p className="pcasual">Nr komentarza: {postId}</p>
                <p className="pcasual">{body}</p>
            </div>
            <div id="likesinfo">
                <button id="amount-likes">{likesCount}</button>
                <button className="like" onClick={handleLikesCountUp}>👍</button>
                <button className="like" onClick={handleLikesCountDown}>👎</button>
            </div>
        </div>
    );
}

export default Komentarz;