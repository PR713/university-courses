import {useEffect, useState} from "react";
import {Link} from "react-router-dom";

interface Article {
    id: number;
    title: string;
    content: string;
}

function Blog() {

    const [articles, setArticles] = useState<Article[]>([]);

    useEffect(() => {
        const storedArticles = localStorage.getItem("articles");
        const articles: Article[] = storedArticles ? JSON.parse(storedArticles) : [];
        setArticles(articles);
    }, []); // runs only once after the component is mounted
    // i tak jeśli zmieniam podstronę to komponent Blog jest odmontowywany i montowany na nowo

    return (<div>
        <h1>Lista artykułów</h1>
        {articles.length > 0 ? (
            <ul>
                {articles.map((article) => (
                    <li key={article.id}>
                        <Link to={`/article/${article.id}`}>{article.title}</Link>
                    </li>
                ))}
            </ul>
        ) : ( <p>Brak artykułów</p>)}
    </div>);
}

export default Blog;
