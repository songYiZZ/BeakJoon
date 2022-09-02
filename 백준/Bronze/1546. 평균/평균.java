import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double[] arr = new double[sc.nextInt()];
        for(int i=0; i<arr.length; i++){
            arr[i] = sc.nextInt();
        }
        double max = Arrays.stream(arr).max().getAsDouble();
        for(int i=0; i<arr.length; i++){
            arr[i] = arr[i]/max*100;
        }
        System.out.println(Arrays.stream(arr).average().getAsDouble());
    }
}