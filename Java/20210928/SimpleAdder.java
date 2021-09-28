package T210928;

public class SimpleAdder {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		 * 자바 프로그램의 구성요소
		 * 키워드 : 미리 약속된 단어(변수명으로 사용 불가능)
		 * 식별자 : 
		 * 상수 : true, false...
		 * 데이터 : 문자열(String), 문자(char), 정수(int), 소수(float) 등
		 * 변수 : 데이터를 담는 그릇
		 * 변수의 선언 : int num;(int형의 num 변수 선언)
		 * 대입문 : num = 10 + 20;(변수에 데이터를 담는 명령문)
		 * = 대입, == 비교연산자
		 */
		int num;
		num = 10 + 20;
		System.out.println(num);
		if(num > 10) System.out.println("계산 결과가 10보다 큽니다.");
	}

}
