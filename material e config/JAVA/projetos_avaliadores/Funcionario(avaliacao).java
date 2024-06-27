public class Funcionario {
    public Funcionario(double salario, String nome, String departamento, String rg) {
        this.salario = salario;
        this.nome = nome;
        this.departamento = departamento;
        this.rg = rg;
        this.ativo = true;
    }

    private double salario;
    private String nome;
    private String departamento;
    private String rg;
    private boolean ativo;

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public String getRg() {
        return rg;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }

    public boolean getAtivo() {

        return ativo;

    }

    @Override
    public String toString() {
        return "Funcionario{" +
                "salario=" + salario +
                ", nome='" + nome + '\'' +
                ", departamento='" + departamento + '\'' +
                ", rg='" + rg + '\'' +
                ", ativo=" + ativo +
                '}';
    }
    public void inativar(){
        this.ativo = false;

    }
    public void ativar(){
        this.ativo = true;

    }

    public int isAtivo(){
        if (this.ativo) {System.out.println("Funcionario atual se encontra com registro ATIVO");
            return 1;
        }
        else{System.out.println("Funcionario atual se encontra com registro INATIVO");
            return 0;
        }
    }
    public void bonificar(double salario){
        this.salario = this.salario + salario;
        System.out.println("Salário atualizado, novo salário declarado:"+this.salario);

    }
}
