package aula_0609;

public class Principal {
    public static void main(String[] args){
        Animal animal = new Animal();
        animal.falar();
        animal.andar();

        Cachorro lauda = new Cachorro();
        lauda.nome = "lauda";
        lauda.falar();
        lauda.andar();
        System.out.println(lauda);

        Gato pituca = new Gato();
        pituca.nome = "pituca";
        pituca.falar();
        pituca.andar();
        System.out.println(pituca);

        Raposa raposa = new Raposa();
        raposa.nome = "raposa";
        raposa.falar();
        raposa.andar();

    }
}
