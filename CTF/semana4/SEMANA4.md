# Semana 4

## Desafio 1

Informação recolhida do site:

- 5.8.1 wordpress
- WooCommerce 5.7.1
- Booster for WooCommerce 5.4.3

Procurando vulneralbilidades nestes produtos nestas versões específicas encontramos os seguintes CVE que podiam estar relacionados com o ataque que pretendiamos fazer:

- CVE-2021-39203
- CVE-2022-21664
- CVE-2022-21661
- CVE-2021-34646 &rarr; melhor opção

Assim, considerando o CVE acima, encontramos a flag: **flag{CVE-2021-34646}**

## Desafio 2

Em bases de dados, é comum o admin estar com id=1 pelo que é a esse id que queremos aceder!

Qual a vulnerablidade? O processo de validação do e-mail tem uma fraqueza quanto à geração do token para dar reset à password &rarr; a geração de token é previsível!
Conseguimos assim fazer-nos passar por outro utilizador. O link abaixo explica o processo para obter esse token:

<https://www.wordfence.com/blog/2021/08/critical-authentication-bypass-vulnerability-patched-in-booster-for-woocommerce/>

Como atacar? Fazemos um pedido de reset de conta na página Home com o atributo php **wcj_user_id4**.

Como o script do site usa algo do estilo: ```md5(time())``` para gerar o token para verificar o email, nem precisamos de ter acesso ao mail! Basta forcar o pedido de reenvio e ter o timing certo para gerar o nosso md5 que depois pode ser usado para forçar a entrada ao fazer a confirmacao de ativação do email que nos faz login diretamente para a conta!

Passos:

**1-** Fazer um pedido de reenvio de email de confirmação para user de id=1 acedendo ao link: <http://ctf-fsi.fe.up.pt:5001/?wcj_user_id=1>

**2-** Vendo o tempo que demorou (ou controlando pela consola do browser o pedido de envio e convertendo para epoch tentando correr um script em simultâneo ao entrar no link. Podemos usar o seguinte script para o efeito:

```php
$code = base64_encode(json_encode( array( 'id' => 1, 'code' => (md5 (time())) )));
```

**3-** Com isto fizemos engenharia reversa do token de confirmação de ativação de um email associado a uma conta. Agr basta "ativar" o email! Para tal usamos o link: <http://ctf-fsi.fe.up.pt:5001/wp-login.php?wcj_verify_email=MY_TOKEN> onde substituimos o ```MY_TOKEN``` pelo valor guardado em ```$code```!

**4-** Finalmente entramos como admin no site. Depois vamos ao canto superior direito ao perfil do admin e entramos na consola do wordpress onde tem um post único com a flag: **flag{please don't bother me}**
