import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int cnt = 0;

		int[] arr = new int[]{(num/10),(num%10)};
		while(true){
			cnt++;
			int tmp = 0;
			tmp = arr[0];
			arr[0] = arr[1];
			arr[1] = (tmp+arr[1])%10;
			if(num == ((arr[0]*10)+(arr[1]*1))){
				break;
			}
		}
		System.out.println(cnt);
		}
    }