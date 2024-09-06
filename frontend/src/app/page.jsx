'use client';

import { useState, useEffect, useRef } from 'react';

import Header from './components/Header';
import Sidebar from './components/SideBar';
import MessageContainer from './components/MessageContainer';
import MessageInput from './components/MessageInput';

export default function Home() {
  const [messages, setMessages] = useState([{ text: 'Hello! How can I help you today? For PDF-related questions, please use the "pdf" keyword.', isUser: false }]);
  const [input, setInput] = useState('');
  const [pdfFile, setPdfFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (input.trim()) {
      setIsLoading(true);
      setMessages((prev) => [...prev, { text: input, isUser: true }]);

      try {
        const response = await fetch('http://localhost:8000/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: input, pdfFile: pdfFile?.name }),
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();

        setMessages((prev) => [...prev, { text: data?.response, isUser: false, isMarkdown: true }]);
      } catch (error) {
        console.error('Error:', error);
        setMessages((prev) => [
          ...prev,
          { text: 'Sorry, there was an error processing your request.', isUser: false },
        ]);
      } finally {
        setIsLoading(false);
        setInput('');
      }
    }
  };

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];

    if (file && file.type === 'application/pdf') {
      try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('http://localhost:8000/api/upload_pdf', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error('Failed to upload PDF');
        }

        setPdfFile(file);
        const data = await response.json();
        alert(data.message);
      } catch (error) {
        console.error('Error uploading PDF:', error);
        alert('Error uploading PDF. Please try again.');
      }
    } else {
      alert('Please upload a PDF file');
    }
  };

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100 md:flex-row">
      <Header toggleSidebar={toggleSidebar} isSidebarOpen={isSidebarOpen} />
      <Sidebar
        isSidebarOpen={isSidebarOpen}
        handleFileUpload={handleFileUpload}
        pdfFile={pdfFile}
        toggleSidebar={toggleSidebar}
      />
      <div className="flex-1 flex flex-col">
        <MessageContainer messages={messages} isLoading={isLoading} chatEndRef={chatEndRef} />
        <MessageInput input={input} setInput={setInput} handleSubmit={handleSubmit} isLoading={isLoading} />
      </div>
    </div>
  );
}