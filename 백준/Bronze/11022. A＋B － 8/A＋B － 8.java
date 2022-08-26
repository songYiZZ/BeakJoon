import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        String[] arr = new String[size];
        for(int i=0; i<arr.length; i++){
            int tmp1 = sc.nextInt();
            int tmp2 = sc.nextInt();
            arr[i] = tmp1+" + " +tmp2+" = " + (tmp1+tmp2);
        }
        for(int i=0; i<arr.length; i++){
            System.out.println("Case #"+(i+1) + ": "+arr[i]);
        }
    }
}