## GitHub

- Commit - 버전 하나하나를 말함

- Repository 	- commit을 모아둔 저장소

- git은 파일을 추적 O / 폴더를 추적 X

- git 기본 원리 : git add . -> git commit -m "commit 이름" -> git push
- 

### - GitHub에 올릴 폴더 및 파일 생성

##### 1. C드라이브안에 TIL 이름의 폴더를 만든다. 												# TIL말고 다른 폴더명으로 해도 상관 X

​	- (CLI ver.) 터미널에서 <code> mkdir TIL</code>

​	- (GUI ver.) 내컴퓨터 -> C드라이브 -> 폴더생성



##### 2. TIL 폴더 경로로 들어가서 git init 을 한다.												# macOS = terminal / Windows는 Git bash

​	<code> $cd TIL </code>

​	<code> $git init </code>

​	(git init을 하고나서 TIL 폴더에서 숨겨진 파일을 보면 .git파일이 보인다.)

​	=> 숨겨진 파일 보는 단축키 : command + shift + .



##### 3. TIL 폴더 내에 파일 생성

​	<code>$ touch a.txt</code>																								# a.txt 대신 생성하고 싶은 파일명.확장자명

​	

##### 4. username / useremail 이름 설정 														# GitHub 이름과 이메일과 동일하게 설정

​	<code> $git config —global user.name “GitHub 이름”</code>

​	<code>$git config —global user.email “GitHub 로그인할 때이메일”</code>

(처음 설정할 때 한번만 하면된다!!)



### - GitHub에 업로드 방법

##### 5. Git bash / terminal 에서

​	<code>$ git add .</code>

​	<code>$ git commit -m “버전 이름”</code>

​	<code>$ git status</code>																									# 필수 명령어, 항상 모든 명령어 뒤에 상태 확인!!(생략 가능)

​	<code>$ git log </code>																										# git에 잘 기록되어있는지 확인(생략 가능)

​	<code>$ git remote add origin 올릴 깃허브주소입력</code>												   # github 주소와 연결

​	<code>$ git push</code>																										# github로 업로드

​	

 ##### 6. 처음 올릴 때는 6번 과정을 하고 다음부터 push할 경우에는

​	<code>$ git add.</code>

​	<code>$ git commit -m “버전 이름”</code>

​	<code>$ git status</code>																									# git에 잘 기록되어있는지 확인(생략 가능)

​	<code>$ git push</code>

(단, GitHub에서 repository가 바뀌면 6번과정부터 다시 해야함!!!!)



### GitHub에서 다운받기

##### 7. GitHub의 repository와 연결되있는 경우

<code>$ git pull</code>																											# GitHub의 repository에서 자료 다운받기

##### 8. GitHub의 repository와 처음 연결하는 경우

<code>git clone 깃허브주소 .</code>																					# 현재 상태의 폴더에 복제 (폴더 내부가 비어있어야 하는것 같음)



### GitHub - branch

##### 9. branch 생성 및 개념

<code>$ git branch 브랜치이름	</code>																				 # 브랜치 만들기

<code>$ git branch</code>																										# 브랜치 목록 확인

<code>$ git checkout 브랜치이름</code>																					# 브랜치 이동

![image](https://image.slidesharecdn.com/11-161011082550/95/11-git-basic-39-638.jpg?cb=1478094673)





### Gitignore

- GitHub로 업로드할 때, 올리고 싶지 않은 파일(개인정보, 파일 등)을 .ignore파일을 만들어서 관리

  ​	<code>$ mkdir .gitignore</code>

- https://gitignore.io/ : 개발자들이 많이쓰는 문서를 제공하는 사이트

  

  

   





