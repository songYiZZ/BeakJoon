import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int tmp = 0;
        while(a>0){
            tmp += a;
            a--;
        }
        System.out.println(tmp);
    }

}