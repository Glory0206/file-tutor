import React, { useState } from "react";
import { Container } from "react-bootstrap";
import { ChatMessage } from "../features/chat/components/ChatMessage";
import { MessageInput } from "../features/chat/components/MessageInput";

const initialMessages = [
  {
    id: 1,
    sender: "bot",
    avatar: "/public/icons/clober.png",
    text: "안녕? 나는 FileTutor야 필요한 정보를 알려줄게!",
  },
  {
    id: 2,
    sender: "user",
    avatar: "",
    text: "BFS와 DFS에 대해서 설명해줘",
  },
];

export function ChatPage() {
  const [messages, setMessages] = useState(initialMessages);

  return (
    <div
      style={{ minHeight: "100vh", display: "flex", flexDirection: "column" }}
    >
      <main className="flex-grow-1 bg-light">
        <Container className="py-5">
          <div className="d-grid gap-3">
            {messages.map((msg) => (
              <ChatMessage key={msg.id} message={msg} />
            ))}
          </div>
        </Container>
      </main>

      <MessageInput />
    </div>
  );
}
