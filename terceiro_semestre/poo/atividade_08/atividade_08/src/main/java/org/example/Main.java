package org.example;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        ProdutoDAO produtoDAO = new ProdutoDAO();

        // Inserir produtos
        produtoDAO.inserirProduto(new Produto("Informática", "Notebook Dell", 2.5, 10, "kg"));
        produtoDAO.inserirProduto(new Produto("Limpeza", "Desinfetante", 1.0, 50, "litro"));
        produtoDAO.inserirProduto(new Produto("Casa & Decoração", "Luminária", 3.0, 5, "kg"));
        produtoDAO.inserirProduto(new Produto("Alimentos", "Pote de Mel", 0.5, 20, "kg"));
        produtoDAO.inserirProduto(new Produto("Papelaria", "Caderno", 0.7, 30, "kg"));

        // Alterar produtos
        Produto produto1 = produtoDAO.buscarProdutoPorId(1);
        if (produto1 != null) {
            produto1.setQuantidade(15);
            produtoDAO.alterarProduto(produto1);
        }

        Produto produto2 = produtoDAO.buscarProdutoPorId(2);
        if (produto2 != null) {
            produto2.setDescricao("Desinfetante Lavanda");
            produtoDAO.alterarProduto(produto2);
        }

        // Excluir um produto
        produtoDAO.excluirProduto(5);

        // Listar todos os produtos
        List<Produto> produtos = produtoDAO.listarProdutos();
        produtos.forEach(System.out::println);

        // Exibir detalhes de produtos
        Produto detalhes1 = produtoDAO.buscarProdutoPorId(1);
        Produto detalhes2 = produtoDAO.buscarProdutoPorId(2);

        System.out.println("\nDetalhes do Produto 1:");
        System.out.println(detalhes1);

        System.out.println("\nDetalhes do Produto 2:");
        System.out.println(detalhes2);
    }
}
