# Sistema de Cadastro de Pessoas
Este projeto implementa um sistema de cadastro de pessoas conforme o diagrama de classes fornecido. O sistema permite o cadastro de objetos de diferentes subclasses da classe abstrata Pessoa, como Cliente, Funcionário e Gerente. Além disso, o sistema permite que o usuário acesse uma pessoa pelo índice no array de pessoas cadastradas e utiliza tratamento de exceção para proteger contra acessos indevidos.

# Funcionalidades
Cadastro de Pessoas: Permite o cadastro de objetos das subclasses Cliente, Funcionário e Gerente.
Impressão de Dados: Imprime os dados de todas as pessoas cadastradas.
Acesso por Índice: Permite que o usuário acesse uma pessoa cadastrada pelo índice e imprime seus dados.
Tratamento de Exceção: Implementa tratamento de exceção para impedir o acesso a índices inválidos no array de pessoas.
Estrutura de Classes
O projeto segue o diagrama de classes apresentado, que contém as seguintes classes principais:

Pessoa: Classe abstrata que contém os atributos nome e nascimento (um objeto Data), além do método abstrato imprimeDados().
Cliente: Subclasse de Pessoa, com o atributo adicional codigo.
Funcionario: Subclasse de Pessoa, com o atributo salario e um método para calcular o imposto.
Gerente: Subclasse de Funcionario, com o atributo area.
Data: Classe que armazena a data de nascimento de uma pessoa (dia, mês e ano).
CadastroPessoas: Classe responsável por armazenar e gerenciar o array de pessoas cadastradas.
TestaCadastro: Classe que contém o método main() para testar o sistema.
Execução do Programa
O programa funciona da seguinte maneira:

Cadastro de Pessoas: O sistema cadastra objetos das subclasses de Pessoa (por exemplo, Cliente, Funcionario, Gerente).
Impressão do Cadastro: Após o cadastro, o sistema imprime os dados de todas as pessoas cadastradas.
Acesso por Índice: O usuário pode inserir um índice para acessar os dados de uma pessoa específica no array. Se o índice for inválido, o programa exibe uma mensagem de erro.

## Exemplo de Saída:
Caso o usuário insira um índice válido:

Digite o índice da pessoa que você deseja acessar: 1
Dados da pessoa acessada:
Nome: Funcionario Exemplo
Salário: 5000.0
Caso o usuário insira um índice inválido:

Tratamento de Exceções
<br>
O tratamento de exceção foi implementado para garantir que o usuário não possa acessar índices inválidos no array de pessoas cadastradas. A exceção ArrayIndexOutOfBoundsException é capturada e tratada para evitar erros no programa e exibir uma mensagem apropriada ao usuário.