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

응답 - 200 OK
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6...",
  "tokenType": "Bearer",
  "expiresIn": 3600
}






3.내 프로필 조회 
4.프로필 수정 
PUT /users
5.회원 탈퇴 
6.특정 회원 조회

