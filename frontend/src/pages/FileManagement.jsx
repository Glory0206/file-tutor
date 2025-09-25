import React, { useState, useMemo, useEffect, useRef } from "react";
import { Container, Row, Col, Button, Form, InputGroup } from "react-bootstrap";
import axios from "axios";
import FileCard from "../features/file-management/components/FileCard";

import { Search, Upload } from "react-bootstrap-icons";

function FileManagement() {
  const [files, setFiles] = useState([]);

  // 검색어 상태
  const [searchTerm, setSearchTerm] = useState("");

  const fileInputRef = useRef(null);

  const handleClick = () => {
    fileInputRef.current.click();
  };

  useEffect(() => {
    const fetchFiles = async () => {
      try {
        const response = await axios.get("/api/files");
        // 1. API 응답 데이터를 프론트엔드에서 사용하기 좋은 형태로 가공합니다.
        const formattedFiles = response.data.map((file) => ({
          id: file.id,
          name: file.filename,
          url: file.url,
          date: new Date().toLocaleDateString(), // 임시 날짜
        }));
        setFiles(formattedFiles);
      } catch (error) {
        console.error("Error fetching files:", error);
      }
    };

    fetchFiles();
  }, []);

  const filteredFiles = useMemo(() => {
    return files.filter((file) => {
      // 검색어 조건 확인 (대소문자 구분 없이)
      const matchesSearch = file.name
        .toLowerCase()
        .includes(searchTerm.toLowerCase());

      return matchesSearch;
    });
  }, [files, searchTerm]); // 의존성 배열

  const handleFileChange = async (e) => {
    const selectedFiles = Array.from(e.target.files);
    if (selectedFiles.length > 0) {
      for (const file of selectedFiles) {
        const formData = new FormData();
        formData.append("file", file);

        try {
          const response = await axios.post("/api/upload", formData, {
            headers: { "Content-Type": "multipart/form-data" },
          });

          // 업로드 성공하면 목록에 추가
          setFiles((prevFiles) => [
            ...prevFiles,
            {
              id: response.data.id,
              name: response.data.filename,
              url: response.data.url,
              date: new Date().toLocaleDateString(),
            },
          ]);
        } catch (error) {
          console.error("업로드 실패:", error);
        }
      }
    }
  };

  return (
    <Container fluid>
      {/* 메인 컨텐츠 영역 */}
      <main className="container">
        {/* 페이지 제목 및 파일 업로드 버튼 */}
        <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
          <h1 className="h2">내 파일</h1>
          <div className="btn-toolbar mb-2 mb-md-0">
            <input
              type="file"
              style={{ display: "none" }}
              ref={fileInputRef}
              onChange={handleFileChange}
              multiple={true}
              accept=".csv, .xlsx, .xls"
            />
            <Button variant="primary" onClick={handleClick}>
              <Upload className="me-2" />
              Upload File
            </Button>
          </div>
        </div>

        {/* 검색창 */}
        <Row className="mb-3">
          <Col md={12}>
            {/* 파일 검색 입력창 */}
            <InputGroup>
              <InputGroup.Text>
                {/* 아이콘 */}
                <Search />
              </InputGroup.Text>
              <Form.Control
                type="text"
                placeholder="파일 검색..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </InputGroup>
          </Col>
        </Row>

        {/* 파일 목록을 카드로 표시하는 영역 */}
        <Row xs={1} sm={2} md={3} lg={4} xl={5} className="g-4">
          {filteredFiles.map((file) => (
            <Col key={file.id}>
              <FileCard file={file} />
            </Col>
          ))}
        </Row>
      </main>
    </Container>
  );
}

export default FileManagement;
