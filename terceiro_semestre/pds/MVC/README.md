# Arquitetura MVC
A arquitetura MVC (Model-View-Controller) é um padrão de design amplamente utilizado no desenvolvimento de software, especialmente em aplicações web. Ela promove a separação de preocupações, permitindo que as diferentes partes de uma aplicação sejam desenvolvidas, testadas e mantidas de maneira mais eficiente. O MVC divide a aplicação em três componentes principais: Model, View e Controller. Abaixo, explicamos cada um desses componentes.

## 1. Model
### Descrição
O Model representa a parte lógica da aplicação. Ele é responsável pela gestão dos dados e pelas regras de negócio. O Model é independente das outras partes da aplicação e não possui conhecimento sobre a interface do usuário ou como os dados serão exibidos.

### Funções
Gerenciar os dados da aplicação, incluindo a recuperação e armazenamento em bancos de dados.
Aplicar regras de negócio, validações e operações nos dados.
Notificar a View quando há alterações nos dados.

## 2. View
### Descrição
A View é a camada responsável pela apresentação da interface ao usuário. Ela exibe as informações, geralmente recebidas do Model, de forma compreensível e interativa. A View não realiza processamento de dados, apenas apresenta as informações.

### Funções
Renderizar dados do Model para o usuário.
Receber entradas do usuário (por meio de formulários, cliques, etc.) e passá-las para o Controller.
Atualizar a interface do usuário em resposta a mudanças nos dados.

## 3. Controller
### Descrição
O Controller atua como intermediário entre a View e o Model. Ele processa as entradas do usuário (como cliques e preenchimentos de formulário), interpreta essas ações e decide qual parte do Model deve ser consultada ou modificada. Após processar a entrada, o Controller atualiza a View com os novos dados.

### Funções
Receber e processar a entrada do usuário.
Chamar métodos do Model para atualizar os dados.
Selecionar a View apropriada para apresentar os dados ao usuário.