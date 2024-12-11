package model;

public class Escolaridade {
    private String instituicao;
    private String curso;
    private int duracaoMeses;
    private int usuarioMatricula;

    public Escolaridade(String instituicao, String curso,
                        int duracaoMeses, int usuarioMatricula) {
        this.instituicao = instituicao;
        this.curso = curso;
        this.duracaoMeses = duracaoMeses;
        this.usuarioMatricula = usuarioMatricula;
    }

    // Getters e Setters (gere usando Alt+Insert)
    public String getInstituicao() { return instituicao; }
    public void setInstituicao(String instituicao) { this.instituicao = instituicao; }

    public String getCurso() { return curso; }
    public void setCurso(String curso) { this.curso = curso; }

    public int getDuracaoMeses() { return duracaoMeses; }
    public void setDuracaoMeses(int duracaoMeses) { this.duracaoMeses = duracaoMeses; }

    public int getUsuarioMatricula() { return usuarioMatricula; }
    public void setUsuarioMatricula(int usuarioMatricula) { this.usuarioMatricula = usuarioMatricula; }
}
