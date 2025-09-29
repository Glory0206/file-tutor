import React, { useState } from "react";
import { Form, Button, InputGroup, Image } from "react-bootstrap";

export function MessageInput({ onSendMessage }) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (text.trim()) {
      onSendMessage(text);
      setText("");
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <footer className="bg-light border-top p-3">
      <div className="d-flex align-items-center gap-3">
        <Image
          alt="User Avatar"
          roundedCircle
          style={{ width: "40px", height: "40px" }}
          src="https://lh3.googleusercontent.com/aida-public/AB6AXuCsB7zuVlVpcywhNtJXwKXlffIizvfLT5jES4MkTN9d9GYytgMN_p0Xi-1rt7ybdqqyV_6vz_RII0Z_ZOQD90-EwUNnyIz3KEyMvzofEH3bdfH7O5do_IdzLhMO8tPEtkHBSQ24HAIgct5MYd9PDIs8nRdBTYEmg_XLlGw_Zz7GM2VRnRGQhDAtSVqqoz53wsz2yGCHFCz8zAwiqt16W0RN9FD_3cM_SZeoaoTzOzOs7cNSSCLodzJ3WC4AsX2ZOTaCmj7BFr2k7L0"
        />
        <InputGroup>
          <Form.Control
            placeholder="무엇이든 물어보세요"
            aria-label="Type your message..."
            value={text}
            onChange={(e) => setText(e.target.value)}
            onKeyPress={handleKeyPress}
          />
          <Button variant="outline-secondary">📎</Button>
          <Button variant="primary" onClick={handleSend}>
            Send
          </Button>
        </InputGroup>
      </div>
    </footer>
  );
}
