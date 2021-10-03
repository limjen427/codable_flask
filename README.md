# codable_flask
'21 fall codable project (todo, reminder, qr) with flask

진행상황:
Flask 공부
폴더 static, template을 만들어 Flask의 필수요소 구조화함
  --> static: Some CSS can be added to add style to the HTML layout you constructed.
  --> template: Templates are files that contain static data as well as placeholders for dynamic data. ex)html files
QR Code를 만듦 --> 이미지화 --> Flask에 QR Code 이미지 삽입

문제점:
local host를 public으로 바뀌지 않음 (flask run --host=0.0.0.0 실패) --> 로딩만 되고 창이 열리지 않음

계획:
Flask 계속 공부
non-local host로 바꿀 수 있도록 연구
todo를 flask에 구현하도록 노력
입력한 link를 qr로 구현하도록 노력