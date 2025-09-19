import { Image } from "react-bootstrap";

export function ChatMessage({ message }) {
  const { sender, avatar, text, content } = message;
  const isUser = sender === "user";

  const Avatar = () => (
    <Image
      src={avatar}
      roundedCircle
      style={{ width: "40px", height: "40px" }}
      alt={`${sender} avatar`}
    />
  );

  return (
    <div className={`d-flex gap-3 ${isUser ? "justify-content-end" : ""}`}>
      {!isUser && <Avatar />}

      <div
        className={`d-flex flex-column ${
          isUser ? "align-items-end" : "align-items-start"
        }`}
      >
        <p className="small text-muted mb-1">{isUser ? "You" : "Aida"}</p>
        <div
          className={`p-3 rounded-3 ${
            isUser ? "bg-primary text-white" : "bg-light text-dark"
          }`}
          style={{ maxWidth: "500px" }}
        >
          <p className="mb-0">{text}</p>
        </div>
      </div>

      {isUser && <Avatar />}
    </div>
  );
}
