package trabalho_ensalamento_A1;

public class Aluno extends Pessoa{
    
    private Curso curso;

    public Aluno(String nome, Curso curso){
        super(nome);
        this.curso = curso;
    }

    public Curso getCurso() {
        return curso;
    }

    public void setCurso(Curso curso) {
        this.curso = curso;
    }

}
