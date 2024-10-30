package provaA1.q7;

public Pessoa carregarPessoaDoArquivo(String nomeArquivo) throws IOException, ClassNotFoundException {
    FileInputStream arquivoLeitura = new FileInputStream(nomeArquivo);
    ObjectInputStream objLeitura = new ObjectInputStream(arquivoLeitura);
    Pessoa pessoa = (Pessoa) objLeitura.readObject();
    objLeitura.close();
    arquivoLeitura.close();
    return pessoa;
}

