import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String sb = "";
        int a = 0;
        int b = 0;
        while(true){
            a = sc.nextInt();
            b = sc.nextInt();
            if(a + b > 0){
                sb += (a+b) + "\n";
            }else{
                break;
            }
        }
        System.out.println(sb);
    }
}