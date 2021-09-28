package T210928;

import java.util.Scanner;
public class Grade {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		System.out.print("점수를 입력하세요 : ");
		int score = s.nextInt();
		String grade = "";
		
		if(score >= 90) grade = "A";
		else if(score >= 80) grade = "B";
		else if(score >= 70) grade = "C";
		else if(score >= 60) grade = "D";
		else grade = "F";

		System.out.println("성적은 " + grade + "입니다.");
	}

}
