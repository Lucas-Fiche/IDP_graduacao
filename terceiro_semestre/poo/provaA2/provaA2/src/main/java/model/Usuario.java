package model;

public class Usuario {
    private int matricula;
    private String senha;
    private String sobrenome;
    private String email;
    private String telefone;

    // Construtor
    public Usuario(int matricula, String senha, String sobrenome,
                   String email, String telefone) {
        this.matricula = matricula;
        this.senha = senha;
        this.sobrenome = sobrenome;
        this.email = email;
        this.telefone = telefone;
    }

    // Getters e Setters (gere usando Alt+Insert no IntelliJ)
    public int getMatricula() { return matricula; }
    public void setMatricula(int matricula) { this.matricula = matricula; }

    public String getSenha() { return senha; }
    public void setSenha(String senha) { this.senha = senha; }

    public String getSobrenome() { return sobrenome; }
    public void setSobrenome(String sobrenome) { this.sobrenome = sobrenome; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getTelefone() { return telefone; }
    public void setTelefone(String telefone) { this.telefone = telefone; }
}
