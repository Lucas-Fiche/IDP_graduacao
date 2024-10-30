package aula_1608;

public class Carro {
    public String proprietario;
    public String placa;
    public String modelo;
    public String cor;
    public int horario_de_entrada;
    public int horario_de_saida;
    public int vagaEstacionada;

    public void fichaTecnica(){
        System.out.println("Nome do Condutor: " + proprietario);
        System.out.println("Placa do Carro: " + placa);
        System.out.println("Modelo do Carro: " + modelo);
        System.out.println("Cor do Carro: " + cor);
        System.out.println("Hora de Entrada: " + horario_de_entrada);
        System.out.println("Hora de Saída: " + horario_de_saida);
        System.out.println("Vaga Estacionada: " + vagaEstacionada);
    }
}
