package test.thread;

public class PrtThread implements Runnable {
	private char c;
	private Prt monitor;
	
	public PrtThread() {
		
	}

	public PrtThread(char c, Prt monitor) {
		this.c = c;
		this.monitor = monitor;
	}
	
	public void run() {
		// 스레드가 공유하는 변수를 동기화하여 실행 순서 보장
		synchronized (monitor) {
			for(int i = 0; i < 10; i++) {
				monitor.printChar(c);
				System.out.println();
			}
		}
	}
}
