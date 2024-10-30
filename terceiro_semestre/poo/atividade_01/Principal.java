package atividade_01;

import java.util.Scanner;

public class Principal {
    public static void main(String[] args){
    
    Scanner leitura = new Scanner(System.in);
    Ipi ipi = new Ipi();
    Icms icms = new Icms();
    Iss iss = new Iss();

    System.out.println("""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            Qual é a sua operação comercial?

            1 - Produto
            2 - Serviço
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            """);

    int menu = leitura.nextInt();

    if (menu == 1) {
        System.out.println("Qual o valor do seu Produto?");
        double valorProduto = leitura.nextDouble();

        double impostoIpi = ipi.aplicarIpi(valorProduto);
        double impostoIcms = icms.aplicarIcms(valorProduto);

        System.out.println(String.format("""
            =-=-=-=-=-=-=-=-=-=-=-=-=
                Impostos Aplicados:
                IPI: R$%.2f
                ICMS: R$%.2f
            =-=-=-=-=-=-=-=-=-=-=-=-=    
                """,impostoIpi, impostoIcms));

        double valorFinal = valorProduto + impostoIpi + impostoIcms;
        System.out.println(String.format("Valor Final: R$%.2f", valorFinal));
    } else if (menu == 2) {
        System.out.println("Qual o valor do seu Serviço?");
        double valorServico = leitura.nextDouble();

        double impostoIcms = icms.aplicarIcms(valorServico);
        double impostoIss = iss.aplicarIss(valorServico);

        System.out.println(String.format("""
            =-=-=-=-=-=-=-=-=-=-=-=-=
                Impostos Aplicados:
                ISS: R$%.2f
                ICMS: R$%.2f
            =-=-=-=-=-=-=-=-=-=-=-=-=
                """,impostoIss, impostoIcms));

        double valorFinal = valorServico + impostoIss + impostoIcms;
        System.out.println(String.format("Valor Final: R$%.2f", valorFinal));
    } else {
        System.out.println("Opção Inválida!");
    }

    leitura.close();

    }
}
