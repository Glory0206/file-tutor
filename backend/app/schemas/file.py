from pydantic import BaseModel

# 파일의 기본 속성
class FileBase(BaseModel):
    filename: str

# 파일 생성 시 필요한 데이터
class FileCreate(FileBase):
    file_path: str # 서버에 저장된 실제 경로

# DB에서 읽어온 파일 데이터를 API 응답으로 보낼 때 사용
class File(FileBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True