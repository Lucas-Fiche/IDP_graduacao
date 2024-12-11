package dao;

import model.Escolaridade;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class EscolaridadeDAO {
    private Connection conexao;

    public EscolaridadeDAO(Connection conexao) {
        this.conexao = conexao;
    }

    public void criar(Escolaridade escolaridade) throws SQLException {
        String sql = "INSERT INTO escolaridades (instituicao, curso, duracao_meses, usuario_matricula) VALUES (?, ?, ?, ?)";

        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setString(1, escolaridade.getInstituicao());
            stmt.setString(2, escolaridade.getCurso());
            stmt.setInt(3, escolaridade.getDuracaoMeses());
            stmt.setInt(4, escolaridade.getUsuarioMatricula());
            stmt.executeUpdate();
        }
    }

    public List<Escolaridade> buscarPorMatricula(int usuarioMatricula) throws SQLException {
        List<Escolaridade> escolaridades = new ArrayList<>();
        String sql = "SELECT * FROM escolaridades WHERE usuario_matricula = ?";

        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setInt(1, usuarioMatricula);

            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    escolaridades.add(new Escolaridade(
                            rs.getString("instituicao"),
                            rs.getString("curso"),
                            rs.getInt("duracao_meses"),
                            rs.getInt("usuario_matricula")
                    ));
                }
            }
        }
        return escolaridades;
    }

    public void atualizar(Escolaridade escolaridade) throws SQLException {
        String sql = "UPDATE escolaridades SET instituicao=?, curso=?, duracao_meses=? WHERE usuario_matricula=?";

        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setString(1, escolaridade.getInstituicao());
            stmt.setString(2, escolaridade.getCurso());
            stmt.setInt(3, escolaridade.getDuracaoMeses());
            stmt.setInt(4, escolaridade.getUsuarioMatricula());
            stmt.executeUpdate();
        }
    }

    public void excluir(int usuarioMatricula) throws SQLException {
        String sql = "DELETE FROM escolaridades WHERE usuario_matricula = ?";

        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setInt(1, usuarioMatricula);
            stmt.executeUpdate();
        }
    }
}
