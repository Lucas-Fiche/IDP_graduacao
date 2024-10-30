package trabalho_ensalamento_A1;

import java.util.List;

public class Turma {
    private Professor professor;
    private Disciplina disciplina;
    private List<Aluno> alunos;

    public Turma(Professor professor, Disciplina disciplina, List<Aluno> alunos){
        this.professor = professor;
        this.disciplina = disciplina;
        this.alunos = alunos;
    }

    public void exibirTurma(){
        System.out.println("===========================================");
        System.out.println("Turma de " + disciplina.getNomeDisciplina());
        System.out.println("===========================================");
        System.out.println("Professor: " + professor.getNome());
        System.out.println("===========================================");
        System.out.println("Alunos: " );
        System.out.println();
        for (int i = 0; i < alunos.size(); i++) {
            Aluno posicaoAluno = alunos.get(i); 
            System.out.println((i + 1) + ": " + posicaoAluno.getNome() + " Curso: " + posicaoAluno.getCurso().getNomeCurso());
        }
    }
}
