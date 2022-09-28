# Trabalho realizado na Semana #3

## Identificação (CVE-2021-4034)

- **Pwnkit**, trata-se de uma vulnerabilidade de escalação de privilégios que permite obter root access estando localizada na *polkit's pkexec* utility.

- *Polkit*, trata-se de uma package default instalada na maioria das distros principais de linux, pelo que um exploit teria um grande número de potenciais alvos.

- Um *out-of-bounds read* e um *out-of-bounds write* são possíveis devido a um *“off-by-one”* de uma variável de loop, criando a vulnerabilidade.

- Em adição, uma vulnerabilidade na forma como o programa lida com erros nos argumentos permite saltar uma instrução para limpar variáveis de ambiente.

## Catalogação

- Identificado a **2021-11-18**  mas apenas tornado público a **2022-01-25**. Descoberto por investigadores da empresa de segurança *Qualys* ao analisarem o código fonte do pacote.

- Não se conseguiu descobrir sobre possíveis recompensas pela descoberta, porém pelo relatório da *Qualys* vê-se que estava em sintonia com a *Red Hat* (desenvolvedora do pacote).

- Um ataque usando esta vulnerabilidade rompe com a integridade, disponibilidade e confidencialidade do sistema, tendo alcançado um **score de 7.8/10**.

- O score não é mais elevado visto o ataque necessitar acesso prévio ao sistema. A complexidade da vulnerabilidade é baixa mas com grande potencial para causar estragos.

## Exploit

- O facto da vulnerabilidade nos deixar escrever *out-of-bounds* permite manipular variáveis de ambiente quando não são dados argumentos ao programa.

- O *“off-by-one”* da variável de loop vai fazer com que seja executada uma variável de ambiente como um comando. 

- Conseguimos então executar código nosso ao utilizar uma determinada variável de sistema e elevar os privilégios (exploração de vulnerabilidade).

- Ao procurar na internet encontramos alguns casos de [automações](https://packetstormsecurity.com/files/166196/Polkit-pkexec-Local-Privilege-Escalation.html) (“a Metasploit module for the argument processing bug in the polkit pkexec binary”).

## Ataques

- Uma atualização do pacote foi rapidamente lançada, porém isso não impediu usuários com máquinas desatualizadas de sofrerem ataques.

- Há relatos de utilização desta vulnerabilidade para conduzir [Cryptocurrency botnets](https://thehackernews.com/2022/09/new-stealthy-shikitega-malware.html) que por sua vez, também tiveram automações. 

- Segundo a mesma fonte, houve um aumento de 75%, num ano, no número de ataques ransomware da *“familia”* deste novo ataque.

- Não é preciso esclarecer a gravidade e utilidade prática de acesso root e que, nas mãos erradas e com os alvos e ferramentas certas, pode levar a graves consequências.
