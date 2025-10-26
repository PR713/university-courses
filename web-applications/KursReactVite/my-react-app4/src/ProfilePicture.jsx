
function ProfilePicture(){
    const imageUrl = './src/assets/react.svg';

    //const handleClick = () => console.log("OUCH!");
    const handleClick = (e) => e.target.style.display = "none";

    return(<img onClick={(e) => handleClick(e)} src={imageUrl}></img>);
    //tutaj ^ (e) pobiera z kliknięcia dlatego przekazujemy (e) a nie ()
}

export default ProfilePicture