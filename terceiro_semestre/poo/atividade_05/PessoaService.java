package atividade_05;

import java.util.ArrayList;
import java.util.List;

public class PessoaService {
    private List<Pessoa> pessoas;
    private int qtdGerente;
    private int qtdFuncionarios;

    public PessoaService(int capacidade) {
        this.pessoas = new ArrayList<>(capacidade);
        this.qtdGerente = 0;
        this.qtdFuncionarios = 0;
    }

    public void cadastrarPessoa(Pessoa pessoa) throws QuantidadeExcedidaException {
        if (pessoa instanceof Gerente) {
            if (qtdGerente >= 1) {
                throw new QuantidadeExcedidaException("A empresa já possui o número máximo de 1 gerente.");
            }
            qtdGerente++;
        } else if (pessoa instanceof Funcionario) {
            if (qtdFuncionarios >= 7) {
                throw new QuantidadeExcedidaException("A empresa já possui o número máximo de 7 funcionários.");
            }
            qtdFuncionarios++;
        }

        pessoas.add(pessoa);
        System.out.println("Pessoa cadastrada com sucesso: " + pessoa.getNome());
    }

    public void imprimirCadastro() {
        if (pessoas.isEmpty()) {
            System.out.println("Nenhuma pessoa cadastrada.");
        } else {
            for (Pessoa pessoa : pessoas) {
                pessoa.imprimeDados();
            }
        }
    }

    public void removerPessoa(int indice) {
        if (indice >= 0 && indice < pessoas.size()) {
            Pessoa pessoaRemovida = pessoas.remove(indice);
            if (pessoaRemovida instanceof Gerente) {
                qtdGerente--;
            } else if (pessoaRemovida instanceof Funcionario) {
                qtdFuncionarios--;
            }
            System.out.println("Pessoa removida com sucesso.");
        } else {
            System.out.println("Índice inválido.");
        }
    }
}

