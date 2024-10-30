package aula_0609;

public abstract class Animal {

    public String nome;

    // public void falar(){
    //     System.out.println(this.nome + ": falar");
    // }

    public abstract void falar();

    public void andar(){
        System.out.println(this.nome + ": andar");
    }
}
