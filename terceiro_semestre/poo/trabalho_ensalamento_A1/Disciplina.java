package trabalho_ensalamento_A1;

public class Disciplina {
    
    private String nomeDisciplina;
    private Curso curso;

    public Disciplina(String nomeDisciplina, Curso curso){
        this.nomeDisciplina = nomeDisciplina;
        this.curso = curso;
    }

    public String getNomeDisciplina() {
        return nomeDisciplina;
    }

    public void setNomeDisciplina(String nomeDisciplina) {
        this.nomeDisciplina = nomeDisciplina;
    }

    public Curso getCurso() {
        return curso;
    }

    public void setCurso(Curso curso) {
        this.curso = curso;
    }

}
