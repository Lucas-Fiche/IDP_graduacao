package aula_2709;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        // Nome do arquivo onde o conteúdo será salvo
        String nomeDoArquivo = "aula_2709/arquivo.txt";
        // Conteúdo a ser salvo no arquivo
        String conteudo = "Este é o conteúdo que será salvo no arquivo.";

        // Tentativa de escrita no arquivo
        try {
            // Cria o FileWriter, permitindo escrita no arquivo
            FileWriter fw = new FileWriter(nomeDoArquivo);
            // Escreve o conteúdo no arquivo
            fw.write(conteudo);
            // Fecha o FileWriter para liberar o recurso
            fw.close();
            // Mensagem de sucesso
            System.out.println("Conteúdo salvo com sucesso!");
        } catch (IOException e) {
            // Trata qualquer exceção de IO
            System.out.println("Ocorreu um erro ao salvar o arquivo.\n");
            e.printStackTrace();
        }
    }
}


