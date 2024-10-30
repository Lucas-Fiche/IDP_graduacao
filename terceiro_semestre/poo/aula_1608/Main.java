package aula_1608;

public class Main {
    public static void main(String[] args){
        Carro carro1 = new Carro();
        carro1.proprietario = "Marcelo";
        carro1.placa = "GHJ6591";
        carro1.modelo = "Jeep Renegade";
        carro1.cor = "Vermelho";
        carro1.horario_de_entrada = 10;
        carro1.horario_de_saida = 11;
        carro1.vagaEstacionada = 250;

        carro1.fichaTecnica();
    }
}
