package atividade_05;

public class ClienteVip extends Cliente {
    private double percentualDesconto;

    public ClienteVip(String nome, Data nascimento, double percentualDesconto) {
        super(nome, nascimento);
        this.percentualDesconto = percentualDesconto;
    }

    public double getPercentualDesconto() {
        return percentualDesconto;
    }

    public void setPercentualDesconto(double percentualDesconto) {
        this.percentualDesconto = percentualDesconto;
    }

    @Override
    public void imprimeDados() {
        super.imprimeDados();
        System.out.println("Percentual de desconto: " + percentualDesconto + "%");
    }
}

