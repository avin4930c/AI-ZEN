import { FaBars, FaTimes } from 'react-icons/fa';

export default function Header({ toggleSidebar, isSidebarOpen }) {
    return (
        <header className="bg-white p-4 flex justify-between items-center md:hidden">
            <h1 className="text-xl font-bold">AI ZEN</h1>
            <button onClick={toggleSidebar} className="text-2xl">
                {isSidebarOpen ? <FaTimes /> : <FaBars />}
            </button>
        </header>
    );
}