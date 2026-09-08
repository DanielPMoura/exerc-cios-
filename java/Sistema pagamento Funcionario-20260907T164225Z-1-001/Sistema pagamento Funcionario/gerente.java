public class gerente extends Funcionario implements bonificação{

    public gerente(String nome, double SalarioBase) {
        super(nome,SalarioBase);

    }
    @Override

    public double calcularBonus() {
        return 1000;    
    }
    @Override
    public double calcularSalario() {
        return SalarioBase + calcularBonus();
   
}
}
