#include <cstdio>
#include <vector>
#include <utility>
using namespace std;

/*
$ time python day13.5.py
3849742

real    0m1,615s
user    0m1,562s
sys     0m0,046s

$ time ./day13.5
3849742

real    0m0,049s
user    0m0,031s
sys     0m0,015s
*/

vector<pair<int, int> > data;

bool firewall(int off)
{
	for(auto e : data)
		if((e.first + off) % (2 * e.second - 2) == 0)
			return true;
	return false;
}

int main()
{
	FILE *fin = fopen("day13.txt", "r");
	int a, b;
	while(fscanf(fin, "%d: %d", &a, &b) != EOF)
		data.push_back({a, b});
	
	int off = 0;
	while(firewall(off)) off++;
	printf("%d\n", off);
}
