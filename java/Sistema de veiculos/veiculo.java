public abstract class veiculo{
    protected String modelo;
    protected int ano;



    public veiculo (String modelo, int ano){
        this.modelo=modelo;
        this.ano=ano;
        if(modelo.isEmpty()){
            throw new IllegalArgumentException("modelo invalido");
        }
        if(ano<2000){
            throw new IllegalArgumentException("ano invalido");
        }
        
    }
    
    public abstract double calcularValor();
    
    public void exibir(){
        System.out.println("Modelo: "+modelo);
        System.out.println("Ano: "+ano);
        System.out.println("valor: "+calcularValor());
        
    }
}