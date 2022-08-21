import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();
        int m = sc.nextInt();
        H = H+((M+m)/60);
        m = (M+m)%60;
        if(H>=24) H=H%24;
        System.out.println(H + " " + m);
    }
}