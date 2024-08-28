import ChatMessage from "./ChatMessage";

export default function MessageContainer({ messages, chatEndRef, isLoading }) {
    return (
        <div className="flex-1 flex flex-col overflow-y-scroll">
            <div className="flex-1 p-4 space-y-4">
                {messages.map((message, index) => (
                    <ChatMessage key={index} message={message} />
                ))}
                {isLoading && (
                    <div className="flex justify-center">
                        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
                    </div>
                )}
                <div ref={chatEndRef} />
            </div>
        </div>
    );
}