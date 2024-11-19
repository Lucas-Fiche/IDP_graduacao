package org.example;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Cidade> cidades = Arrays.asList(
                new Cidade("GO", "Anápolis", false),
                new Cidade("GO", "Goiânia", true),
                new Cidade("SP", "Ribeirão Preto", false),
                new Cidade("SP", "Campinas", false),
                new Cidade("MG", "Belo Horizonte", true),
                new Cidade("MG", "Uberlândia", false),
                new Cidade("MG", "Montes Claros", false),
                new Cidade("MG", "Unaí", false),
                new Cidade("TO", "Palmas", true),
                new Cidade("TO", "Araguarí", false),
                new Cidade("MT", "Cuiabá", true),
                new Cidade("MS", "Dourados", false),
                new Cidade("MS", "Campo Grande", true),
                new Cidade("MS", "Corumbá", false),
                new Cidade("MT", "Barra do Garças", false),
                new Cidade("MT", "Araguaiana", false),
                new Cidade("RO", "Porto Velho", true),
                new Cidade("RO", "Costa Marques", false)
        );

        // Agrupamento por UF e ordenação alfabética
        Map<String, Set<String>> cidadesPorUF = new TreeMap<>();
        for (Cidade cidade : cidades) {
            cidadesPorUF.putIfAbsent(cidade.getUf(), new TreeSet<>());
            cidadesPorUF.get(cidade.getUf()).add(cidade.getNome());
        }
        System.out.println("Cidades agrupadas por UF em ordem alfabética:");
        for (Map.Entry<String, Set<String>> entry : cidadesPorUF.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        // Ordenação por capitais e nome
        cidades.sort(Comparator.comparing(Cidade::isCapital).reversed().thenComparing(Cidade::getNome));
        System.out.println("\nCidades com capitais primeiro e em ordem alfabética:");
        for (Cidade cidade : cidades) {
            System.out.println((cidade.isCapital() ? "(Capital) " : "") + cidade.getNome());
        }

        // Conjunto de cidades em ordem decrescente
        Set<String> conjuntoCidades = new TreeSet<>(Comparator.reverseOrder());
        for (Cidade cidade : cidades) {
            conjuntoCidades.add(cidade.getNome());
        }
        System.out.println("\nCidades em ordem alfabética decrescente:");
        for (String nome : conjuntoCidades) {
            System.out.println(nome);
        }
    }
}