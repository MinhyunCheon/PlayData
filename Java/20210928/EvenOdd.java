package T210928;

import java.util.Scanner;
public class EvenOdd {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num;
		Scanner s = new Scanner(System.in);
		System.out.print("정수를 입력해주세요 : ");
		num = s.nextInt();
		String msg = "";
		
		if(num % 2 == 0) msg = "입력된 정수는 짝수입니다.";
		else msg = "입력된 정수는 홀수입니다.";
		
		System.out.println(msg);
		System.out.println("종료되었습니다.");
	}

}
