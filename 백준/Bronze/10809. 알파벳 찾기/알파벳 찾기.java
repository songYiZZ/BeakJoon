import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        String[] s = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        String result = "";
        for(int i=0; i<s.length; i++){
            result += str.indexOf(s[i])+" ";
        }
        System.out.println(result);

    }
}