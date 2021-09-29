package T210929;

public class TypeCasting_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 캐스팅 방법 1(명시적 형변환)
		int v1 = (int)5.3;
		long v2 = (long)10;
		float v3 = (float)5.8;
		double v4 = (double)16;
		
		System.out.println(v1);
		System.out.println(v2);
		System.out.println(v3);
		System.out.println(v4);
		System.out.println();
		
		// 캐스팅 방법 2
		long v5 = 10L;
		long v6 = 10l;
		float v7 = 5.8F;
		float v8 = 5.8f;
		
		System.out.println(v5);
		System.out.println(v6);
		System.out.println(v7);
		System.out.println(v8);
	}

}
