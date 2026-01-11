"""
2026-01-05 웹 및 rest api 수업(네트워크 기초 일부).md 수업 - 웹, http
"""
# from http.server import HTTPServer, BaseHTTPRequestHandler
# import json
#
#
# # 요청을 처리할 핸들러 클래스 정의 (웨이터의 역할)
# class MyHandler(BaseHTTPRequestHandler):
#
#     # GET 요청이 들어왔을 때 실행되는 메서드
#     def do_GET(self):
#         # 1. 요청 경로 확인 (주문 내용 확인)
#         if self.path == '/api/user':
#             # 응답할 데이터 준비 (주방에서 요리)
#             data = {
#                 "name": "임태종",
#                 "nickname": "jeff",
#                 "role": "Instructor"
#             }
#
#             # 2. 응답 헤더 작성 (영수증 작성)
#             self.send_response(200)  # 200 OK: 성공적으로 처리함
#             self.send_header('Content-Type', 'application/json')  # JSON 형식임을 명시
#             self.end_headers()  # 헤더 작성 끝
#
#             # 3. 응답 바디 작성 및 전송 (음식 서빙)
#             # 데이터를 JSON 문자열로 변환하고, 바이트로 인코딩하여 전송
#             self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
#         else:
#             # 정의되지 않은 경로로 요청이 온 경우 (없는 메뉴 주문)
#             self.send_response(404)  # 404 Not Found
#             self.end_headers()
#
#
# #
# # 메인 실행 블록
# if __name__ == '__main__':
#     # 서버 주소와 포트 설정 ([localhost:8000](http://localhost:8000))
#     server_address = ('', 8000)
#
#     # 서버 생성 (가게 오픈 준비)
#     httpd = HTTPServer(server_address, MyHandler)
#
#     print(f"🚀 Server is running on port 8000...")
#     print(f"   http://localhost:8000/api/user 로 접속해보세요.")
#
#     # 서버 실행 및 대기 (손님이 올 때까지 무한 대기)
#     httpd.serve_forever()

import json

# ============================================================
# 1. 기본 직렬화: 파이썬 딕셔너리를 JSON 문자열로 변환
# ============================================================

# jeff 사용자 정보를 담은 딕셔너리 생성
user_data = {
    "name": "jeff",           # 문자열 값
    "email": "[jeff@example.com](mailto:jeff@example.com)",
    "age": 30,                # 정수 값
    "is_active": True,        # 불리언 값 (JSON에서는 true로 변환됨)
    "skills": ["Python", "JavaScript", "SQL"]  # 리스트 값
}

# json.dumps(): 딕셔너리 → JSON 문자열
# dumps의 's'는 string을 의미합니다
json_string = json.dumps(user_data,indent=4)

with open("user_data2.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, ensure_ascii=False, indent=4)

json.dump(user_data, open("user_data.json", "w",encoding="utf-8"),ensure_ascii=False, indent=4)

print(type(json_string))  # <class 'str'> - 문자열 타입
print(json_string)
# 출력: {"name": "jeff", "email": "[jeff@example.com](mailto:jeff@example.com)", "age": 30, ...