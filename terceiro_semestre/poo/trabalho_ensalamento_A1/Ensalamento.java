package trabalho_ensalamento_A1;

import java.util.ArrayList;
import java.util.List;

public class Ensalamento {

    public static void realizarEnsalamento() {

        List<Disciplina> disciplinasTI = new ArrayList<>();
        List<Disciplina> disciplinasADM = new ArrayList<>();
        
        Curso ti = new Curso("TI", disciplinasTI);
        Curso adm = new Curso("ADM", disciplinasADM);

        Disciplina poo = new Disciplina("POO", ti);
        Disciplina ed = new Disciplina("Estrutura de Dados", ti);
        Disciplina bi = new Disciplina("BI", adm);

        
        disciplinasTI.add(poo);                 
        disciplinasTI.add(ed);  

        
        disciplinasADM.add(bi);  

        ti.setDisciplinas(disciplinasTI);
        adm.setDisciplinas(disciplinasADM);

        Professor professorMia = new Professor("Mia", poo);
        Professor professorSaulo = new Professor("Saulo", ed);
        Professor professorPaula = new Professor("Paula", bi);

        List<Aluno> alunosTI = new ArrayList<>();
        alunosTI.add(new Aluno("Alfredo", ti));
        alunosTI.add(new Aluno("Amélia", ti));
        alunosTI.add(new Aluno("Bruno", ti));
        alunosTI.add(new Aluno("Capitú", ti));
        alunosTI.add(new Aluno("Debra", ti));
        alunosTI.add(new Aluno("Iracema", ti));
        alunosTI.add(new Aluno("Julieta", ti));
        alunosTI.add(new Aluno("Luciana", ti));
        alunosTI.add(new Aluno("Norberto", ti));
        alunosTI.add(new Aluno("Wendel", ti));
        alunosTI.add(new Aluno("Zoey", ti));

        List<Aluno> alunosADM = new ArrayList<>();
        alunosADM.add(new Aluno("Ana", adm));
        alunosADM.add(new Aluno("Bentinho", adm));
        alunosADM.add(new Aluno("Ian", adm));
        alunosADM.add(new Aluno("Joelmir", adm));
        alunosADM.add(new Aluno("Luana", adm));
        alunosADM.add(new Aluno("Majô", adm));
        alunosADM.add(new Aluno("Maria", adm));
        alunosADM.add(new Aluno("Paulo", adm));
        alunosADM.add(new Aluno("Romeu", adm));

        Turma turmaPOO = new Turma(professorMia, poo, alunosTI);
        Turma turmaED = new Turma(professorSaulo, ed, alunosTI);
        Turma turmaBI = new Turma(professorPaula, bi, alunosADM);

        turmaPOO.exibirTurma();
        turmaED.exibirTurma();
        turmaBI.exibirTurma();
    }
}
