import PropTypes from "prop-types";

function SearchBar({searchingFor}) {
    return (
        <div className="container my-4">
            <div className="input-group">
                <input
                    type="text"
                    className="form-control"
                    placeholder="Search..."
                    aria-label="Search"
                    onChange={(e) => searchingFor(e.target.value)}
                />
                <button className="btn btn-primary" type="button">
                    Search
                </button>
            </div>
        </div>
    );
}

SearchBar.propTypes = {
    searchingFor: PropTypes.func.isRequired,
};

export default SearchBar;