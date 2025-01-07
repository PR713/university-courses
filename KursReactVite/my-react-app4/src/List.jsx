import PropTypes from "prop-types";

function List(props) {
    const itemList = props.items;
    const category = props.category;
    // const fruits =
    //     [{id: 1, name: "apple", calories: 95},
    //         {id: 2, name: "orange", calories: 45},
    //         {id: 3, name: "banana", calories: 105},
    //         {id: 4, name: "coconut", calories: 155},
    //         {id: 5, name: "pineapple", calories: 37}];

    //fruits.sort((a,b) => a.name.localeCompare(b.name));
    //fruits.sort((a,b) => b.name.localeCompare(a.name)); //REVERSE ALPHABETICAL
    //fruits.sort((a,b) => a.calories - b.calories); //NUMERICAL
    //fruits.sort((a,b) => b.calories - a.calories);

    // Wynik jest mniejszy niż 0 (np. a.number jest mniejsze niż b.number), to a zostanie umieszczone przed b
    //(czyli zachowamy rosnący porządek).
    //Wynik jest większy niż 0 (np. a.number jest większe niż b.number), to b zostanie umieszczone przed a.
    //Wynik jest równy 0 (np. a.number jest równe b.number), wtedy nie zmienia się kolejność tych dwóch elementów.

    //const lowCalFruits = fruits.filter(fruit => fruit.calories < 100);

    const listItems = itemList.map(item => <li key={item.id}>
        {item.name}: &nbsp;
        <b>{item.calories}</b></li>);

    // const listItems = lowCalFruits.map(lowCalFruit => <li key={lowCalFruit.id}>
    //                                     {lowCalFruit.name}: &nbsp;
    //                                     <b>{lowCalFruit.calories}</b></li>);

    return (<>
                <h3 className="list-category">{category}</h3>
                <ol className="list-items">{listItems}</ol>
            </>);
}
List.propTypes = {
    category: PropTypes.string,
    items: PropTypes.arrayOf(PropTypes.shape({
                                    id: PropTypes.number,
                                    name: PropTypes.string,
                                    calories: PropTypes.number}))
}

List.defaultProps = {
    category: "Category",
    items: []
}

export default List