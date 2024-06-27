import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class GerenciarFuncionario {

    public static List<Funcionario> funcionarios = new ArrayList<>();
    static Scanner leitor = new Scanner(System.in);
    public static void main(String[] args) {
        int opcao = 0;
        while (opcao != 9){
            System.out.println("O que deseja realizar?");
            System.out.println("1 - Cadastrar novo funcionário.");
            System.out.println("2 - Consultar funcionário por RG.");
            System.out.println("3 - Consultar todos funcionários cadastrados.");
            System.out.println("4 - Alterar dados.");
            System.out.println("5 - Inativar conta de um funcionario.");
            System.out.println("6 - Excluir dados de um funcionário.");
            System.out.println("7 - Bonificar funcionário.");
            System.out.println("8 - Reativar conta de um funcionário.");
            System.out.println("9 - Encerrar programa.");
            opcao = Integer.parseInt(leitor.nextLine());
        switch (opcao){
            case 1:
                System.out.println("Digite o nome:");
                String nome = leitor.nextLine();
                System.out.println("Digite o departamento:");
                String departamento = leitor.nextLine();
                System.out.println("Digite o rg:");
                String rg = leitor.nextLine();
                System.out.println("Digite o salário:");
                double salario = Double.parseDouble(leitor.nextLine());
                execCadastrar(nome,departamento,rg,salario);
                break;
            case 2:
                String rg1;
                System.out.println("Digite o rg:");
                rg1 = leitor.nextLine();
                execConsultar(rg1);
                break;
            case 3:
                execConsultar();

                break;
            case 4:
                String rg2;
                System.out.println("Digite o rg:");
                rg2 = leitor.nextLine();
                execAlterar(rg2);
                break;
            case 5:
                String rg3;
                System.out.println("Digite o rg:");
                rg3 = leitor.nextLine();
                execInativar(rg3);
                break;
            case 6:
                String rg4;
                System.out.println("Digite o rg:");
                 rg4 = leitor.nextLine();
                execExcluir(rg4);
                break;
            case 7:
                String rg5;
                double bonificacao;
                int contador = 0;
                System.out.println("Digite o rg:");
                rg5 = leitor.nextLine();
                System.out.println("Digite o valor da bonificação:");
                bonificacao = Double.parseDouble(leitor.nextLine());
                while (contador < funcionarios.size()){
                    if (funcionarios.get(contador).getRg().equals(rg5)){
                        if (!funcionarios.get(contador).getAtivo()){
                            System.out.println("Impossivel modificar salário de um cadastro inativo");
                            break;
                        }
                        else{
                        funcionarios.get(contador).bonificar(bonificacao);}
                        break;
                    }
                    ++contador;
                    if (contador == funcionarios.size()){
                        System.out.println("Rg não encontrado");
                        break;
                    }

                }
                break;
            case 8:
                String rg6;
                System.out.println("Digite o rg:");
                rg6 = leitor.nextLine();
                execAtivar(rg6);
                break;
            case 9:
                System.out.println("Programa encerrado");
                return;
            default:
                System.out.println("Número não corresponde a nenhuma das opções");
                break;
        }

        }







    }


    public static void execConsultar(String rg){
        int cont = 0;
        while (cont<funcionarios.size()){
            if (funcionarios.get(cont).getRg().equals(rg)){
                System.out.println(funcionarios.get(cont).toString());
            }
            ++cont;
        }
    }
    public static void execAtivar(String rg){
        int index = 0;
        while (index<funcionarios.size()){
                if (funcionarios.get(index).getRg().equals(rg)){
                    if(funcionarios.get(index).getAtivo()){
                        System.out.println(("Erro! conta ja se encontra ativada"));

                    }
                    else{funcionarios.get(index).ativar();
                        System.out.println("Conta reativada com sucesso.");
                    }
            }
            ++index;
        }
    }
    public static void execInativar(String rg) {
        int index = 0;
        while (index<funcionarios.size()) {
            if (funcionarios.get(index).getRg().equals(rg)) {
                if (!funcionarios.get(index).getAtivo()) {
                    System.out.println(("Erro! conta ja se encontra inativada"));
                } else {
                    funcionarios.get(index).inativar();
                    System.out.println("Conta inativada com sucesso");
                }
            }
            ++index;
        }
    }
    public static void execConsultar(){int cont = 0;
        while (cont< funcionarios.size()){
            System.out.println(funcionarios.get(cont));
            ++cont;


        }
    }
    public static void execAlterar(String rg){
        System.out.println("Digite dados que você quer alterar do rg:"+rg);
        int cont =0;
        while (cont<funcionarios.size()){
            if (funcionarios.get(cont).getRg().equals(rg)){
                if (!funcionarios.get(cont).getAtivo()){
                    System.out.println("Impossivel alterar funcionario com cadastro inativo");
                    break;
                }

            }
            cont++;

        }
        System.out.println("1 - Nome");
        System.out.println("2 - Departamento");
        int resultado = Integer.parseInt(leitor.nextLine());
        cont = 0;
        switch (resultado){
            case 1:
                String nome;
                System.out.println("Insira novo nome:");
                nome = leitor.nextLine();
                while (cont < funcionarios.size()){
                    if (funcionarios.get(cont).getRg().equals(rg)){
                        funcionarios.get(cont).setNome(nome);
                        System.out.println("Nome atualizado com sucesso");
                        break;
                    }
                    ++cont;
                    if (cont == funcionarios.size()){
                        System.out.println("Rg não encontrado");
                        break;
                    }
                }

            case 2:
                String departamento;
                System.out.println("Insira novo departamento");
                departamento = leitor.nextLine();
                while (cont < funcionarios.size()){
                    if (funcionarios.get(cont).getRg().equals(rg)){
                        funcionarios.get(cont).setDepartamento(departamento);
                        System.out.println("Departamento atualizado com sucesso");
                        break;
                    }
                    ++cont;
                    if (cont == funcionarios.size()){
                        System.out.println("Rg não encontrado");
                        break;
                    }
                }
                break;
            default:
                System.out.println("Digito fora de alcance");
        }
    }
    public static void execExcluir(String rg){
        int index = 0;
        while (index<funcionarios.size()){
            if (funcionarios.get(index).getRg().equals(rg)){
                funcionarios.remove(index);
                System.out.println("Excluido dados sobre funcionario");
            }
            ++index;
        }
    }
    public static void execCadastrar(String nome, String departamento, String rg, double salario)
    {

    Funcionario funcionario = new Funcionario(salario,nome,departamento,rg);
        System.out.println("Cadastrado com sucesso");
        funcionarios.add(funcionario);
    }





}
