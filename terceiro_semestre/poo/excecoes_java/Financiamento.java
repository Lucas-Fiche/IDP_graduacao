package excecoes_java;

public class Financiamento {
    public double valorTotal;
    public double entrada;
    public int parcelas;

    public Financiamento(double valorTotal, double entrada, int parcelas){

        if (entrada < valorTotal * 0.2){
            throw new RuntimeException("A entrada deve ser pelo menos 20% do valor total");
        } else if (parcelas < 6) {
            throw new RuntimeException("O número mínimo de parcelas deve ser 6");
        }

        this.valorTotal = valorTotal;
        this.entrada = entrada;
        this.parcelas = parcelas;
    }

    public double prestacao(){
        return(valorTotal - entrada)/parcelas;
    }
}
