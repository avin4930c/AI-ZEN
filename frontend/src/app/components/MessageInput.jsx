import { FaPaperPlane } from 'react-icons/fa';

export default function MessageInput({ input, setInput, handleSubmit, isLoading }) {
    return (
        <form onSubmit={handleSubmit} className="p-4 bg-white border-t flex-none">
            <div className="flex items-center space-x-2">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    className="flex-1 p-2 border rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Ask about the PDF or database..."
                    required
                />
                <button
                    type="submit"
                    className="p-2 text-white bg-blue-500 rounded-full hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    disabled={isLoading}
                >
                    <FaPaperPlane className="w-5 h-5" />
                </button>
            </div>
        </form>
    );
}