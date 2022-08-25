import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int standard = sc.nextInt();
        String result = "";
        for(int i=0; i<size; i++){
            int temp = sc.nextInt();
            if(temp < standard){
                result += temp + " ";
            }
        }
        System.out.println(result);
    }
}