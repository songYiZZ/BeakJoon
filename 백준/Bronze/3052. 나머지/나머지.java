import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] arr = new String[10];
        for(int i=0; i<10; i++){
            arr[i] = sc.nextInt()%42+"";
        }
        System.out.println(Arrays.stream(arr).distinct().count());
    }
}