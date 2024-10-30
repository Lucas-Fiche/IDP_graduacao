package aula_2009;

public class Main {
    public static void main(String[] args) {
        // Criando duas contas
        Conta conta1 = new Conta();
        Conta conta2 = new Conta();

        try {
            // Definindo o número das contas
            conta1.setNumero(123);
            conta2.setNumero(456);

            // Exibindo os números das contas
            System.out.println("Conta 1 - Número: " + conta1.getNumero());
            System.out.println("Conta 2 - Número: " + conta2.getNumero());

            // Depósitos
            conta1.deposito(1000);
            conta2.deposito(500);

            // Exibindo os saldos após depósito
            System.out.println("Saldo da Conta 1 após depósito: " + conta1.consultarSaldo());
            System.out.println("Saldo da Conta 2 após depósito: " + conta2.consultarSaldo());

            // Transferência da Conta 1 para a Conta 2
            conta1.transferencia(300, conta2);

            // Exibindo os saldos após a transferência
            System.out.println("Saldo da Conta 1 após transferência: " + conta1.consultarSaldo());
            System.out.println("Saldo da Conta 2 após receber transferência: " + conta2.consultarSaldo());

            // Saque na Conta 2
            conta2.saque(-100);

            // Exibindo o saldo da Conta 2 após saque
            System.out.println("Saldo da Conta 2 após saque: " + conta2.consultarSaldo());
        } catch (ClassCastException classCastException) {
            System.out.println("Apenas valores positivos são permitidos.");
        } catch (RuntimeException runtimeException) {
            System.out.println("O valor informado é maior que o saldo disponível");
        } 
        
    }
}

