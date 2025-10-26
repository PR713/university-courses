import { ReactNode } from 'react';

interface KoszykProps {
    children: ReactNode;
}

function Koszyk({ children }: KoszykProps) {
    return (
        <div>
            <p>Koszyk</p>
            {children}
        </div>
    )
}

export default Koszyk