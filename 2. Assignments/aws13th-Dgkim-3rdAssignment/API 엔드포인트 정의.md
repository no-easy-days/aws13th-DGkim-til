# API 엔드포인트 정의서

# users
## 1.users(회원) 리소스
POST / users (새로운 페이지를 생성하니깐)
POST /auth/signup
## 2.로그인 
POST /users/login (user가 login이란 리소스로 토큰을 생성해서 상태를 변화시키니깐)
## 3.내 프로필 조회 
GET /users/me
## 4.프로필 수정 
PATCH /users/me
## 5.회원 탈퇴 
DELETE /users/me
## 6.특정 회원 조회
GET /userd/{userid}

# posts(게시글)
## 1.게시글 목록 조회
GET  /posts
## 2.게시글 검색
GET  /posts?search=keyword
## 3.게시글 정렬
GET  /posts?sort=creatdAT
## 4.게시글 상세 조회
GET  /posts/{postid}
## 5.게시글 작성
POST  /posts
## 6.게시글 수정
PATCH  /posts/{postid}
## 7.게시글 삭제
DELETE  /posts/{postid}
## 8.내가 쓴 게시글 목록
GET /users/me/posts
GET  /posts/me/posts

# comments(댓글)
## 1.댓글 목록 조회
GET /posts/{postid}/commets
## 2.댓글 작성
POST /posts/{postId}/comments
댓글은 포스트에 종속되어 있기 때문에 posts리소스에 묶는게 논리적
## 3.댓글 수정
PUT /comments/{commentid}
## 4.댓글 삭제
DELETE /commets/{commentidid}
## 5.내가 쓴 댓글 목록
GET /users/me/comments
GET /comments/me

# likes(좋아요)
## 1.좋아요 등록
POST /posts/{postid}/likes
POST /comments/{commentid}/likes
## 2.좋아요 취소
DELETE /posts/{postid}/likes
DELETE/comments/{commentid}/likes
## 3.좋아요 상태 확인
GET /posts/{postid}/likes
GET /comments/{commedtid}/likes
## 4.내가 좋아요한 게시글 목록
GET users/me/likes/posts
GET /likes/ms
좋아요 등록,좋아요 취소,좋아요 상태 확인,내가 좋아요한 게시글 목록

