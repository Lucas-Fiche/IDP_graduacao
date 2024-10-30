package trabalho_ensalamento_A1;

public class Professor extends Pessoa{

    private Disciplina disciplina;

    public Professor(String nome, Disciplina disciplina){
        super(nome);
        this.disciplina = disciplina;
    }

    public Disciplina getDisciplina() {
        return disciplina;
    }

    public void setDisciplina(Disciplina disciplina) {
        this.disciplina = disciplina;
    }
}
