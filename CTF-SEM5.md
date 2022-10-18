# Desafio 1

>mem_file é aberto pelo programa e lido

>se rescrevermos a variável meme_file conseguimos abrir um ficheiro à nossa escolha

>Existe um buffer-overflow ao escrever para o buffer. A escrita fora dos parámetros desejáveis permite rescrever o meme_file
podemos assim enganar o programa de forma a abrir o ficheiro que desejá-mos.

Escrever 20 carácteres seguidos de flag.txt

flag{8459a55....65}

# Desafio 2

> Foi colocado um valor entre o meme_file e o buffer que serve como verificação para possíveis rescritas. Esse valor não é possível escrever com o teclado.

> Conseguimos na mesma fazer rescrever o meme_file

> Existe um buffer-overflow. Neste caso temos de escrever o valor de proteção seguido da path do ficheiro da flag

Notas :

cast para apontadores de inteiros -> não relevante

usar convertor de string para conseguir o val -> convertor não viável

deadbeef in hex

DPS de algumas horas ...

para passar é impossível mandar pela bash (não é possível escrever esses carácters). Que mundo cruel!!!
solução ... mandar um ficheiro :)

user echo "1..20#"__flag.txt " > ex.txt

em que __ são os dois caracteres que n se consegue passar pela bash 
e #"__ == 0xfefc2223 (por ordem inversa por ser string)
e 1 .. 20, são os 20 chars iniciais

Flag conseguida ... {d36 ... ae80}
