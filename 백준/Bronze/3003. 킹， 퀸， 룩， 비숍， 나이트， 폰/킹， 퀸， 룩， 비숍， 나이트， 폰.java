import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] chess = {1,1,2,2,2,8};
        int[] tmp = new int[6];
        for(int i=0; i<tmp.length; i++){
            tmp[i] = sc.nextInt();
        }
        String str = "";
        for(int i=0; i<chess.length;i++){
            str += (chess[i]-tmp[i])+" ";
        }
        System.out.println(str);
    }
}