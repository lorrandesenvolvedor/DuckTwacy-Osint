![Timg](./adicionais/imagens/Timg.png)
_Uma ferramenta simples de busca, criada na linguagem python versão 3.11 em XXIII/V/MMXXVI d.C, pelo ainda Dev junior Lorran Da Conceição Dos Santos, ideia da ferramenta e apenas buscar por usuários e fazer pequenas varreduras, o código está aberto para melhorias, edições, etc..._

**INFORMAÇÕES**
A ferramenta contém 3 arquivos, estrutura simples, faz as requisições de maneira direta e verifica lendo que o site dependeu 200 e se respondeu com o nome de usuário em seu código (isso não é muito seguro pois ainda pode dar falso positivos.), a ferramenta funciona por linhas de comando e você pode verificar os comandos existentes utilizando --help ou -h

**COMANDOS PRONTOS E DICAS EXTRAS**
____________________________________________________________
![Aimg](./adicionais/imagens/Aimg.png)
-b [usuário] (Aqui ele irá buscar por apenas um único usuário nas plataformas listadas. Para buscar mais de um usuário e só você repetir o parâmetro por exemplo: **-b user1 -b user2** assim por diante.)
____________________________________________________________
![Bimg](./adicionais/imagens/Bimg.png)
-n [nome] -sn [sobrenome] (aqui é uma função de encontrar o email se alguém através de um primeiro nome, e um segundo nome, pode ser um nome e sobrenome por exemplo **-n Aline -sn Silva** a ferramenta irá fazer algumas combinações misturando caráteres do nome e sobrenome e irá imprimir apenas oque for encontrado)
____________________________________________________________
![Cimg](./adicionais/imagens/Cimg.png)
-vE [gmail@gmail.com] (aqui a ferramenta irá caçar em quais plataformas um endereço de email está registrado, utilizando a biblioteca holehe, irá caçar pelo email digitado em cerca de 100 plataformas ou mais, imprime tudo oque for encontrado, exemplo de uso: **vE user@gmail.com**)

____________________________________________________________
**BIBLIOTECAS NECESSARIAS PARA RODAR O PROGRAMA**


requests 


BeautifulSoup 


httpx 


holehe
