import org.example.Produto;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ProdutoTeste {

    @Test
    public void testEquals() {
        Produto p1 = new Produto("Notebook", 2500.00);
        Produto p2 = new Produto("Notebook", 3000.00);
        Produto p3 = new Produto("Smartphone", 1500.00);

        assertEquals(p1, p2, "Produtos com o mesmo nome devem ser iguais.");
        assertNotEquals(p1, p3, "Produtos com nomes diferentes devem ser diferentes.");
    }

    @Test
    public void testHashCode() {
        Produto p1 = new Produto("Notebook", 2500.00);
        Produto p2 = new Produto("Notebook", 3000.00);

        assertEquals(p1.hashCode(), p2.hashCode(), "Produtos iguais devem ter o mesmo hashCode.");
    }

    @Test
    public void testCompareTo() {
        Produto p1 = new Produto("Notebook", 2500.00);
        Produto p2 = new Produto("Smartphone", 1500.00);
        Produto p3 = new Produto("Tablet", 2500.00);

        assertTrue(p1.compareTo(p2) > 0, "Produto mais caro deve retornar valor positivo.");
        assertTrue(p2.compareTo(p1) < 0, "Produto mais barato deve retornar valor negativo.");
        assertEquals(0, p1.compareTo(p3), "Produtos com mesmo preço devem retornar 0.");
    }

    @Test
    public void testGetNome() {
        Produto produto = new Produto("Notebook", 2500.00);
        assertEquals("Notebook", produto.getNome(), "O método getNome deve retornar o nome correto.");
    }
}
