import { Button } from "react-bootstrap";

// filter: 현재 선택된 필터 값
// setFilter: 필터 값을 변경하는 함수
// FILTER_CATEGORIES: 필터 종류를 담고 있는 객체
function FilterButtons({ filter, setFilter, FILTER_CATEGORIES }) {
  const buttons = [
    { label: "모든 파일", category: FILTER_CATEGORIES.ALL },
    { label: "문서", category: FILTER_CATEGORIES.DOCUMENTS },
    { label: "기타", category: FILTER_CATEGORIES.OTHERS },
  ];

  return (
    <div className="btn-group">
      {buttons.map(({ label, category }) => (
        <Button
          key={category} // 각 버튼에 고유한 key 부여
          variant={filter === category ? "primary" : "outline-secondary"} // 현재 필터와 일치하면 'primary' 스타일 적용, 그렇지 않으면 'outline-secondary' 스타일 적용
          onClick={() => setFilter(category)} // 버튼 클릭 시 해당 카테고리로 필터 변경
        >
          {label}
        </Button>
      ))}
    </div>
  );
}

export default FilterButtons;
