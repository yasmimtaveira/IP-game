# 🧟 ESCAPE THRILLER - Projeto de Introdução a Programação

## 🫂 Equipe:
* Ayllane Maria Silva de Santana \<amss\>
* Júlia Almeida Brainer Dantas \<jabd\>
* Larissa Paiva dos Santos \<lps8\>
* Livia dos Santos Ferreira \<lsf4\>
* Yasmim Taveira Lopes \<ytl\>


## 📜 Descrição
**ARQUITETURA DO PROJETO:**

IP-game (diretório principal)
 |
 | - README.md (Arquivo padrão do GitHub que contém o relatório do projeto)
 |
 | - sons (Pasta com os arquivos .mp3 (música de fundo) e .wav (efeitos sonoros))
 |
 | - sprites (Pasta com todas as imagens e sprites usadas (tela de fundo, inicio, personagens, etc.)
 |
 | - constantes.py (código com algumas constantes como as dimensões da tela)
 |
 | - main.py (Arquivo do código base, onde ocorre o loop principal)
 |
 | - microfone2.py (Arquivo da classe Microfone) 
 |
 | - personagem.py (Arquivo da classe Personagem)
 |
 | - relogio.py (Arquivo da classe Relogio)
 |
 | - sapato.py (Arquivo da classe Sapato)
 |
 | - zumbi.py (Arquivo da classe Zumbi)
 |
 | - telas.py (Arquivo com as funções da tela inicial, game over e vitória)
 |
 | - prototipo.py (código inicial dos primeiros passos do projeto)


## 🎮 Como jogar
* **Antes de rodar o jogo, siga os passos a seguir:**

1- instale o python, na versão 3.8+

2- instale o pygame, a principal biblioteca utilizada na criação do jogo, necessária para rodá-lo

3-

## 🕹️ Telas
Capturas de tela do sistema funcionando:

**Tela inicial:**

![Telainicial](https://github.com/user-attachments/assets/8f7814c6-c605-4770-adad-c61fe973aa74)


**Menu do jogo:**

<img width="800" height="480" alt="tela_instruções" src="https://github.com/user-attachments/assets/d06f9635-d7e4-48ca-bafd-57611fe3b8f2" />


**Mapa do jogo:**

<img width="1361" height="857" alt="Captura de tela 2025-12-17 203809" src="https://github.com/user-attachments/assets/c13e3192-f430-4aa2-a678-325ea6596f2d" />


**Tela da vitória:**

<img width="800" height="480" alt="gameover_vitoria" src="https://github.com/user-attachments/assets/69487196-db89-48e0-b772-b57ddf9c7fbd" />


**Tela da derrota:**

<img width="800" height="480" alt="gameover_derrota" src="https://github.com/user-attachments/assets/aedaf8a4-9217-4a16-9e2e-fd091ff7311a" />


## 💻 Ferramentas utilizadas
* **PYGAME:** Principal biblioteca que tornou possível a criação do jogo de forma acessível. Muito utilizada, principalmente para o desenvolvimento de jogos 2d. 

* **GITHUB:** Foi utilizado para a organização do código- fonte, facilitando o trabalho em em equipe, controlando diversas versões. Ademais, garantiu a segurança do código, evitando assim a perdas durante a realização do trabalho. 

* **Pixel art:** A plataforma foi utilizada para adquirir algumas sprites e modificar cenários do jogo. 

* **IA:** Usada apenas para a criação  da sprite do Rei do Pop e do mapa principal do jogo. 

* **The Mushroom Kingdom:** Plataforma usada para adquirir os efeitos sonoros do jogo.

* **VS code:** Editor de código-fonte utilizado para o desenvolvimento e modularização de toda a programação do jogo

* **Biblioteca os:** usada para encontrar os endereços dos arquivos do diretório.

* **Biblioteca sys:** função exit usada para fechar a janela do jogo


## 📝 Divisão de tarefas
* Larissa e Yasmim - código base, classes e objetos;
* Lívia - tema, slide, código e imagem das telas;
* Júlia e Ayllane - sprites, pesquisa de arquivos e relatório.


## 📚 Conceitos utilizados
* **Estruturas condicionais:** utilizadas para checagem da condição de vitória ou derrota, além na organização das telas do jogo, a verificação das teclas acionadas pelo usuário, etc.

* **Estruturas de repetição:** o jogo acontece num loop infinito (while) que contém outras repetições para as telas do jogo, e o uso do "for" foi crucial para que houvesse a verificação de eventos.

* **Funções:** utilizadas para facilitar a leitura do código e deixá-lo otimizado, como as telas e a função de restart das variáveis do jogo.

* 	**Estruturas de dados:** uso de tuplas para armazenar dados como código RGB de cores.

* **Programação Orientada a Objeto (POO):** criação de classes com atributos e métodos para conseguirmos instanciar objetos (Michael, zumbis, coletáveis), desenhá-los na tela e manipular os mesmos.


## ⚠️ Desafios e lições
Esta seção tem como objetivo apresentar os principais desafios e erros enfrentados durante o desenvolvimento do projeto, bem como as lições aprendidas ao longo de sua execução.

* **Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?**

Não houve erros significativos que comprometessem a realização do projeto. Desde as etapas iniciais, o nosso grupo manteve atenção constante à organização e ao desenvolvimento do trabalho. Ao longo do processo, foram realizadas revisões frequentes do código e da estrutura do projeto, permitindo a identificação de possíveis inconsistências e sua correção antes que impactassem negativamente o andamento do jogo. Além disso, o acompanhamento das sugestões fornecidas pelos monitores e o trabalho colaborativo entre os integrantes contribuíram para a manutenção da qualidade do projeto.

* **Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?**

Os maiores desafios enfrentados durante o projeto foram a organização da modularização, a identificação e correção de bugs e a aplicação dos conceitos de Programação Orientada a Objetos (POO) utilizando a biblioteca Pygame. Para lidar com essas dificuldades, o grupo realizou revisões constantes do código, testes frequentes e ajustes nas classes e módulos, além de considerar as sugestões dos monitores, o que possibilitou a continuidade e a conclusão do projeto.)

* **Quais as lições aprendidas durante o projeto?**

Durante a realização do projeto, foi possível colocar em prática os conceitos abordados na disciplina de Introdução à Programação. Além disso, o grupo adquiriu conhecimentos fundamentais para o desenvolvimento do jogo utilizando a biblioteca Pygame, como Programação Orientada a Objetos (POO), classes, atributos e métodos, criação de objetos a partir de classes, herança, polimorfismo, uso de bibliotecas em Python, modularização e os principais comandos do Git. Ademais, o projeto reforçou a importância do trabalho em equipe e das revisões constantes do código, contribuindo para o desenvolvimento e a conclusão do projeto.
