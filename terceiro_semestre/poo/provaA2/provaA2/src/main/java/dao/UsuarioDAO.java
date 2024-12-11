package dao;

import model.Usuario;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class UsuarioDAO {
    private Connection conexao;

    public UsuarioDAO(Connection conexao) {
        this.conexao = conexao;
    }

    public void criar(Usuario usuario) throws SQLException {
        String sql = "INSERT INTO usuarios (matricula, senha, sobrenome, email, telefone) VALUES (?, ?, ?, ?, ?)";

        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setInt(1, usuario.getMatricula());
            stmt.setString(2, usuario.getSenha());
            stmt.setString(3, usuario.getSobrenome());
            stmt.setString(4, usuario.getEmail());
            stmt.setString(5, usuario.getTelefone());
            stmt.executeUpdate();
        }
    }

    public boolean autenticar(int matricula, String senha) throws SQLException {
        String sql = "SELECT COUNT(*) FROM usuarios WHERE matricula = ? AND senha = ?";

        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setInt(1, matricula);
            stmt.setString(2, senha);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return rs.getInt(1) > 0;
                }
            }
        }
        return false;
    }

    public Usuario buscarPorMatricula(int matricula) throws SQLException {
        String sql = "SELECT * FROM usuarios WHERE matricula = ?";

        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setInt(1, matricula);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return new Usuario(
                            rs.getInt("matricula"),
                            rs.getString("senha"),
                            rs.getString("sobrenome"),
                            rs.getString("email"),
                            rs.getString("telefone")
                    );
                }
            }
        }
        return null;
    }

    public void atualizar(Usuario usuario) throws SQLException {
        String sql = "UPDATE usuarios SET senha=?, sobrenome=?, email=?, telefone=? WHERE matricula=?";

        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setString(1, usuario.getSenha());
            stmt.setString(2, usuario.getSobrenome());
            stmt.setString(3, usuario.getEmail());
            stmt.setString(4, usuario.getTelefone());
            stmt.setInt(5, usuario.getMatricula());
            stmt.executeUpdate();
        }
    }

    public void excluir(int matricula) throws SQLException {
        String sql = "DELETE FROM usuarios WHERE matricula = ?";

        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setInt(1, matricula);
            stmt.executeUpdate();
        }
    }

    public List<Usuario> listarTodos() throws SQLException {
        List<Usuario> usuarios = new ArrayList<>();
        String sql = "SELECT * FROM usuarios";

        try (Statement stmt = conexao.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                usuarios.add(new Usuario(
                        rs.getInt("matricula"),
                        rs.getString("senha"),
                        rs.getString("sobrenome"),
                        rs.getString("email"),
                        rs.getString("telefone")
                ));
            }
        }
        return usuarios;
    }
}
