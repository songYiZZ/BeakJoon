import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        String str = sc.next();
        int temp = 0;
        for(int i=0; i<size; i++){
            temp += Integer.parseInt(str.charAt(i)+"");
        }
        System.out.println(temp);
    }
}