# Semana 10


## Desafio 1

Neste desafio reparamos rapidamente que um ataque XSS era possível:

![](alert_script.png)

![](alert_result.png)


Vamos então explorar esta vulnerabilidade para alcançar a flag. 
Nós sabemos que a página de admin é a mesma que a do utilizador. A única coisa que muda do ponto de vista do admin são os botões que são clicáveis para ele tomar a decisão. Essa decisão é depois apresentada passados uns 5s ao utilizador.


![image-1.png](./image-1.png)


## Desafio 2

- É possível fazer login, um teste à velociadade da net e dar ping de um host.
- Para dar ping de um host quase de certeza que é utilizado o utilitário ping do linux. Se a string que for enviada para o comando for controlada por nós então podemos executar um comando por nós desejado.

Ao testar se o ponto anterior de facto ocorria chegou-se à solução do desafio.

A ideia passa por chamar um comando por nós pretendido, neste caso cat /flags/flag.txt. Uma vez que a string dada de input é por nós controlada podemos correr dois comandos separando-os com ";".


NOTA: Outras possíveis soluções mais elegantes seriam ... ;cat /flags/flag.txt , |cat /flags/flag.txt, &cat /flags/flag.txt ...

Também é possível chegar à solução sem sequer chegar a abrir o site para introduzir o input, como por exemplo ... http://ctf-fsi.fe.up.pt:5000/tools/ping.php?target=%3Bcat+%2Fflags%2Fflag.txt

![](Desafio2_sem10_exploit.png)

![](Desafio2_sem10.png)






