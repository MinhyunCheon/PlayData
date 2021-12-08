import test.thread.Prt;
import test.thread.PrtThread;

public class ThreadMain {
	public static void main(String[] args) {
		Prt monitor = new Prt();
		
		PrtThread runn01 = new PrtThread('A', monitor);
		Thread t01 = new Thread(runn01);
		t01.start();
		
		PrtThread runn02 = new PrtThread('B', monitor);
		Thread t02 = new Thread(runn02);
		t02.start();
	}
}
