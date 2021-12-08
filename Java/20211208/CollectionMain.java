import java.util.ArrayList;
import java.util.List;

public class CollectionMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List list = new ArrayList();	// 제네릭스가 없어도 선언 가능
		// List는 object를 매개변수로 요구하지만 상수 또는 기본 데이터도 저장이 가능하다.
		// Integer로 자동 박싱(업캐스팅 x)후 저장
		list.add(1);
		list.add(true);
		list.add("a");
	}

}
