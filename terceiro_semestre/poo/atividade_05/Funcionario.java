package atividade_05;

public class Funcionario extends Pessoa{

    private float salario;

    public Funcionario(String nome, Data nascimento, float salario) {
        super(nome, nascimento);
        this.salario = salario;
    }

    public float calculaImposto(float salario){
        return salario*3/100;
    }

    @Override
    public void imprimeDados(){
        System.out.println("Nome: " + this.getNome());
        System.out.print("Nascimento: ");
        getNascimento().imprimeData();
        System.out.println("Salário: " + this.getSalario());
    }

    public float getSalario() {
        salario -= calculaImposto(salario);
        return salario;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }
}
