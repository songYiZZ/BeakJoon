import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = sc.nextInt();
        int size = sc.nextInt();
        int[] arr = new int[size];
        for (int money : arr){
            money = sc.nextInt();
            int amt = sc.nextInt();
            sum -= money*amt;
        }
        if(sum == 0) System.out.println("Yes");
        else System.out.println("No");
    }

}