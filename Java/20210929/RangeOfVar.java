package T210929;

public class RangeOfVar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int value1 = 3;
		{
			int value2 = 5;
			System.out.println(value1);
			System.out.println(value2);
		}
		System.out.println(value1);
//		System.out.println(value2);	// 오류 발생(value2는 스코프 만료)
	}

}