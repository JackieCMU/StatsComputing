import static org.junit.Assert.*;
import org.junit.Test;

public class skiingTest {
	
	@Test
	public void testEqual() {
		skiing tester = new skiing();
		
		int [] hills1 = {1, 4, 20, 21, 24};
		assertTrue(18 == tester.hill_cost(hills1, 17));
		assertTrue(5 == tester.hill_cost(hills1, 20));
		assertTrue(0 == tester.hill_cost(hills1, 23));
		assertTrue(454 == tester.hill_cost(hills1, 0));
		
		int [] hills2 = {1};
		assertTrue(0 == tester.hill_cost(hills2, 9));
	}

}
