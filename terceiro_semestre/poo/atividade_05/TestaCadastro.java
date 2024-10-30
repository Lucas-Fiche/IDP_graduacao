package atividade_05;

import java.util.Scanner;

public class TestaCadastro {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        PessoaService pessoaService = new PessoaService(10);  

        int opcao;
        do {
            System.out.println("\n--- Menu ---");
            System.out.println("1. Cadastrar uma pessoa");
            System.out.println("2. Imprimir cadastros");
            System.out.println("3. Remover uma pessoa");
            System.out.println("4. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    cadastrarPessoa(pessoaService, scanner);
                    break;
                case 2:
                    pessoaService.imprimirCadastro();
                    break;
                case 3:
                    removerPessoa(pessoaService, scanner);
                    break;
                case 4:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        } while (opcao != 4);

        scanner.close();
    }

    private static void cadastrarPessoa(PessoaService pessoaService, Scanner scanner) {
        System.out.println("Escolha o tipo de pessoa para cadastrar:");
        System.out.println("1. Gerente");
        System.out.println("2. Funcionário");
        System.out.println("3. Cliente");
        System.out.println("4. Cliente VIP");
        int tipo = scanner.nextInt();
        scanner.nextLine(); 

        System.out.print("Digite o nome: ");
        String nome = scanner.nextLine();

        System.out.print("Digite o dia de nascimento: ");
        int dia = scanner.nextInt();
        System.out.print("Digite o mês de nascimento: ");
        int mes = scanner.nextInt();
        System.out.print("Digite o ano de nascimento: ");
        int ano = scanner.nextInt();
        scanner.nextLine(); 
        Data nascimento = new Data(dia, mes, ano);

        try {
            switch (tipo) {
                case 1:
                    System.out.print("Digite o salário do gerente: ");
                    float salarioGerente = scanner.nextFloat();
                    scanner.nextLine(); 
                    System.out.print("Digite a área do gerente: ");
                    String area = scanner.nextLine();
                    Gerente gerente = new Gerente(nome, nascimento, salarioGerente, area);
                    pessoaService.cadastrarPessoa(gerente);
                    break;

                case 2: 
                    System.out.print("Digite o salário do funcionário: ");
                    float salarioFuncionario = scanner.nextFloat();
                    Funcionario funcionario = new Funcionario(nome, nascimento, salarioFuncionario);
                    pessoaService.cadastrarPessoa(funcionario);
                    break;

                case 3: 
                    System.out.print("Digite o código do cliente: ");
                    int codigo = scanner.nextInt();
                    Cliente cliente = new Cliente(nome, nascimento);
                    cliente.setCodigo(codigo);
                    pessoaService.cadastrarPessoa(cliente);
                    break;

                case 4: 
                    System.out.print("Digite o percentual de desconto do cliente VIP: ");
                    double percentualDesconto = scanner.nextDouble();
                    ClienteVip clienteVip = new ClienteVip(nome, nascimento, percentualDesconto);
                    pessoaService.cadastrarPessoa(clienteVip);
                    break;

                default:
                    System.out.println("Tipo inválido.");
            }
        } catch (QuantidadeExcedidaException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    private static void removerPessoa(PessoaService pessoaService, Scanner scanner) {
        System.out.print("Digite o índice da pessoa que deseja remover: ");
        int indice = scanner.nextInt();
        pessoaService.removerPessoa(indice);
    }
}
