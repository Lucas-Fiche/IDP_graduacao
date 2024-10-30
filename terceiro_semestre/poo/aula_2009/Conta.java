package aula_2009;

import java.io.IOException;

public class Conta {
    private double saldo;
    private int numero;

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public double deposito(double valor) {
        if (valor > 0) {
            saldo += valor;
        }
        return saldo;
    }

    public double transferencia(double valor, Conta destino) {
        if (valor > 0 && saldo >= valor) {
            saldo -= valor;
            destino.deposito(valor);
        } 
        return saldo;
    }

    public double consultarSaldo() {
        return saldo;
    }

    public double saque(double valor) {
        if (valor > saldo) {
            throw new RuntimeException("O valor informado:  " + valor + " é maior que o saldo disponível: " + saldo);
        } 
        
        if (valor < 0) {
            throw new ClassCastException("Apenas valores positivos são permitidos e você informou " + valor);
        }

        if (valor <= saldo) {
            saldo -= valor;
        } 

        return saldo;
    }
    
    // Exemplo usando a exceção Throws ao invés de Try Catch
    public void imprimir() throws IOException {
        throw new IOException("Saldo insuficiente");
    }
}

