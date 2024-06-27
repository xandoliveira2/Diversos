package view;

import model.Produto;

import javax.lang.model.type.ErrorType;
import java.nio.channels.ScatteringByteChannel;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class GerenciarEstoque {
    public static Scanner sc = new Scanner(System.in);
    public static List<Produto> produtos = new ArrayList();
    public static void main(String[] args) {  //main -> onde vai rodar nosso codigo principal


            int opcao = 9;
            while (opcao != 0) {
                System.out.println("Selecione a opção:");
                System.out.println("1-Cadastrar produto");
                System.out.println("2-Alterar dados de um produto");
                System.out.println("3-Excluir produto");
                System.out.println("4-Entrada no estoque");
                System.out.println("5-Saída no estoque");
                System.out.println(("6-Saldo atual no estoque"));
                System.out.println("7-Listar produtos");
                System.out.println("0-Sair");
                System.out.println("Digite uma opção:");
                try{
                opcao = Integer.parseInt(sc.nextLine());}catch (Exception e){
                    System.out.println("Erro: "+e);
                }

                switch (opcao) {
                    case 1:
                        Cadastrar_produto();
                        break;
                    case 2:
                        Alterar_produto();
                        break;
                    case 3:
                        Remover_produto();
                        break;
                    case 4:
                        Entrada_estoque();
                        break;
                    case 5:
                        Saida_estoque();
                        break;
                    case 6:
                        Quantidade_estoque();
                        break;
                    case 7:
                        listar();
                        break;
                    case 0:
                        return;
                    default:
                        System.out.println("Não existe essa opção");
                        break;

                }
            }



    }

    public static void Cadastrar_produto (){ // função cadastrar que vai solicitar para o usuario nome,qtde,e preco do produto que ele vai cadastrar
        try{
        System.out.println("Digite nome do produto:");
        String nome = sc.nextLine();
        System.out.println("Digite quantidade do produto em estoque:");
        int quantidade = Integer.parseInt(sc.nextLine());
        System.out.println("Digite preço do produto:");
        double preco = Double.parseDouble(sc.nextLine());
        produtos.add(new Produto(nome,quantidade,preco));
        System.out.println("Cadastrado com sucesso");}
        catch (Exception e){
            System.out.println("Erro: "+e);
        }
    }
    public static void Remover_produto(){//função para remover uma determinada quantidade de produtos de um produto
        try{ // o codigo pede o nome do produto (nosso identificador) e a quantidade que vai remover
        System.out.println("Digite nome do produto que você quer alterar:");
        String nome = sc.nextLine();
        for (Produto o : produtos){
            if (o.getNome().equalsIgnoreCase(nome))
            {
                produtos.remove(o);
                System.out.println("Produto removido com sucesso");
                return;
            }

            } System.out.println("Não existe esse cadastro");
        }
        catch (Exception e){
            System.out.println("Erro: "+e);
        }
    }
    public static void Alterar_produto(){
        try { //aqui temos a função para deixamos para o usuario digitar oque deseja alterar no produto puxando pelo nome dele
            System.out.println("Digite nome do produto que você quer alterar:");
            String nome = sc.nextLine();
            for (Produto o : produtos) {
                if (o.getNome().equalsIgnoreCase(nome)) {
                    int opcao = 0;
                    while (opcao != 9) {
                        System.out.println("Digite a opção que deseja fazer:");
                        System.out.println("1-Alterar nome");
                        System.out.println("2-Alterar quantidade");
                        System.out.println("3-Alterar preço");
                        System.out.println("9-Sair");

                        opcao = Integer.parseInt(sc.nextLine());



                        switch (opcao) {
                            case 1:
                                System.out.println("Digite novo nome:");

                                String novonome = sc.nextLine();

                                o.setNome(novonome);
                                System.out.println("Nome alterado com sucesso");
                                break;
                            case 2:
                                System.out.println("Digite quantidade atual:");
                                int novaquantidade = Integer.parseInt(sc.nextLine());
                                o.setQuantidade(novaquantidade);
                                System.out.println("Quantidade alterada com sucesso");
                                break;
                            case 3:
                                System.out.println("Digite preço atual:");
                                double novopreco = Integer.parseInt(sc.nextLine());
                                o.setPreco(novopreco);
                                System.out.println("Preço alterado com sucesso");
                                break;
                            case 9:
                                return;
                            default:
                                System.out.println("Opção inválida");
                                break;

                        }
                }



                } else {
                    System.out.println("Não existe esse cadastro");
                }
            }
        }catch (Exception e){
            System.out.println("Erro "+e);
        }
    }

    public static void Entrada_estoque(){ //informando nome e quantidade de produtos para adicionar
        try{
        listar_nomes();
        System.out.println("Digite nome do produto que deseja adicionar mais unidades:");
        String nome = sc.nextLine();
        System.out.println("Digite número de unidades que irá adicionar:");
        int numero = Integer.parseInt(sc.nextLine());


        Produto o =procurar(nome);
        if (o.getNome().equalsIgnoreCase("null")){
            System.out.println("Produto não existe");
        }else{
            o.adicionar_estoque(numero);
            System.out.println("Foi adicionado ao produto "+o.getNome()+", "+numero+" produtos. Atualmente tem no estoque: "+o.getQuantidade()+" unidades.");
        }
    }catch (Exception e){
            System.out.println("Erro: "+e);

        }
    }
    public static void Saida_estoque(){ //informando nome e quantidade de conteudo p sair do estoque
        try {
            listar_nomes();
            System.out.println("Digite nome do produto que deseja remover unidades:");
            String nome = sc.nextLine();
            System.out.println("Digite número de unidades que irá remover:");
            int numero = Integer.parseInt(sc.nextLine());
            Produto o = procurar(nome);
            if (o.getNome().equalsIgnoreCase("null")) {
                System.out.println("Produto não existe");
            } else {
                o.diminuir_estoque(numero);
                System.out.println("Foi removido no estoque o produto  " + o.getNome() + ", " + numero + " produtos. Atualmente tem no estoque: " + o.getQuantidade() + " unidades.");
            }
        }catch (Exception e){
            System.out.println("Erro: "+e);
        }
    }
    public static Produto procurar(String nome){ //função externa apenas para procurar o objeto usando nome para evitar ficar copiando
        //esse codigo toda hora para procurar
        for (Produto o: produtos){
            if (o.getNome().equalsIgnoreCase(nome)){
                return o;
            }
        }
        return new Produto("null",0,0);
        }
        public static void Quantidade_estoque(){ //função simples apenas para mostrar itens disponiveis para consulta e mostrar a quantidade de itens daquele produto vai ter
        try {
            listar_nomes();
            System.out.println("Digite nome para ver a quantidade de unidades desse produto");
            String nome = sc.nextLine();
            Produto a = procurar(nome);
            if (a.getNome().equalsIgnoreCase("null")) {
                System.out.println("Não existe esse produto no estoque");
            } else {
                System.out.println("Tem no estoque: " + a.getQuantidade() + " unidades do produto " + nome + ".");
            }
        }catch (Exception e){System.out.println("Erro: "+e);}
        }


        public static void listar(){ // função para mostrar todos os itens da lista produtos
        if (produtos.size() == 0){
            System.out.println("Não tem produtos para mostrar");
            return;
        }
        for (Produto o: produtos){
            System.out.println(o);
        }
        }

        public static void listar_nomes(){// função externa para mostrar apenas os nomes dos produtos para quando o usuario precisar
        //digitar o nome de algum produto ter um 'gabarito' para saber o nome dos produtos e não precisar muito de decorar cada nome
        System.out.println("Produtos disponíveis");
        for (Produto o: produtos){
            System.out.println("-"+o.getNome());
        }
        }
}
