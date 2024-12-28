import {useParams} from "react-router-dom";

interface Article {
    id: number;
    title: string;
    content: string;
}

function Article() {

    const {id} = useParams<{ id: string }>(); //pobranie id z url
    const storedArticles = localStorage.getItem("articles");
    const articles: Article[] = storedArticles ? JSON.parse(storedArticles) : [];
    const article: Article | undefined = articles.find((a) => a.id === Number(id));

    return (<div>
            {article ? (
                <>
                    <h1>{article.title}</h1>
                    <p>{article.content}</p>
                </>
            ) : (
                <p>Nie znaleziono artykułu.</p>
            )}
        </div>
    );
}

export default Article;