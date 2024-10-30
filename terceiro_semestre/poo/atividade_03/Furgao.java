public class Furgao extends Veiculo{
    public Furgao(double peso){
        super(peso, "Furgao");
    }

    @Override
    public double calcularPreco(){
        if (peso <= 3000) {
            return 25.00;
        } else if (peso > 3000 && peso <= 6000) {
            return 50.00;
        } else {
            // throw new IllegalArgumentException("Peso do furgão excede o limite.");
            System.out.println("Peso excede o Limite");
            return 0.0;
        }
    }
}
