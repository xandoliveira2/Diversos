package model;
import java.text.DecimalFormat;
public class Produto {
    private String nome;
    private int quantidade;
    private double preco;

    public Produto(String nome, int quantidade, double preco) {
        this.nome = nome;
        this.quantidade = quantidade;
        this.preco = preco;
    }
    public void adicionar_estoque(int numero){
        this.quantidade+=numero;
    }
    public void diminuir_estoque(int numero){//quantidade nao pode ser menor que 0
        if (this.quantidade-numero <0){
            System.out.println("Erro, não pode ter menos que 0");
        }else{
        this.quantidade-=numero;}
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {//quantidade nao pode ser menor que 0
        if (quantidade<0){
            System.out.println("Erro, não pode ter menos que 0");
        }else{
        this.quantidade = quantidade;}
    }

    public double getPreco() {
        return preco;
    }


    public void setPreco(double preco) { //preco nao pode ser menor ou igual a 0
        if (preco <=0){
            System.out.println("Preço não pode ser 0 ou menor");
        }else{
        this.preco = preco;}
    }

    @Override
    public String toString() {
        double numero = this.preco;
        DecimalFormat df = new DecimalFormat("#.##");
        String numeroFormatado = df.format(numero);
          // Saída: 3.14
        return
                "nome= " + nome +
                ".\nquantidade= " + quantidade +
                ".\npreco= " + numeroFormatado+ " .\n";
    }
}
