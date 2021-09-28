package T210928;

import java.util.Scanner;
public class Bonus {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		final int TARGET = 1000;
		int sales;
		int bonus;
		String result;
		
		Scanner s = new Scanner(System.in);
		System.out.print("실적을 입력하세요. : ");
		sales = s.nextInt();
		
		if(sales >= TARGET) {
			result = "실적 달성";
			bonus = (sales - TARGET) / 10;
		}
		
		else {
			result = "실적 미달성";
			bonus = 0;
		}
		System.out.println(result + "\n" + "보너스 : " + bonus);
	}

}
