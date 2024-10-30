import java.util.Scanner;
public class Principal {
    public static void main(String[] args) {
        try (Scanner leitura = new Scanner(System.in)) {
            while (true) {
                System.out.println("Deseja adicionar um novo veículo? (Sim/Não)");
                String resposta = leitura.nextLine().trim().toLowerCase();
                
                if (resposta.equals("sim")){
                    System.out.println("""
                    Informe o tipo do Veículo (1 a 5):
                    1 - Motocicleta
                    2 - Carro
                    3 - Caminhonete
                    4 - Furgão
                    5 - SUV
                    """);
                
                int tipo = leitura.nextInt();
                
                System.out.println("Informe o peso do Veículo: ");
                double peso = leitura.nextDouble();
                leitura.nextLine();
                
                Veiculo veiculo = null;
                
                switch (tipo) {
                    
                    case 1:
                        veiculo = new Motocicleta(peso);
                        break;
                        
                    case 2:
                        System.out.println("Qual o modelo? (Hatchback | Sedan):");
                        String modelo = leitura.nextLine().trim();
                        veiculo = new Carro(peso);
                        ((Carro) veiculo).defineModelo(modelo); 
                        break;

                    case 3:
                        veiculo = new Caminhonete(peso);
                        break;
                        
                    case 4:
                        veiculo = new Furgao(peso);
                        break;
                        
                    case 5:
                        veiculo = new SUV(peso);
                        break;
                        
                    default:
                        System.out.println("Tipo de Veículo Desconhecido!");
                }
                
                if (veiculo != null) {
                    double preco = veiculo.calcularPreco();
                    System.out.println("O valor para o veículo selecionado é R$%.2f.".formatted(preco));
                }
                } else if (resposta.equals("não")){
                break;
                } else {
                System.out.println("Opção Inválida!");
                }
            }
        }
    }
}
