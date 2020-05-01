ccコンパイラーエラーの特徴
1. セミコロン抜け
a. 
```c
#include <stdio.h>

int main(void) {
	// Write your code here
        printf('%d',a)
	return 0;
}
```
```shell
practice0.c:5:14: error: expected ';' after expression
printf("jjj")
             ^
             ;
1 error generated.
```

2. 括弧閉がない時
a. "\{" 

```c
#include <stdio.h>

int main(void) {
	// Write your code here
        printf("jjj");
	return 0;
```
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
```c
#include <stdio.h>

int main(void) {
	// Write your code here
        printf("jjj";
	return 0;
}
```
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

```c
#include <stdio.h>

int main(void) {
	// Write your code here
        printf("jjj);
	return 0;
}
```
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

d. 括弧シングルクオ

```c
#include <stdio.h>

int main(void) {
	// Write your code here
        printf('jjj');
	return 0;
}
```

```shell
practice0.c:5:8: warning: multi-character character constant [-Wmultichar]
printf('jjj');
       ^
practice0.c:5:8: warning: incompatible integer to pointer conversion passing 'int' to parameter of type 'const char *' [-Wint-conversion]
printf('jjj');
       ^~~~~
/usr/include/stdio.h:318:43: note: passing argument to parameter '__format' here
extern int printf (const char *__restrict __format, ...);
                                          ^
practice0.c:5:8: warning: format string is not a string literal (potentially insecure) [-Wformat-security]
printf('jjj');
       ^~~~~
practice0.c:5:8: note: treat the string as an argument to avoid this
printf('jjj');
       ^
       "%s", 
3 warnings generated.
timeout: the monitored command dumped core
/bin/bash: line 1:     9 Segmentation fault      timeout 1 ./practice0 < practice0.in
```
3. 変数未宣言

```c
#include <stdio.h>

int main(void) {
	// Write your code here
	int a=0;
        printf("%d",a);
	return 0;
}
```

```shell
practice0.c:6:13: error: use of undeclared identifier 'a'
printf("%d",a);
            ^
1 error generated.

```

4. 定義していない関数
```c
#include <stdio.h>

int main(void) {
	// Write your code here
	int a=0;
	indd();
printf("%d",a);
	return 0;
}
```

```shell
practice0.c:6:2: warning: implicit declaration of function 'indd' is invalid in C99 [-Wimplicit-function-declaration]
        indd();
        ^
1 warning generated.
/tmp/practice0-5470a0.o: In function `main':
practice0.c:(.text+0x4): undefined reference to `indd'
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

5 打ち間違え関数

```c
#include <stdio.h>

int main(void) {
	// Write your code here
	int a=0;
        prinf("%d",a);
	return 0;
}
```
```shell
practice0.c:6:1: warning: implicit declaration of function 'prinf' is invalid in C99 [-Wimplicit-function-declaration]
prinf("%d",a);
^
1 warning generated.
/tmp/practice0-2c82a3.o: In function `main':
practice0.c:(.text+0xb): undefined reference to `prinf'
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

