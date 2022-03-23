package util;

import java.util.LinkedList;
import java.util.List;

public class SingleParticle {
	List<Path> S = new LinkedList<Path>();
	int n;
	
	public SingleParticle(List<Path> S, int n) {
		this.S = S;
		this.n = n;
	}
}
