public abstract class Veiculo {

    public double peso;
    public String tipo;

    public Veiculo (double peso, String tipo) {
        this.peso = peso;
        this.tipo = tipo;
    }
    
    public abstract double calcularPreco();
}
