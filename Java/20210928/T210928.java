package T210928;
/*
 * public : 접근 제어 지시자, 모든 접근을 허용하므로 보안성은 낮음
 * 클래스명은 Camel Case를 따라 첫글자와 음절마다 대분자를 사용하여 작성
 * class : 클래스임을 명시
 */
public class T210928 {
	/*
	 * public static : 메모리에 가장 먼저 로드
	 * void : return 값이 없음을 명시
	 * main : 메소드명
	 * String[] args : String 배열 args는 변수명
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/* 표준 입/출력
		 * 컴퓨터가 기본적으로 제공하는 입/출력, System 패키지에 정의
		 * 입력 : 키보드(System.in)
		 * 출력 : 모니터(System.out, System.err)
		 * System : 클래스명
		 * out : 변수
		 * println : 메소드명
		 * System.out.println(); : 표준 출력 명령
		 * "Hello Java!" : 출력할 문자열
		 */
		System.out.println("Hello Java!");
	}

}
