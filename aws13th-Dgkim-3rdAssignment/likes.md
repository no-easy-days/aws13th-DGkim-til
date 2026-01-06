likes(좋아요)


1.좋아요 등록
POST /likes 


2.좋아요 취소
PUT /likes

3.좋아요 상태 확인
GET /likes

4.내가 좋아요한 게시글 목록
GET users/me/likes/posts


좋아요 등록,좋아요 취소,좋아요 상태 확인,내가 좋아요한 게시글 목록

게시글 좋아요 등록	POST	/posts/{postId}/likes	특정 게시글에 좋아요 생성
게시글 좋아요 취소	DELETE	/posts/{postId}/likes	특정 게시글 좋아요 삭제
댓글 좋아요 등록	POST	/comments/{commentId}/likes	특정 댓글에 좋아요 생성
댓글 좋아요 취소	DELETE	/comments/{commentId}/likes	특정 댓글 좋아요 삭제
좋아요 상태 확인	GET	/posts/{postId}/likes/status	로그인한 유저의 좋아요 여부 확인
내가 좋아요한 글 목록	GET	/users/me/likes/posts	나가 좋아요 누른 게시글만 모아보기

게시글 좋아요	POST	/likes/posts/{postId}	특정 게시글에 좋아요 등록
게시글 좋아요 취소	DELETE	/likes/posts/{postId}	특정 게시글 좋아요 삭제
댓글 좋아요	POST	/likes/comments/{commentId}	특정 댓글에 좋아요 등록
댓글 좋아요 취소	DELETE	/likes/comments/{commentId}	특정 댓글 좋아요 삭제
내가 한 좋아요 목록	GET	/likes/me	내가 누른 모든 좋아요(글/댓글 통합 가능)





