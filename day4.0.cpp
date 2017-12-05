#include <string>
#include <iterator>
#include <iostream>
#include <sstream>
#include <set>
#include <vector>
using namespace std;

int main()
{
	int res = 0;
	string line, word;
	while(getline(cin, line), !line.empty())
	{
		stringstream s(line);
		vector<string> words(istream_iterator<string>(s), {});
		if(set<string>(words.begin(), words.end()).size() == words.size())
			res++;
	}
	printf("%d\n", res);
}
