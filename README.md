# algebraic-expression-to-function
convert algebraic expression to funcional expression
将算数式转换为函数式的小工具

## Usage

```sh

$python f2f.py "{yourexpression}"

or

$./f2f.sh "{yourexpression}"

```

For example,input

```sh

$python f2f.py "A+b-x*(12.13+51^y)^1.4121"

or

$./f2f.sh "A+b-x*(12.13+51^y)^1.4121"

```

Your will get:

add(A,mius(b,muilt(x,power(add(12.13,power(51,y)),1.4121))))
