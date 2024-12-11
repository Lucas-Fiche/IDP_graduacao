# Sistema de Escolaridade com Java e JDBC

## Descrição do Projeto

Este projeto implementa um sistema de gerenciamento de escolaridade utilizando **Java**, a API **JDBC** e o banco de dados relacional **H2**. O sistema realiza as seguintes operações:

- Gerenciamento de usuários (cadastrar, atualizar, excluir e autenticar);
- Gerenciamento de escolaridade (cadastrar, listar, atualizar e excluir);
- Autenticação do usuário através de matrícula e senha.

O sistema segue o paradigma de orientação a objetos e utiliza uma separação clara de responsabilidades (DAO, modelo, e aplicação principal).

---

## Tecnologias Utilizadas

- **Java 22**
- **JDBC (Java Database Connectivity)**
- **Banco de Dados H2 (em memória)**
- **Maven** para gerenciamento de dependências

---

## Estrutura do Projeto

### Pacotes e Arquivos

- **application**: Contém a classe principal `AplicacaoEscolaridade`.
- **model**: Contém as classes `Usuario` e `Escolaridade` que representam os modelos do sistema.
- **dao**: Contém as classes DAO (`UsuarioDAO` e `EscolaridadeDAO`) responsáveis pelas operações de acesso ao banco de dados.
- **database**: Contém a classe `DatabaseConnection` para gerenciar a conexão com o banco de dados e inicializar as tabelas.

---

## Configuração e Execução

### Pré-requisitos

- **Java JDK 22**
- **Maven** instalado e configurado

### Passo a Passo

#### 1. Clone o repositório do projeto

```bash
# Clone o projeto para sua máquina
$ git clone <URL_DO_REPOSITORIO>
$ cd <NOME_DO_DIRETORIO>
```

#### 2. Execute o Maven para instalar as dependências

```bash
$ mvn clean install
```

#### 3. Compile e execute o projeto

```bash
# Compile e execute o projeto
$ mvn exec:java -Dexec.mainClass="application.AplicacaoEscolaridade"
```

#### 4. Interaja com o sistema via terminal

- Escolha as opções exibidas no menu para autenticação, gerenciamento de usuários ou escolaridade.

---

## Funcionalidades

### Gerenciamento de Usuários

1. **Cadastrar**: Adiciona um novo usuário ao sistema.
2. **Atualizar**: Permite atualizar os dados do usuário logado.
3. **Excluir**: Remove o usuário do sistema.
4. **Autenticar**: Permite fazer login no sistema com matrícula e senha.

### Gerenciamento de Escolaridade

1. **Cadastrar**: Registra novas informações de escolaridade para o usuário logado.
2. **Listar**: Exibe todas as escolaridades vinculadas ao usuário logado.
3. **Atualizar**: Modifica informações de uma escolaridade existente.
4. **Excluir**: Remove uma escolaridade vinculada ao usuário logado.

---

## Estrutura do Banco de Dados

### Tabela `usuarios`

| Coluna    | Tipo         | Descrição                      |
| --------- | ------------ | ------------------------------ |
| matricula | INTEGER      | Número único de identificação  |
| senha     | VARCHAR(255) | Senha do usuário               |
| sobrenome | VARCHAR(255) | Sobrenome do usuário           |
| email     | VARCHAR(255) | Email do usuário               |
| telefone  | VARCHAR(20)  | Telefone de contato do usuário |

### Tabela `escolaridades`

| Coluna             | Tipo         | Descrição                              |
| ------------------ | ------------ | -------------------------------------- |
| id                 | INTEGER      | ID único da escolaridade               |
| instituicao        | VARCHAR(255) | Nome da instituição de ensino          |
| curso              | VARCHAR(255) | Nome do curso                          |
| duracao\_meses     | INTEGER      | Duração do curso em meses              |
| usuario\_matricula | INTEGER      | Referência à matrícula do usuário (FK) |

---

## Observações Importantes

1. O banco de dados **H2** é configurado para ser executado em memória. Ao reiniciar o sistema, os dados inseridos anteriormente serão apagados.
2. Certifique-se de que todas as dependências estão instaladas antes de executar o sistema.
3. Em caso de problemas, execute o Maven novamente com:

```bash
$ mvn dependency:tree
```

---

