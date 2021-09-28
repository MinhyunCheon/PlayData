package T210928;

import java.util.Scanner;
public class Larger {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x, y, max;
		
		Scanner in = new Scanner(System.in);
		System.out.print("첫번째 정수 : ");
		x = in.nextInt();
		System.out.print("두번째 정수 : ");
		y = in.nextInt();
		
		if(x > y) max = x;
		else max = y;
		
		System.out.println("큰 수는 " + max + "입니다.");
	}

}
