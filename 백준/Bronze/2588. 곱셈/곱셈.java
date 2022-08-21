import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        String B = sc.next();
        for(int i=B.length()-1; i>=0; i--){
            System.out.println(A*(Integer.parseInt(B.charAt(i)+"")));
        }
        System.out.println(A * (Integer.parseInt(B)));
    }
}