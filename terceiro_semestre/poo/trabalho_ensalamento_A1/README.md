# Trabalho A1 - Ensalamento

Escreva um programa em Java, utilizando orientação a objetos, para realizar a alocação de estudantes em turmas de uma instituição de ensino. Obs: estou chamando erroneamente essa operação de "ensalamento" por falta de termo melhor.

Nesta instituição, esse cenário é visto da seguinte forma:

Alunos e professores possuem algumas características em comum, no momento, destacamos apenas o "nome" (outros atributos serão incluídos nas próximas versões). Em outras palavras, aluno é uma pessoa e professor é uma pessoa;

Um professor tem a disciplina na qual ele é titular para ministrá-la;

Aluno é vinculado ao curso no qual ele está matriculado;

Um curso possui uma ou mais disciplinas associadas a ele;

Uma turma é a alocação de todos esses recursos e é feita pelo ensalamento:
turma possui um professor;
turma possui uma disciplina;
turma possui um ou mais alunos matriculados.

O programa deve:

- ter uma classe para cada conceito descrito no cenário acima;
os dados devem ser fixos no código-fonte (hard-coded) conforme listagem abaixo (obs: adotamos essa estratégia para facilitar a implementação do programa);

- a execução do ensalamento deve ser realizada por um método na classe Ensalamento;

- o método main deve apenas acionar a execução do ensalamento;

- o resultado do ensalamento deve ser apresentado para o resultado para o usuário.

Dados fornecidos:

Alunos
Alfredo - TI
Amélia - TI
Ana - ADM
Bruno - TI
Bentinho - ADM
Capitú - TI
Debra - TI
Ian - ADM
Iracema - TI
Joelmir - ADM
Julieta - TI
Luana - ADM
Luciana - TI
Majô - ADM
Maria - ADM
Norberto - TI
Paulo - ADM
Romeu - ADM
Wendel - TI
Zoey - TI
Professores
Mia - POO
Saulo - Estrutura de Dados
Paula - BI
Cursos
TI
ADM
Disciplinas
POO do curso de TI
Estrutura de Dados do curso de TI
BI do curso de ADM