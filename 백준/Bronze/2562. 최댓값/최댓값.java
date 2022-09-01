import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int num = 0;
		int cnt = 0;
		int max = 0;
		for(int i=0; i<9; i++){
			StringTokenizer st = new StringTokenizer(br.readLine());
			num = Integer.parseInt(st.nextToken());
			if(max < num){
				max = num;
				cnt = i+1;
			}
		}
		System.out.println(max+"\n"+cnt);
    }
}