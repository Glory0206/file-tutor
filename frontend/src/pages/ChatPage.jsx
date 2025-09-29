import React, { useState, useEffect } from "react";
import { Container } from "react-bootstrap";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import { ChatMessage } from "../features/chat/components/ChatMessage";
import { MessageInput } from "../features/chat/components/MessageInput";

const initialMessages = [
  {
    id: 1,
    sender: "bot",
    avatar: "/public/icons/clober.png",
    text: "안녕? 나는 FileTutor야 필요한 정보를 알려줄게!",
  },
];

export function ChatPage() {
  const [messages, setMessages] = useState(initialMessages);
  const [files, setFiles] = useState([]);
  const { fileId } = useParams();

  useEffect(() => {
    const fetchFiles = async () => {
      try {
        const response = await axios.get("/api/files");
        setFiles(response.data || []);
      } catch (error) {
        console.error("Error fetching files:", error);
      }
    };

    fetchFiles();
  }, []);

  const handleSendMessage = async (text) => {
    if (!fileId) {
      const botMessage = {
        id: messages.length + 2,
        sender: "bot",
        avatar: "/public/icons/clober.png",
        text: "파일을 선택해주세요.",
      };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
      return;
    }

    const userMessage = {
      id: messages.length + 1,
      sender: "user",
      avatar: "",
      text: text,
    };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    try {
      const response = await axios.post(`/api/chat/${fileId}?question=${text}`);

      const botMessage = {
        id: messages.length + 2,
        sender: "bot",
        avatar: "/public/icons/clober.png",
        text: response.data.answer,
      };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error("Error sending message:", error);
      const errorMessage = {
        id: messages.length + 2,
        sender: "bot",
        avatar: "/public/icons/clober.png",
        text: "Sorry, something went wrong.",
      };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
  };

  return (
    <div style={{ height: "100%", display: "flex", flexDirection: "column" }}>
      <main
        style={{ flex: "1 1 auto", overflowY: "auto" }}
        className="bg-light"
      >
        <Container className="py-5">
          <div className="d-grid gap-3">
            {messages.map((msg) => (
              <ChatMessage key={msg.id} message={msg} />
            ))}
          </div>
        </Container>
      </main>

      <footer className="bg-light border-top">
        <MessageInput onSendMessage={handleSendMessage} />
      </footer>
    </div>
  );
}
