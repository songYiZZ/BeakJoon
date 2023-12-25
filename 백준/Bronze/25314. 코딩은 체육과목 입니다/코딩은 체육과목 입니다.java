import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        String result = "";
        boolean go = true;
        while(go){
            if(input-4 > 0){
                result += "long ";
                input = input-4;
            }else{
                result += "long int";
                go = false;
            }
        }
        System.out.println(result);
    }
}
