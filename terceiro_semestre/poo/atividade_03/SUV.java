public class SUV extends Veiculo{
    public SUV(double peso){
        super(peso, "SUV");
    }

    @Override
    public double calcularPreco(){
        if (peso <= 2000) return 20.00;
        else return new Furgao(peso).calcularPreco();
    }
}
