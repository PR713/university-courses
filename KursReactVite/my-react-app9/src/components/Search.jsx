import PropTypes from "prop-types";

function Search({onSearch}){

    return (
        <div>
            <input type="text" placeholder="Search..." onChange={(e) => onSearch(e.target.value)}/>
        </div>
    )
}

Search.propTypes = {
    onSearch: PropTypes.func.isRequired,
};

export default Search