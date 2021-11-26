username/ useremail을 설정을 하고 나서

username과 useremail을 다른걸로 바꾸고 싶어서 초기화 한 후에 다시 설정할 수 있는 방법은 없는건가요??

아래 방법으로 변경하시면 됩니다.

**커밋 작성자(author) 설정**

```
$ git config --global user.email "메일주소"
$ git config --global user.name "유저네임"
```

- 커밋을 작성하는 사람이 누구인지 알아야하기 때문

지정된 설정 확인

```
$ git config --global -l
# $ git config --global --list
```