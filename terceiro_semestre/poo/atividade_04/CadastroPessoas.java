package atividade_04;

public class CadastroPessoas {
    private int qtdAtual;
    private Pessoa[] pessoas;

    public CadastroPessoas(int tamanho) {
        pessoas = new Pessoa[tamanho];
        qtdAtual = 0;
    }

    public int getCapacidade() {
        return pessoas.length; 
    }

    public int getQtdAtual() {
        return qtdAtual;
    }

    public void setQtdAtual(int qtdAtual) {
        this.qtdAtual = qtdAtual;
    }

    public void cadastraPessoa(Pessoa pess) {
        if (qtdAtual < pessoas.length) {
            pessoas[qtdAtual] = pess;
            qtdAtual++;
        } else {
            System.out.println("Cadastro de pessoas lotado!");
        }
    }

    public void imprimeCadastro() {
        for (int i = 0; i < qtdAtual; i++) {
            pessoas[i].imprimeDados();
        }
    }

    public void removePessoa(int indice) {
        if (indice >= 0 && indice < qtdAtual) {
            for (int i = indice; i < qtdAtual - 1; i++) {
                pessoas[i] = pessoas[i + 1];
            }
            pessoas[qtdAtual - 1] = null;
            qtdAtual--;
        } else {
            System.out.println("Índice inválido.");
        }
    }
}
