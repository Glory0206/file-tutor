import React from "react";
import { Form, Button, InputGroup, Image } from "react-bootstrap";

export function MessageInput() {
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
            placeholder="Type your message..."
            aria-label="Type your message..."
          />
          <Button variant="outline-secondary">
            {/* <AttachmentIcon /> */}
            📎
          </Button>
          <Button variant="primary">Send</Button>
        </InputGroup>
      </div>
    </footer>
  );
}
