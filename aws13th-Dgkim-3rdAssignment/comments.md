Comments(댓글)


1.댓글 목록 조회
GET /posts/{postid}/commets

2.댓글 작성
POST /comments

/posts/{postId}/comments
댓글은 포스트에 종속되어 있기 때문에 posts리소스에 묶는게 논리적


3.댓글 수정
PUT /comments/{commentid}

4.댓글 삭제

DELETE /commets/{commentidid}

5.내가 쓴 댓글 목록

GET /users/me/comments


댓글 목록 조회,댓글 작성,댓글 수정,댓글 삭제,내가 쓴 댓글 목록


작성 POST /comments 로 리소스를 comments에 집중하여 공통로직으로 처리하며 postid를 바디로 처리하여 url의존도를 낮춘 방식
작성 POST /comments/posts/{postid} 코멘트 리소스에 집중하면서도, 종속의 관계를 일부 보여준다. 코멘트가 다른곳에도 종속되어 사용될떄 유리하다.
작성 POST /posts/{postid}/comments 코멘트를 posts의 종속으로 확정하여, 게시글의 상태에 따라 코멘트 생성 여부가 확실하게 정해진다.