import java.math.*;
import java.util.*;
/**
 * The skiing class calculates the optimal cost.
 * go through from minimum value in list to
 * (maximum value - K) in list
 */
public class skiing {
	
	public static int hill_cost(int[] hills, int K) {
		int cost = Integer.MAX_VALUE; int sum;
		int len = hills.length;
		if (len == 1) {
			return 0;
		}
		Arrays.sort(hills);
		int min = hills[0]; int max = hills[len-1];
		for(int i = min; i <= max - K; i++) {
			int start = i; int end = i + K;
			sum = addAll(hills, start, end);
			cost = Math.min(cost, sum);
		}
		return cost;
	}

	public static int addAll(int [] hills, int start, int end) {
		int sum = 0;
		for (int i = 0; i < hills.length; i++) {
			if (hills[i] < start) {
				sum += Math.pow(start - hills[i], 2);
			} else if (hills[i] > end) {
				sum += Math.pow(hills[i] - end, 2);
			}
		}
		return sum;
	}
	
	public static void main(String[] args) {
		int [] hills1 = {1, 4, 20, 21, 24};
		System.out.println(hill_cost(hills1, 0));
	}
}
