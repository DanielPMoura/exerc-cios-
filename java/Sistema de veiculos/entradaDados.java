import java.util.Scanner;
import java.util.ArrayList;
import java.util.InputMismatchException;
public class entradaDados {
    public static void main(String[] args) {
        
        Scanner sc= new Scanner(System.in);
        ArrayList<veiculo> lista= new ArrayList<>();
        String tipoVeiculo;
        
        
        System.out.println("Digite o tipo de veiculo (carro/moto):");
        tipoVeiculo=sc.nextLine();
    try{
        if (tipoVeiculo.equalsIgnoreCase("carro")) {
            
            System.out.println("Digite o modelo do veiculo");
            String modelo=sc.nextLine();
            
            System.out.println("Digite o ano do veiculo:");
            int ano=sc.nextInt();
            
            lista.add(new carro(modelo,ano));
            System.out.println("realizado com sucesso");
        }
        else if(tipoVeiculo.equalsIgnoreCase("moto")){
            System.out.println("Digite o modelo do veiculo");
            String modelo=sc.nextLine();
            
            System.out.println("Digite o ano do veiculo:");
            int ano=sc.nextInt();
            
            lista.add(new moto(modelo,ano));
            System.out.println("realizado com sucesso");
            
            
        }else{
            System.out.println("tipo de veiculo invalido");
            
        }
        
    }catch(IllegalArgumentException e){
            System.out.println("Erro: "+e.getMessage());
        }
        catch(InputMismatchException e){
            System.out.println("Erro: entrada de dados invalida");
        }finally{
            System.out.println("\nLista de Veículos:");
            for(veiculo v: lista){
                v.exibir();
            }
        }
    }
}
