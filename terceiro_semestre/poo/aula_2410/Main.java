package aula_2410;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        
        ArrayList<String> cidades = new ArrayList<>();

        cidades.add("São Paulo");
        cidades.add("Rio de Janeiro");
        cidades.add("Curitiba");
        cidades.add("Belo Horizonte");
        cidades.add("Porto Alegre");
        cidades.add("Brasília");
        cidades.add("Fortaleza");
        cidades.add("Goiânia");
        cidades.add("Bichinho");
        cidades.add("São Miguel do Gostoso");


        System.out.println("Lista de cidades:");
        for (String cidade : cidades) {
            System.out.println(cidade);
        }

        cidades.remove("São Paulo");

        System.out.println("\nApós remover uma cidade:");
        for (String cidade : cidades) {
            System.out.println(cidade);
        }

        System.out.println(cidades.size());
    }
}
