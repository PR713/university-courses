import { createContext, useState, useContext } from 'react';
import PropTypes from "prop-types";

// Tworzymy Context do zarządzania trybem ciemnym
const DarkModeContext = createContext();

// Custom Hook do używania DarkModeContext w komponentach
export const useDarkMode = () => useContext(DarkModeContext);
//pozwala uzyskać dostęp do wartości przekazanych w DarkModeContext (w value)
// przez DarkModeProvider

export const DarkModeProvider = ({ children }) => {
    const [darkMode, setDarkMode] = useState(false);

    const toggleDarkMode = () => setDarkMode(prev => !prev);

    return (
        <DarkModeContext.Provider value={{ darkMode, toggleDarkMode }}>
            {children}
        </DarkModeContext.Provider>
    );//wszystkie dzieci komponentu DarkModeProvider będą miały dostęp do wartości w value
};

DarkModeProvider.propTypes = {
    children: PropTypes.node.isRequired
}