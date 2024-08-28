import { FaPaperclip, FaDatabase, FaFilePdf } from 'react-icons/fa';

export default function Sidebar({ pdfFile, handleFileUpload, isSidebarOpen }) {
    return (
        <div className={`w-full md:w-64 bg-white shadow-lg p-4 ${isSidebarOpen ? 'block' : 'hidden'} md:block`}>
            <h1 className="text-2xl font-bold mb-4 hidden md:block">AI ZEN</h1>
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                    Upload PDF
                </label>
                <div className="flex items-center justify-center w-full">
                    <label className="flex flex-col items-center justify-center w-full h-32 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100" aria-label="Upload PDF">
                        <div className="flex flex-col items-center justify-center pt-5 pb-6">
                            <FaPaperclip className="w-8 h-8 text-gray-400 mb-2" />
                            <p className="mb-2 text-sm text-gray-500 text-center">
                                <span className="font-semibold">Click to upload PDF</span>
                            </p>
                        </div>
                        <input
                            type="file"
                            className="hidden"
                            accept=".pdf"
                            onChange={handleFileUpload}
                        />
                    </label>
                </div>
            </div>
            {pdfFile && (
                <p className="text-sm text-gray-600">
                    Uploaded: {pdfFile.name}
                    <a href={URL.createObjectURL(pdfFile)} download={pdfFile.name} className="text-blue-500 ml-2">
                        Download
                    </a>
                </p>
            )}
            <div className="mt-8">
                <h2 className="text-xl font-semibold mb-4">Data Sources</h2>
                <div className="space-y-4">
                    <div className="flex items-center space-x-2">
                        <FaDatabase className="w-6 h-6 text-blue-500" />
                        <span>SQLite Database</span>
                    </div>
                    <div className="flex items-center space-x-2">
                        <FaFilePdf className="w-6 h-6 text-green-500" />
                        <span>Uploaded PDF</span>
                    </div>
                </div>
            </div>
        </div>
    );
}