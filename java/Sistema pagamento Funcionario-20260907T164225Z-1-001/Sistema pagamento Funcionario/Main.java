import java.util.Scanner;
import java.util.ArrayList;

public class  Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Funcionario> funcionarios = new ArrayList<>();

        
        for (int i = 0; i < 2; i++) {
            System.out.println("Digite os dados do " + (i + 1) + "° funcionário:");

            
            System.out.print("Nome: ");
            String nome = sc.nextLine();

            System.out.print("Salário: R$ ");
            double salario = sc.nextDouble();
            sc.nextLine(); 

            
            System.out.print("O funcionário é Gerente ou Vendedor? ");
            String tipo = sc.nextLine().trim().toLowerCase();

            
            Funcionario funcionario = null;
            if (tipo.equals("gerente")) {
                funcionario = new gerente(nome, salario);
            } else if (tipo.equals("vendedor")) {
                funcionario = new vendedor(nome, salario);
            } else {
                System.out.println("Tipo inválido, criando como Vendedor por padrão.");
                funcionario = new vendedor(nome, salario); 
            }

            
            funcionarios.add(funcionario);
        }

        System.out.println("\nDados dos Funcionários:");
        for (Funcionario funcionario : funcionarios) {
            funcionario.exibir();
            System.out.println();
        }

        sc.close(); 
    }
}
