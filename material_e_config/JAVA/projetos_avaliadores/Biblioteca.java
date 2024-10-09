import java.util.Scanner;
public class Biblioteca {
    public Livro livro = new Livro();

    public static void main(String[] args) {
        Biblioteca livros = new Biblioteca() ;
        int opcao = 0;
        do{
            System.out.println("Digite a opção que deseja:");
            System.out.println("1-Cadastrar livro");
            System.out.println("2-Emprestar livro");
            System.out.println("3-Devolver livro");
            System.out.println("4-Exibir livros");
            System.out.println("9-Sair");
            Scanner leitor = new Scanner(System.in);
            opcao=Integer.parseInt(leitor.nextLine());
            switch (opcao){
                case 1: livros.cadastrarLivros();
                    break;
                case 2: livros.emprestarLivro();
                    break;
                case 3: livros.devolverLivro();
                    break;
                case 4: livros.exibirLivro();
                    break;
                case 9:
                    System.out.println("Fim");
                    break;
                default:
                    System.out.println("Número inválido");
            }
        }
        while(opcao != 9);
    }
    public void exibirLivro(){
        for (int i=0;i<dados.length;i++){
            if (dados[i] == null ){break;}
            else{
                System.out.println(dados[i]);
            }
        }
    }
    public String[] dados = new String[3000];
    public int cont = 0;
    public void cadastrarLivros(){
        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite titulo do livro: ");
        livro.titulo = leitor.nextLine();
        System.out.println("Digite autor do livro: ");
        livro.autor = leitor.nextLine();
        livro.disponivel = "true";
        dados[cont]=livro.titulo;
        cont++;
        dados[cont]=livro.autor;
        cont++;
        dados [cont]=livro.disponivel;
        cont++;
    }
    public void emprestarLivro(){
        System.out.println("Digite nome do livro que você queira emprestar:");
        Scanner leitor = new Scanner(System.in);
        String titulo = leitor.nextLine();
        for (int i=0; i< dados.length;i++){
            if (dados[i].equals(titulo)){
                if (dados[i+2].equals("true")){
                    System.out.println("Livro emprestado");
                    dados[i+2] = "false";
                    break;}
                else{
                    System.out.println("Erro no empréstimo. Livro não se encontra na biblioteca");
                    break;
                }}else{
                System.out.println("Livro não encontrado");
                break;
            }}
    }
    public void devolverLivro(){
        System.out.println("Digite nome do livro que você queira devolver:");
        Scanner leitor = new Scanner(System.in);
        String titulo = leitor.nextLine();
        for (int i=0; i< dados.length;i++){
            if (dados[i].equals(titulo)){
                if (dados[i+2].equals("false")){
                    System.out.println("Livro devolvido");
                    dados[i+2] = "true";
                    break;}else{
                    System.out.println("Erro na devolução. Livro já se encontra na biblioteca");
                    break;
                }
            }
        }
    }
}
