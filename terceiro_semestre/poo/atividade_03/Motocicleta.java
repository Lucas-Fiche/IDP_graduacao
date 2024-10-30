public class Motocicleta extends Veiculo{
    public Motocicleta(double peso){
        super(peso, "Motocicleta");
    }

    @Override
    public double calcularPreco(){
        if (peso <= 100) {
            return 2.00;
        } else if (peso > 100 && peso < 300) {
            return 4.00;
        } else {
            return 10.00;
        }
    }
}
