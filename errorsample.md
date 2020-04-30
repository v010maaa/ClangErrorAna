ccコンパイラーエラーの特徴
1. セミコロン抜け
a. 
```shell
practice0.c:5:14: error: expected ';' after expression
printf("jjj")
             ^
             ;
1 error generated.
```

2. 括弧閉がない時
a. "\{" 
```shell
practice0.c:6:11: error: expected '}'
        return 0;
                 ^
practice0.c:3:16: note: to match this '{'
int main(void) {
               ^
1 error generated.
```

b. "("
```shell
practice0.c:5:13: error: expected ')'
printf("jjj";
            ^
practice0.c:5:7: note: to match this '('
printf("jjj";
      ^
1 error generated.
```

c. ""

```shell
practice0.c:5:8: warning: missing terminating '"' character [-Winvalid-pp-token]
printf("jjj);
       ^
practice0.c:5:8: error: expected expression
practice0.c:7:2: error: expected '}'
}
 ^
practice0.c:3:16: note: to match this '{'
int main(void) {
               ^
1 warning and 2 errors generated.
```

3 変数未定義
filename.c: In function 'main':
filename.c:8:17: error: 'e' undeclared (first use in this function)
scanf("%lf", &e);
^
filename.c:8:17: note: each undeclared identifier is reported only once for each function it appears in

4 ダブルクオーテーションがない時
filename.c: In function 'main':
filename.c:9:13: error: stray '\357' in program
printf(sum：%lf\n", d + e);
^
5 全角エラー
filename.c: In function 'main':
filename.c:5:30: error: stray '\343' in program
for(i=0; i<10; i++){　
^
filename.c:5:31: error: stray '\200' in program
for(i=0; i<10; i++){　
^
filename.c:5:32: error: stray '\200' in program
for(i=0; i<10; i++){　
^

6 打ち間違え関数
filename.c: In function 'main':
filename.c:8:10: warning: implicit declaration of function 'pintf'; did you mean 'printf'? [-Wimplicit-function-declaration]
pintf("\n");
^~~~~
printf
/tmp/ccydTXBB.o: In function 'main':
filename.c:(.text+0x3e): undefined reference to 'pintf'
collect2: error: ld returned 1 exit status

7 初期化エラーは出ない
