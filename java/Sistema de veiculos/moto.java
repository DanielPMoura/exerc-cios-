public class moto extends veiculo {

public moto(String modelo, int ano){
    super(modelo,ano);
}
@Override
public double calcularValor(){
    return 15000;


}
}
