public class carro extends veiculo{


public carro(String modelo, int ano){
    super(modelo,ano);
}
@Override
public double calcularValor(){
    return 30000;


}
}
