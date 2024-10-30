public class Caminhonete extends Veiculo{
    public Caminhonete(double peso){
        super(peso, "Caminhonete");
    }

    @Override
    public double calcularPreco(){
        if (peso <= 3000) {
            return 25.00;
        } else if (peso > 3100 && peso <= 6000){
            return 50.00;
        } else {
            System.out.println("Peso da Caminhonete excede o limite.");
            return 0.0;
        }
    }  
}
