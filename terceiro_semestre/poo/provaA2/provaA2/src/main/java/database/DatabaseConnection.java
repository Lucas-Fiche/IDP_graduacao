package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class DatabaseConnection {
    private static final String URL = "jdbc:h2:mem:escolaridade;DB_CLOSE_DELAY=-1";
    private static final String USER = "sa";
    private static final String PASSWORD = "";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    public static void inicializarBancoDeDados(Connection conexao) throws SQLException {
        try (Statement stmt = conexao.createStatement()) {
            // Criação tabela usuários
            stmt.execute("CREATE TABLE usuarios (" +
                    "matricula INTEGER PRIMARY KEY, " +
                    "senha VARCHAR(255), " +
                    "sobrenome VARCHAR(255), " +
                    "email VARCHAR(255), " +
                    "telefone VARCHAR(20)" +
                    ")");

            // Criação tabela escolaridades
            stmt.execute("CREATE TABLE escolaridades (" +
                    "id INTEGER AUTO_INCREMENT PRIMARY KEY, " +
                    "instituicao VARCHAR(255), " +
                    "curso VARCHAR(255), " +
                    "duracao_meses INTEGER, " +
                    "usuario_matricula INTEGER, " +
                    "FOREIGN KEY (usuario_matricula) REFERENCES usuarios(matricula)" +
                    ")");
        }
    }
}
