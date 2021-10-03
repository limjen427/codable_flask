# codable_flask
'21 fall codable project (todo, reminder, qr) with flask

10/3/21
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

9/26/21
    목적: 웹사이트에 todo, reminder, qr code를 flask를 통해 구현하려함
    한 일: 
        --> flask 셋업 완료 및 기초 프로젝 진행(flask에 적응하기 위함)
        --> git repo set up & create each branches

    다음주 목표:
        --> localhost 열고 웹사이트 만들기
        --> qr generator 최대한 완성
        --> qr 인식기 고려중