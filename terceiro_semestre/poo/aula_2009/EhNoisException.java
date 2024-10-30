package aula_2009;

public class EhNoisException {
    public EhNoisException(String message) {
        super(">>" + message);
        System.err.println("é noisss!!!!!");
    }
}
