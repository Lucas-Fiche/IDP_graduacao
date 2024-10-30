public class Controller {
    private Model model;
    private View view;

    public Controller(Model model, View view) {
        this.model = model;
        this.view = view;
    }

    public void setNomePessoa(String nome) {
        model.setNome(nome);
    }

    public void setIdadePessoa(int idade) {
        model.setIdade(idade);
    }

    public void atualizarVisao() {
        view.exibirPessoa(model.getNome(), model.getIdade());
    }
}
