public class Carro extends Veiculo {
    private String modelo; 
    public Carro(double peso) {
        super(peso, "Carro");
    }

    public void defineModelo(String modelo) {
        this.modelo = modelo;
    }

    @Override
    public double calcularPreco() {
        if (peso <= 2000) {
            if (modelo.equalsIgnoreCase("hatchback")) return 13.00;
            else if (modelo.equalsIgnoreCase("sedan")) return 15.00;
        } else {
            return new Furgao(peso).calcularPreco();
        }
        return 0.0; 
    }
}