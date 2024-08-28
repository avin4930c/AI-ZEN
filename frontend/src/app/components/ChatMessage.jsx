import ReactMarkdown from 'react-markdown';

export default function ChatMessage({ message }) {
    return (
        <div className={`flex ${message.isUser ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-xs sm:max-w-md md:max-w-lg lg:max-w-2xl xl:max-w-3xl rounded-lg p-3 ${message.isUser ? 'bg-blue-500 text-white' : 'bg-white text-black'}`}>
                {message.isMarkdown ? (
                    <ReactMarkdown>{message.text}</ReactMarkdown>
                ) : (
                    <p>{message.text}</p>
                )}
            </div>
        </div>
    );
}