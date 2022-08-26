import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int[] arr = new int[size];
        for(int i=0; i<arr.length; i++){
            arr[i] = sc.nextInt()+sc.nextInt();
        }
        for(int i=0; i<arr.length; i++){
            System.out.println("Case #"+(i+1) + ": "+arr[i]);
        }
    }
}