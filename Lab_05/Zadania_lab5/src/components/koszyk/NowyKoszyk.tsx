import Produkt from "./Produkt.tsx";
import React from "react";

function NowyKoszyk(){

    const Produkty = ['apple', 'pear', 'banana', 'ananas', 'grape'];

    return(
        <div>
            <ul>
                {Produkty.map((produkt) => (
                    <li><Produkt name={produkt}/></li>
                        ))}
            </ul>
        </div>
    )
}

export default NowyKoszyk;