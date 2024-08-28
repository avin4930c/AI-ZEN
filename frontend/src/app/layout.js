import { Inter } from "next/font/google";
import "./globals.css";
import { IconBase } from "react-icons";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "AI ZEN - AI Chatbot",
  description: "AI ZEN is an AI chatbot designed to summarize PDF documents and generate queries to retrieve and summarize information from an SQLite database.",
  icons: {
    icon: "/favicon.ico",
  }
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
