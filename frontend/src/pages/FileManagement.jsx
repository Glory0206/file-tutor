import React, { useState, useMemo } from "react";
import { Container, Row, Col, Button, Form, InputGroup } from "react-bootstrap";
import FileCard from "../features/file-management/components/FileCard";
import FilterButtons from "../features/file-management/components/FilterButtons";

import { Search, Upload } from "react-bootstrap-icons";

const FILTER_CATEGORIES = {
  ALL: "All",
  DOCUMENTS: "Documents",
  OTHERS: "Others",
};

const files = [
  {
    id: "d1a2b3c4-001",
    name: "Research Paper 1.pdf",
    date: "Oct 26, 2023",
    type: "doc",
    image:
      "https://lh3.googleusercontent.com/aida-public/AB6AXuDVtGN2rbNl_EiCtHhnaHinOCHAQ_zFjeLCSLHz2WhyZQKqcA0-b_cOY3RfwoK5XAheI9zbVj9r5A5lBG2X2yGHpXrl77TGazLIAriglQi7kH9c20hjPtj-WS6TmcJrFz2gs04aQAH2Y9wXtu1EuAHfAS-mTQAhUvZMeLSBUwNOx3u-UoY-kz77tXsqrmq01gjwklq2j975oOirfhADKq2UbEGWKF3Fz81r-PhuHP1aW1pxxYsB_JoGx2zYK1ocxF_kH-ComgKFPX8",
  },
  {
    id: "d1a2b3c4-002",
    name: "Presentation.pptx",
    date: "Oct 25, 2023",
    type: "doc",
    image:
      "https://lh3.googleusercontent.com/aida-public/AB6AXuAJtlyQdo_D8yIZZSuK6geo8Fl8hjilBbvSkrPlKMk5_WMMCIqvml-YvsAvtq62_uRw5YharrlhurYoZ4H54Ac7zKRvMaW51HPsD13SuKecvnPpSZJlTgKACENBq5XLJFkjcxHW53us6ULy2K7jL4qFEH_7ADmlzi42WqbGbabdh77SGXAwi_iXG-MNiHtl4zNYR0RF2MzsviJuAsHPaSigKJedLRDWQXUxmQ9qHvMUCMU76kpqd4reqhKGioSOjFtjoM5OUltVTtI",
  },
  {
    id: "d1a2b3c4-005",
    name: "Assignment 2.zip",
    date: "Oct 22, 2023",
    type: "other",
    image:
      "https://lh3.googleusercontent.com/aida-public/AB6AXuCfls73gisi40i0-swL-LjqO_j15GSyI4J2gJcpdiJqpYN94Hxa9VaWoO3TyJrGpgDSvFVpkzh0IxrffI8bczEpdFbuq6Z7LjrOYO_eHP6MR6hGzCfesMA1k2ZJOeV9QTW7DN9lykTE9L9bY9CAeEjRTHOhIDE5CTe27SyJneb_YOH9juXA_A50V3rPDKNRHYndXayEEz8pnYzobWweVWQD6bXpsmCXMo51DHaZxAT6YDY48mUoh_ZQUR-kruUZvwzIa0Q5SCuGqjg",
  },
];

function FileManagement() {
  // 현재 선택된 필터 상태
  const [filter, setFilter] = useState(FILTER_CATEGORIES.ALL);
  // 검색어 상태
  const [searchTerm, setSearchTerm] = useState("");

  const filteredFiles = useMemo(() => {
    return files.filter((file) => {
      // 카테고리 필터 조건 확인
      const matchesFilter =
        filter === FILTER_CATEGORIES.ALL ||
        (filter === FILTER_CATEGORIES.DOCUMENTS && file.type === "doc") ||
        (filter === FILTER_CATEGORIES.OTHERS && file.type === "other");

      // 검색어 조건 확인 (대소문자 구분 없이)
      const matchesSearch = file.name
        .toLowerCase()
        .includes(searchTerm.toLowerCase());

      return matchesFilter && matchesSearch;
    });
  }, [files, filter, searchTerm]); // 의존성 배열

  return (
    <Container fluid>
      {/* 메인 컨텐츠 영역 */}
      <main className="container">
        {/* 페이지 제목 및 파일 업로드 버튼 */}
        <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
          <h1 className="h2">내 파일</h1>
          <div className="btn-toolbar mb-2 mb-md-0">
            <Button variant="primary">
              <Upload className="me-2" />
              Upload File
            </Button>
          </div>
        </div>

        {/* 검색창 및 필터 버튼 */}
        <Row className="mb-3">
          <Col md={8}>
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
          <Col md={4} className="d-flex justify-content-end">
            {/* 파일 타입 필터 버튼 그룹 */}
            <FilterButtons
              filter={filter}
              setFilter={setFilter}
              FILTER_CATEGORIES={FILTER_CATEGORIES}
            />
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
