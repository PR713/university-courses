import React, { ReactNode } from 'react';

interface KoszykProps {
    children: ReactNode;
}

function Koszyk({ children }: KoszykProps) {
    return (
        <div>
            <h1>Koszyk</h1>
            {children}
        </div>
    )
}

export default Koszyk