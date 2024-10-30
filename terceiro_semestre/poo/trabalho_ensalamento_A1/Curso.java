package trabalho_ensalamento_A1;

import java.util.List;

public class Curso {
    
    private String nomeCurso;
    private List<Disciplina> disciplinas;

    public Curso(String nomeCurso, List<Disciplina> disciplinas){
        this.nomeCurso = nomeCurso;
        this.disciplinas = disciplinas;
    }

    public String getNomeCurso() {
        return nomeCurso;
    }

    public void setNomeCurso(String nomeCurso) {
        this.nomeCurso = nomeCurso;
    }

    public List<Disciplina> getDisciplinas() {
        return disciplinas;
    }

    public void setDisciplinas(List<Disciplina> disciplinas) {
        this.disciplinas = disciplinas;
    }

}
