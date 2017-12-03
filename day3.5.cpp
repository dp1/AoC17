#include <cstdio>

int mat[5000][5000];

int main()
{
	// d is the current direction, with 0 meaning right and going counterclockwise
	int x = 2500, y = 2500, d = 0, n = 1;
	while(n <= 312051)
	{
		// write; move; rotate if possible
		mat[x][y] = n;
		
		x += (d & 1) * (d - 2);
		y += (~d & 1) * (1 - d);
		
		n = 0;
		for(int i = -1; i <= 1; i++)
			for(int j = -1; j <= 1; j++)
				n += mat[x+i][y+j];
		
		if(d == 0 && mat[x-1][y] == 0) d++;
		else if(d == 1 && mat[x][y-1] == 0) d++;
		else if(d == 2 && mat[x+1][y] == 0) d++;
		else if(d == 3 && mat[x][y+1] == 0) d = 0;
	}
	printf("%d\n", n);
}
