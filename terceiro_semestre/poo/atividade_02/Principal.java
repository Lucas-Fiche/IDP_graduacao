package atividade_02;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        bombaCombustivel bomba1 = new bombaCombustivel("Diesel", 6.5, 150);
        try (Scanner leitura = new Scanner(System.in)) {
            System.out.println("""
            =====================================
            Menu

            1 - Abastecer em Reais
            2 - Abastecer por Litro
            3 - Alterar valor do Litro
            4 - Alterar tipo de Combustível
            5 - Alterar quantidade de Combustível na Bomba
            6 - Sair
            =====================================
                """);
            
            int menu = 0;
            while (menu != 6){
                menu = leitura.nextInt();
                if (menu == 1){
                    System.out.println("Quantos reais deseja abastecer?");
                    double valorReais = leitura.nextDouble();
                    bomba1.abastecerPorValor(valorReais);
                } else if (menu == 2) {
                    System.out.println("Quantos litros deseja abastecer?");
                    double litros = leitura.nextDouble();
                    bomba1.abastecerPorLitro(litros);
                } else if (menu == 3) {
                    System.out.println("Digite o novo valor do Litro:");
                    double novoValor = leitura.nextDouble();
                    bomba1.alteraValor(novoValor);
                } else if (menu == 4) {
                    System.out.println("Digite o novo tipo de gasolina:");
                    String novoTipo = leitura.next();
                    bomba1.alterarCombustivel(novoTipo);
                } else if (menu == 5) {
                    System.out.println("Digite a nova quantidade de gasolina na bomba:");
                    double novaQuantidade = leitura.nextDouble();
                    bomba1.alterarQuantidadeCombustivel(novaQuantidade);
                } else if (menu == 6) {
                    System.out.println("Volte Sempre!");
                    break;
                } else {
                    System.out.println("Opção Inexistente!");
                }
                System.out.println("""
                =====================================
                Deseja realizar outra operação?
                1 - Abastecer em Reais
                2 - Abastecer por Litro
                3 - Alterar valor do Litro
                4 - Alterar tipo de Combustível
                5 - Alterar quantidade de Combustível na Bomba
                6 - Sair
                =====================================
                """);
            }
        }

    }
}

