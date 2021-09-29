package T210929;

public class RelationOperator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 비교 연산자
		System.out.println(5 < 2);
		System.out.println(5 > 2);
		System.out.println(5 < 5);
		System.out.println(5 <= 5);
		System.out.println(5 >= 5);
		System.out.println(5 == 5);
		System.out.println(5 != 5);
		System.out.println(5 == 3);
		System.out.println(5 != 3);
		
		// reference 비교
		String str1 = new String("안녕");
		String str2 = new String("안녕");
		System.out.println(str1 == str2);
	}

}
