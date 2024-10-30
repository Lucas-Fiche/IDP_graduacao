package atividade_04;

public class Gerente extends Funcionario{
    
    private String area;

    public Gerente(String nome, Data nascimento, float salario, String area) {
        super(nome, nascimento, salario);
        this.area = area;
    }

    
    @Override
    public float calculaImposto(float salario){
        return salario * 5/100;
    }

    @Override
    public void imprimeDados(){
        System.out.println("Nome: " + this.getNome());
        System.out.print("Nascimento: ");
        getNascimento().imprimeData();
        System.out.println("Salário: " + this.getSalario());
        System.out.println("Área: " + this.getArea());
    }

    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }

}
