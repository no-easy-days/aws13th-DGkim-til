users(회원) 리소스 

1.회원가입
POST / users (새로운 페이지를 생성하니깐)
헤더

바디
{
"email" : eewwqq1@daum.net,
"passward" : asd123,
"nickname" : eewwqq1
"profile_image" : ()
}

응답
성공 - 201 created
{

}

2.로그인 
POST /users/login (user가 login이란 리소스로 토큰을 생성해서 상태를 변화시키니깐)

헤더
Content-Type: application/json

Body
{
  "email": "dg@example.com",
  "password": "securePassword123"
}

응답 - 200 ok
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6...",
  "tokenType": "Bearer",
  "expiresIn": 3600
}


3.내 프로필 조회 
GET /users/id

헤더 Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6.

응답 - 200 ok

4.프로필 수정 
PUT /users/id

헤더

바디
 
응답 - 200 ok

5.회원 탈퇴 
DELETE /users/id

헤더

응답

6.특정 회원 조회
GET /userd/{id}

헤더 

응답 - 200 ok

{
  "status": "success",
  "data": {
    "id": "res_123",
    "name": "리소스 이름",
    "description": "리소스 설명",
    "created_at": "2026-01-04T12:00:00Z",
    "updated_at": "2026-01-04T12:00:00Z"
  }
}