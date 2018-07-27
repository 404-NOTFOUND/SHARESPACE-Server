# SHARESPACE-Server
SHARESPACE Server & Web app with Python Flask

## Server (REST API with Flask-RESTful)

### Newsfeed
서버에 있는 전체 이미지 중에서 무작위로 일정 개수의 이미지를 선택해 각각 제목과 이미지 URL을 제공한다.

### Image infomation
요청받은 이미지에 대한 정보를 제공한다.

- 제목
- 본문
- 태그
- 게시자 이름
- 이미지 URL

## Web app

### session
사용자 이름과 이메일을 받아 세션에 저장하는 방식으로 세션을 관리한다(세부적인 로그인 구현 생략).

```Python
session.get('username') # 사용자 이름 (str)
session.get('email') # 이메일 (str)
session.get('logged_in') # 로그인 상태 (bool)
```

### Google VR view
Google의 [VR view](https://developers.google.com/vr/develop/web/vrview-web) JavaScript API를 이용해서 360° 포토를 임베딩한다.

```HTML
<script src="https://storage.googleapis.com/vrview/2.0/build/vrview.min.js"></script>
```
