import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        String star = "";
        for(int i=0; i<size; i++){
            star += "*";
            System.out.println(star);
        }
    }
}