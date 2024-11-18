import org.example.Estoque;
import org.example.Produto;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Set;

public class EstoqueTeste {

    @Test
    public void testAdicionarProduto() {
        Estoque estoque = new Estoque();
        Produto produto = new Produto("Notebook", 2500.00);

        assertTrue(estoque.adicionarProduto(produto), "Produto deve ser adicionado com sucesso.");
        assertFalse(estoque.adicionarProduto(produto), "Produto duplicado não deve ser adicionado.");
    }

    @Test
    public void testRemoverProduto() {
        Estoque estoque = new Estoque();
        Produto produto = new Produto("Notebook", 2500.00);

        estoque.adicionarProduto(produto);
        assertTrue(estoque.removerProduto("Notebook"), "Produto existente deve ser removido.");
        assertFalse(estoque.removerProduto("Smartphone"), "Produto inexistente não deve ser removido.");
    }

    @Test
    public void testBuscarProduto() {
        Estoque estoque = new Estoque();
        Produto produto = new Produto("Notebook", 2500.00);

        estoque.adicionarProduto(produto);
        assertEquals(produto, estoque.buscarProduto("Notebook"), "Produto existente deve ser retornado.");
        assertNull(estoque.buscarProduto("Smartphone"), "Busca por produto inexistente deve retornar null.");
    }

    @Test
    public void testListarProdutos() {
        Estoque estoque = new Estoque();
        Produto p1 = new Produto("Notebook", 2500.00);
        Produto p2 = new Produto("Smartphone", 1500.00);

        estoque.adicionarProduto(p1);
        estoque.adicionarProduto(p2);

        Set<Produto> produtos = estoque.listarProdutos();
        assertTrue(produtos.contains(p1), "Produto 1 deve estar na lista.");
        assertTrue(produtos.contains(p2), "Produto 2 deve estar na lista.");
        assertEquals(2, produtos.size(), "Lista deve conter exatamente dois produtos.");
    }
}
