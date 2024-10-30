public class Main {
    public static void main(String[] args) {

        Model pessoa = new Model("João", 25);
        
        View view = new View();
        
        Controller controller = new Controller(pessoa, view);
        
        controller.atualizarVisao();
        
        controller.setNomePessoa("Maria");
        controller.setIdadePessoa(30);
        
        controller.atualizarVisao();
    }
}
