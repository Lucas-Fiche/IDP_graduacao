package application;

import model.Usuario;
import model.Escolaridade;
import dao.UsuarioDAO;
import dao.EscolaridadeDAO;
import database.DatabaseConnection;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;
import java.util.Scanner;

public class AplicacaoEscolaridade {
    private static Connection conexao;
    private static UsuarioDAO usuarioDAO;
    private static EscolaridadeDAO escolaridadeDAO;
    private static Scanner scanner = new Scanner(System.in);
    private static Usuario usuarioLogado = null;

    public static void main(String[] args) {
        try {
            // Garantir o carregamento do driver JDBC
            Class.forName("org.h2.Driver");

            conexao = DatabaseConnection.getConnection();
            DatabaseConnection.inicializarBancoDeDados(conexao);

            usuarioDAO = new UsuarioDAO(conexao);
            escolaridadeDAO = new EscolaridadeDAO(conexao);

            menuPrincipal();
        } catch (SQLException e) {
            System.err.println("Erro ao iniciar aplicação: " + e.getMessage());
        } catch (ClassNotFoundException e) {
            System.err.println("Driver JDBC não encontrado: " + e.getMessage());
        } finally {
            try {
                if (conexao != null) conexao.close();
            } catch (SQLException e) {
                System.err.println("Erro ao fechar conexão: " + e.getMessage());
            }
        }
    }

    private static void menuPrincipal() throws SQLException {
        int opcao;
        do {
            System.out.println("\n--- SISTEMA DE ESCOLARIDADE ---");
            System.out.println("1. Login");
            System.out.println("2. Sair");
            System.out.print("Escolha uma opção: ");

            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpar buffer

            switch (opcao) {
                case 1:
                    login();
                    break;
                case 2:
                    System.out.println("Encerrando...");
                    break;
                default:
                    System.out.println("Opção inválida!");
            }
        } while (opcao != 2);
    }

    private static void login() throws SQLException {
        System.out.print("Digite sua matrícula: ");
        int matricula = scanner.nextInt();
        scanner.nextLine(); // Limpar buffer

        System.out.print("Digite sua senha: ");
        String senha = scanner.nextLine();

        if (usuarioDAO.autenticar(matricula, senha)) {
            usuarioLogado = usuarioDAO.buscarPorMatricula(matricula);
            menuLogado();
        } else {
            System.out.println("Credenciais inválidas!");
        }
    }

    private static void menuLogado() throws SQLException {
        int opcao;
        do {
            System.out.println("\n--- MENU USUÁRIO ---");
            System.out.println("1. Manutenção de Usuário");
            System.out.println("2. Manutenção de Escolaridade");
            System.out.println("3. Listar Escolaridades");
            System.out.println("4. Logout");
            System.out.print("Escolha uma opção: ");

            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpar buffer

            switch (opcao) {
                case 1:
                    manutencaoUsuario();
                    break;
                case 2:
                    manutencaoEscolaridade();
                    break;
                case 3:
                    listarEscolaridades();
                    break;
                case 4:
                    usuarioLogado = null;
                    return;
                default:
                    System.out.println("Opção inválida!");
            }
        } while (true);
    }

    private static void manutencaoUsuario() throws SQLException {
        System.out.println("\n--- MANUTENÇÃO DE USUÁRIO ---");
        System.out.println("1. Atualizar Usuário");
        System.out.println("2. Excluir Usuário");
        System.out.print("Escolha uma opção: ");

        int opcao = scanner.nextInt();
        scanner.nextLine(); // Limpar buffer

        switch (opcao) {
            case 1:
                atualizarUsuario();
                break;
            case 2:
                excluirUsuario();
                break;
            default:
                System.out.println("Opção inválida!");
        }
    }

    private static void atualizarUsuario() throws SQLException {
        System.out.print("Digite nova senha: ");
        String novaSenha = scanner.nextLine();

        System.out.print("Digite novo sobrenome: ");
        String novoSobrenome = scanner.nextLine();

        System.out.print("Digite novo email: ");
        String novoEmail = scanner.nextLine();

        System.out.print("Digite novo telefone: ");
        String novoTelefone = scanner.nextLine();

        Usuario usuarioAtualizado = new Usuario(
                usuarioLogado.getMatricula(),
                novaSenha,
                novoSobrenome,
                novoEmail,
                novoTelefone
        );

        usuarioDAO.atualizar(usuarioAtualizado);
        System.out.println("Usuário atualizado com sucesso!");
    }

    private static void excluirUsuario() throws SQLException {
        System.out.println("Tem certeza que deseja excluir seu usuário? (S/N)");
        String confirmacao = scanner.nextLine().toUpperCase();

        if (confirmacao.equals("S")) {
            usuarioDAO.excluir(usuarioLogado.getMatricula());
            System.out.println("Usuário excluído com sucesso!");
            usuarioLogado = null;
        }
    }

    private static void manutencaoEscolaridade() throws SQLException {
        System.out.println("\n--- MANUTENÇÃO DE ESCOLARIDADE ---");
        System.out.println("1. Cadastrar Escolaridade");
        System.out.println("2. Atualizar Escolaridade");
        System.out.println("3. Excluir Escolaridade");
        System.out.print("Escolha uma opção: ");

        int opcao = scanner.nextInt();
        scanner.nextLine(); // Limpar buffer

        switch (opcao) {
            case 1:
                cadastrarEscolaridade();
                break;
            case 2:
                atualizarEscolaridade();
                break;
            case 3:
                excluirEscolaridade();
                break;
            default:
                System.out.println("Opção inválida!");
        }
    }

    private static void cadastrarEscolaridade() throws SQLException {
        System.out.print("Digite a instituição: ");
        String instituicao = scanner.nextLine();

        System.out.print("Digite o curso: ");
        String curso = scanner.nextLine();

        System.out.print("Digite a duração em meses: ");
        int duracaoMeses = scanner.nextInt();
        scanner.nextLine(); // Limpar buffer

        Escolaridade novaEscolaridade = new Escolaridade(
                instituicao,
                curso,
                duracaoMeses,
                usuarioLogado.getMatricula()
        );

        escolaridadeDAO.criar(novaEscolaridade);
        System.out.println("Escolaridade cadastrada com sucesso!");
    }

    private static void atualizarEscolaridade() throws SQLException {
        System.out.print("Digite a instituição: ");
        String instituicao = scanner.nextLine();

        System.out.print("Digite o curso: ");
        String curso = scanner.nextLine();

        System.out.print("Digite a duração em meses: ");
        int duracaoMeses = scanner.nextInt();
        scanner.nextLine(); // Limpar buffer

        Escolaridade escolaridadeAtualizada = new Escolaridade(
                instituicao,
                curso,
                duracaoMeses,
                usuarioLogado.getMatricula()
        );

        escolaridadeDAO.atualizar(escolaridadeAtualizada);
        System.out.println("Escolaridade atualizada com sucesso!");
    }

    private static void excluirEscolaridade() throws SQLException {
        System.out.println("Tem certeza que deseja excluir sua escolaridade? (S/N)");
        String confirmacao = scanner.nextLine().toUpperCase();

        if (confirmacao.equals("S")) {
            escolaridadeDAO.excluir(usuarioLogado.getMatricula());
            System.out.println("Escolaridade excluída com sucesso!");
        }
    }

    private static void listarEscolaridades() throws SQLException {
        List<Escolaridade> escolaridades = escolaridadeDAO.buscarPorMatricula(usuarioLogado.getMatricula());

        if (escolaridades.isEmpty()) {
            System.out.println("Nenhuma escolaridade cadastrada.");
        } else {
            System.out.println("\n--- ESCOLARIDADES ---");
            for (Escolaridade escolaridade : escolaridades) {
                System.out.println("Instituição: " + escolaridade.getInstituicao());
                System.out.println("Curso: " + escolaridade.getCurso());
                System.out.println("Duração: " + escolaridade.getDuracaoMeses() + " meses");
                System.out.println();
            }
        }
    }
}