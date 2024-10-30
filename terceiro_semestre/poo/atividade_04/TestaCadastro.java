package atividade_04;

import java.util.Scanner;

public class TestaCadastro {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CadastroPessoas cadastro = null; 

        int opcao;
        do {
            System.out.println("\n--- Menu ---");
            System.out.println("1. Cadastrar pessoas");
            System.out.println("2. Imprimir cadastros");
            System.out.println("3. Remover uma pessoa");
            System.out.println("4. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    if (cadastro == null) { 
                        System.out.print("Digite o número de pessoas que deseja cadastrar: ");
                        int capacidade = scanner.nextInt();
                        cadastro = new CadastroPessoas(capacidade); 
                        System.out.println("Cadastro criado com capacidade para " + capacidade + " pessoas.");
                    }

                    cadastrarVariasPessoas(cadastro, scanner);
                    break;

                case 2:
                    if (cadastro == null || cadastro.getQtdAtual() == 0) {
                        System.out.println("Nenhuma pessoa cadastrada.");
                    } else {
                        cadastro.imprimeCadastro();
                    }
                    break;

                case 3:
                    if (cadastro == null || cadastro.getQtdAtual() == 0) {
                        System.out.println("Nenhuma pessoa cadastrada para remover.");
                    } else {
                        removerPessoa(cadastro, scanner);
                    }
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

    private static void cadastrarVariasPessoas(CadastroPessoas cadastro, Scanner scanner) {
        int vagasDisponiveis = cadastro.getCapacidade() - cadastro.getQtdAtual();
        if (vagasDisponiveis <= 0) {
            System.out.println("O cadastro já está cheio. Não é possível adicionar mais pessoas.");
            return;
        }

        System.out.println("\nHá " + vagasDisponiveis + " vagas disponíveis para cadastro.");
        int numeroDePessoas = vagasDisponiveis; 

        for (int i = 0; i < numeroDePessoas; i++) {
            System.out.println("\nCadastro da pessoa " + (cadastro.getQtdAtual() + 1) + ":");
            cadastrarPessoa(cadastro, scanner);
        }
    }

    private static void cadastrarPessoa(CadastroPessoas cadastro, Scanner scanner) {
        System.out.println("Escolha o tipo de pessoa para cadastrar:");
        System.out.println("1. Gerente");
        System.out.println("2. Funcionário");
        System.out.println("3. Cliente");
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

        switch (tipo) {
            case 1: 
                System.out.print("Digite o salário do gerente: ");
                float salarioGerente = scanner.nextFloat();
                scanner.nextLine(); 
                System.out.print("Digite a área do gerente: ");
                String area = scanner.nextLine();
                Gerente gerente = new Gerente(nome, nascimento, salarioGerente, area);
                cadastro.cadastraPessoa(gerente);
                break;

            case 2: 
                System.out.print("Digite o salário do funcionário: ");
                float salarioFuncionario = scanner.nextFloat();
                Funcionario funcionario = new Funcionario(nome, nascimento, salarioFuncionario);
                cadastro.cadastraPessoa(funcionario);
                break;

            case 3:
                System.out.print("Digite o código do cliente: ");
                int codigo = scanner.nextInt();
                Cliente cliente = new Cliente(nome, nascimento);
                cliente.setCodigo(codigo);
                cadastro.cadastraPessoa(cliente);
                break;

            default:
                System.out.println("Tipo inválido.");
        }
    }

    private static void removerPessoa(CadastroPessoas cadastro, Scanner scanner) {
        if (cadastro.getQtdAtual() == 0) {
            System.out.println("Nenhuma pessoa cadastrada para remover.");
            return;
        }

        System.out.print("Digite o índice da pessoa que deseja remover (0 a " + (cadastro.getQtdAtual() - 1) + "): ");
        int indice = scanner.nextInt();

        if (indice >= 0 && indice < cadastro.getQtdAtual()) {
            cadastro.removePessoa(indice);
            System.out.println("Pessoa removida com sucesso!");
        } else {
            System.out.println("Índice inválido.");
        }
    }
}
