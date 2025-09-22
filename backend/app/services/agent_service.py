import pandas as pd
import traceback
from fastapi import HTTPException
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

from app.core.config import settings

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    temperature=0,
    google_api_key=settings.GOOGLE_API_KEY,
    convert_system_message_to_human=True
)

def excel_agent(file_path: str, query: str) -> str:
    print(f"사용자 질문: {query}")
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        return HTTPException(status_code=404, detail="요청하신 파일을 찾을 수 없습니다.")
    except Exception as e:
        return HTTPException(status_code=400, detail="엑셀 파일을 처리하는 중 오류가 발생했습니다.")
    
    try:
        # LLM과 DataFrame을 사용하여 Pandas 에이전트를 생성
        agent = create_pandas_dataframe_agent(
            llm=llm,
            df=df, verbose=True,
            agent_executor_kwargs={"handle_parsing_errors": True}, # 파싱 에러 발생 시 재시도)
            allow_dangerous_code=True
        )
        result = agent.invoke({"input": query})

        return result.get("output", "죄송합니다. 질문에 대한 답변을 생성하지 못했습니다.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"질문에 대한 답변 생성 중 오류가 발생했습니다. 서버 로그를 확인해주세요. (오류: {e})")