package T210929;

public class TypeCasting_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 자동 형변환(업캐스팅, byte/short 자료형 데이터 입력)
		float v1 = 3;	// int -> float(업캐스팅)
		long v2 = 5;	// int -> long(업캐스팅)
		double v3 = 7;	// int -> double(업캐스팅)
		byte v4 = 9;	// (예외 : int -> byte)
		short v5 = 11;	// (예외 : int -> short)
		
		System.out.println(v1);
		System.out.println(v2);
		System.out.println(v3);
		System.out.println(v4);
		System.out.println(v5);
		System.out.println();
		
		// 다운 캐스팅 시에는 데이터 손실이 발생할 가능성 존재
		byte v6 = (byte)128;	// int -> byte(다운캐스팅)
		int v7 = (int)3.5;		// double -> int(다운캐스팅)
		float v8 = (float)7.5;	// double -> float(다운캐스팅)
		
		System.out.println(v6);
		System.out.println(v7);
		System.out.println(v8);
	}

}
