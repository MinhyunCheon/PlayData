package test.thread;

public class Prt {
	// 해당 메소드를 스레드로 호출하면 충돌 발생 synchronized를 통해 회피 가능 
	public void printChar(char c) {
		for(int i = 0; i < 10; i++) {
			System.out.print(c);
		}
	}
}
