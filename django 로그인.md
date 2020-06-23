# django 로그인

```
python manage.py migrate
```



장고에서는 해싱이라는 기능으로 비밀번호를 암호화한다.

`**해시**: goTH5D**************************************`

장고는 패스워드를 받고 데이터베이스에 저장하려고 하는데,

관리자 계정에서 비밀번호를 볼 수 있기 때문에 암호화 해서 한다.

그런데, 이것을 복호화 한다면 암호를 알아볼 수 있다.

`https://www.convertstring.com/ko/Hash/SHA256`

sha256해시

`hello -> 2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824`



또한, 솔트라는 것이 있는데....

**`솔트**: aTXewj****** `

솔트를 통해 암호가 달라지게 되면 해시 값도 달라져 비밀번호의 암호화를 지킬 수 있게 된다. -> 18만번을 반복한다.



![image](https://user-images.githubusercontent.com/58652391/85352884-f4a24b80-b541-11ea-94bd-3302bda21de5.png)



![image](https://user-images.githubusercontent.com/58652391/85353584-8ced0000-b543-11ea-90ea-5e7652dbc2f0.png)

