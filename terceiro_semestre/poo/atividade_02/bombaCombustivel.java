package atividade_02;

public class bombaCombustivel {
    private String tipoCombustivel;
    private double valorLitro;
    private double quantidadeCombustivel;

    public bombaCombustivel (String tipoCombustivel, double valorLitro, double quantidadeCombustivel){
        this.tipoCombustivel = tipoCombustivel;
        this.valorLitro = valorLitro;
        this.quantidadeCombustivel = quantidadeCombustivel;
    }

    public void abastecerPorValor(double valorDinheiro){
        double litros = valorDinheiro / valorLitro;

        if (litros > quantidadeCombustivel){
            System.out.println("Sem combustível suficiente para abastecer!");
        } else {
            System.out.println("Abastecendo!");
            quantidadeCombustivel -= litros;
            System.out.println("Litros abastecidos: %.2f Litros".formatted(litros));
            System.out.println("Quantidade Restante de Combustível na Bomba: %.2f Litros".formatted(quantidadeCombustivel));
        }
    }

    public void abastecerPorLitro(double qtd_litros){
        double preco = qtd_litros * valorLitro;
        
        if (qtd_litros > quantidadeCombustivel){
            System.out.println("Sem combustível suficiente para abastecer!");
        } else {
            System.out.println("Abastecendo!");
            quantidadeCombustivel -= qtd_litros;
            System.out.println("Valor: R$%.2f".formatted(preco));
            System.out.println("Quantidade Restante de Combustível na Bomba: %.2f Litros".formatted(quantidadeCombustivel));
        }
    }

    public void alteraValor(double novoValorLitro){
        
        if (novoValorLitro < 1){
            System.out.println("O valor deve ser positivo!");
        } else {
            valorLitro = novoValorLitro;
            System.out.println("Novo valor: R$%.2f".formatted(valorLitro));
        }
    }

    public void alterarCombustivel(String novoTipoCombustivel){
        tipoCombustivel = novoTipoCombustivel;
        System.out.println("Alterado para %s".formatted(tipoCombustivel));
    }

    public void alterarQuantidadeCombustivel(double novaQuantidadeCombustivel){
        quantidadeCombustivel = novaQuantidadeCombustivel;
        System.out.println("Quantidade de Combustível na Bomba: %.2f".formatted(quantidadeCombustivel));
    }
}
