public abstract class Funcionario{

    protected String nome;
    protected double SalarioBase;

    public Funcionario(String nome, double SalarioBase){
        this.SalarioBase = SalarioBase;
        this.nome = nome;
        if (SalarioBase<=0) {
            System.out.println("Salário base deve ser maio que zero.");
        }
        if(nome.isEmpty()){
            System.out.println("Nome do funcionário não pode ser vazio.");

        }

            

    }

    public abstract double calcularSalario();

    public void exibir(){
        System.out.println("Nome: "+nome);
        System.out.println("Salario Base: "+SalarioBase);
        System.out.println("Salario Final "+calcularSalario());
    }
}