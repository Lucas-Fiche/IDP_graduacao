package provaA1.q3;

public class CarroBuilder {

    public static Carro[] construirCarros(String marca, String modelo, int anoInicial, int anoFinal) {
        int tamanhoArray = anoFinal - anoInicial + 1;
        Carro[] carros = new Carro[tamanhoArray];

        for (int i = 0; i < tamanhoArray; i++) {
            int anoModelo = anoInicial + i;
            carros[i] = new Carro(anoModelo, new Modelo(marca, modelo), "Placa" + (i + 1));
        }

        return carros;
    }
}