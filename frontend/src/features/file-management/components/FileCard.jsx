import { Card } from "react-bootstrap";

function FileCard({ file }) {
  return (
    <Card className="h-100">
      {/* 파일 미리보기 이미지 */}
      <Card.Img variant="top" src={file.image} />
      <Card.Body>
        {/* 파일 이름 (이름이 길 경우 ...으로 표시) */}
        <Card.Title className="text-truncate">{file.name}</Card.Title>
        {/* 파일 수정 날짜 */}
        <Card.Text>
          <small className="text-muted">{file.date}</small>
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default FileCard;
