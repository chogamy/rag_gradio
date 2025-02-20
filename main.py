import gradio as gr
import requests


def query_api(user_input):
    # API 엔드포인트 URL
    api_url = "<YOUR_RAG_API_URL"

    data = {"user_key": "rag_test", "question": user_input}

    # POST 요청 보내기
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        # API에서 반환된 데이터 처리
        response = response.json()
        generation_result = response[0]["result"][0]["answer"]
        # tokens = (
        #     response[0]["result"][0]["tokens"]
        #     if "tokens" in response[0]["result"][0].keys()
        #     else 0
        # )
        # exec_time = response[0]["result"][0]["exec_time"]
        search_result = response[0]["result"][0]["all_context"]
        return search_result, generation_result
    else:
        return "API 요청 실패", "응답을 받을 수 없습니다."


# Gradio 인터페이스 설정
iface = gr.Interface(
    fn=query_api,
    inputs=gr.Textbox(label="입력 텍스트"),
    outputs=[gr.Textbox(label="검색 결과"), gr.Textbox(label="생성된 답변")],
    title="RAG 시스템",
    description="텍스트를 입력하면 검색 결과와 생성된 답변을 보여줍니다.",
)


if __name__ == "__main__":
    iface.launch(share=True)
