Programa para coletar um CEP indicado.

NOTA: A base de CEPS (ceps.txt) não está completa. (motivos, bases completas requerem pagamento ou são difusas demais para implementações simples)

Critérios de aceitação:

        · Dado um CEP válido, deve retornar o endereço correspondente
        · Dado um CEP válido, que não exista o endereço, deve substituir um dígito da direita para a esquerda por zero até que o endereço seja localizado (Exemplo: Dado 22333999 tentar com 22333990, 22333900 …)
        · Dado um CEP inválido, deve retornar uma mensagem reportando o erro: "CEP inválido"O que se espera para as questões 1  - dicas e direcionamentos:
      	 	· Os serviços devem receber e responder JSON;
      	 	· Faça o uso de Mocks principalmente nos testes;
       		· Os dados dos CEPs podem ser "Mocados";
       	 	· Pense em como documentar os cenários desenvolvidos (Testes sempre são uma boa forma de documentar);
       	 	· Ao finalizar o desenvolvimento você pode compartilhar o código pelo Github ou de outra maneira que preferir (como arquivo compactado). Se possível, em caso de arquivo compactado, envie o mesmo para um virtual drive e compartilha o link na prova;
        	· Fique a vontade para entrar em contato e tirar dúvidas;
        	· Juntamente com o Código, deve-se documentar a estratégia utilizada para a criação da aplicação, a arquitetura utilizada e os padrões. A documentação pode ser feita via GIT/Bitbucket ou adicionado no HackerRank. Isto faz parte da avaliação da prova.
        	· Em caso de uso do Git/Bitbucket não esqueça de criar o .gitignore.


Documentação está localizada na pasta "Documentação", é composta do Arquivo word (Documentação.docx) <Principal>

O funcionamento do APP está descrito em melhores detalhes em (Funcionamento Doc.png) <imagem>

A relação cliente servidor está descrita em (Cliente-Servidor.png) <imagem>



Notas de implementação:

Não foi possível implementara funcionalidades do front end. As APIs e Scripts funcionam perfeitamente mas não consegui
implementar funcionalidades do front end pelos motivos:

TCC - A entrega final do TCC era dia 19/09, tive de fazer várias correções e logo não consegui trabalhar no app.
Provas - A semana de 21 a 25 é uma semana de provas, com o estado atual estamos trabalhando em EAD, logo tive de conciliar as atividades passadas pelos professores com a implementação.
Freelance - No momento estou trabalhando como freelance, tive de fazer alguns itens nesta semana, também conciliando com todos os outros.


Com isso dito, todas as APIs estão funcionais assim como scripts!