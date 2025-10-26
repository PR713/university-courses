import React, {useState} from 'react';


function MyComponent1(){
    const [name, setName] = useState("Guest");
    const [quantity, setQuantity] = useState(1);
    const [comment, setComment] = useState("");
    const [payment, setPayment] = useState("");
    const [shipping, setShipping] = useState("");

    function handleNameChange(event){
        setName(event.target.value);
    }

    function handleQuantityChange(event){
        setQuantity(event.target.value);
    }

    function handleCommentChange(event){
        setComment(event.target.value);
    }

    function handlePaymentChange(event){
        setPayment(event.target.value);
    }

    function handleShippingChange(event) {
        setShipping(event.target.value);
    }

    return(<div>
            <input value={name} onChange={handleNameChange}/>
            <p>Name: {name}</p>

            <input value={quantity} onChange={handleQuantityChange} type="number"/>
            <p>Quantity: {quantity}</p>

            <textarea value={comment} onChange={handleCommentChange}
            placeholder="Enter delivery instructions"/>
            <p>Comment: {comment}</p>

            <select value={payment} onChange={handlePaymentChange}>
                <option value="">Select an option</option>
                <option value="Visa">Visa</option>
                <option value="MasterCard">MasterCard</option>
                <option value="GiftCard">GiftCard</option>
            </select>
            <p>Payment: {payment}</p>

            <label>
                <input type="radio" value="PickUp"
                        checked={shipping === "PickUp"}
                        onChange={handleShippingChange}/>
                Pick Up
            </label> <br/>
            <label>
                <input type="radio" value="Delivery"
                                checked={shipping=== "Delivery"}
                                onChange={handleShippingChange}/>
                Delivery
                {/*checked w sensie box checked wyświetlony jeśli ustawione na Delivery
                można np zrobić że zaznaczają się na krzyż xd*/}
            </label>
            <p>Shipping: {shipping}</p>
    </div>);
}

export default MyComponent1