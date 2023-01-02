#include<bits/stdc++.h>

int batata(int *v, int x)
{
	int sub = 0;
	int cont = 0;
	int y = 0;
	do {
		for(int i=0; i<x;i++)
		{
			scanf("%d",&v[i]);
			if (v[i]==0)
			{
				return 0;
			}
		}
		for(int i=0; i<x-1;i++)
		{
			sub=v[i]-v[i+1];
			if((sub>2)||(sub<-2))
			{
				printf("No\n");
				break;
			}
			else
			{
				cont=cont+1;
				if(cont==x-1)
				{
					printf("Yes\n");
					break;
				}
			}
		}
			cont=0;
			sub=0;
			free(v);
			int *v =(int *)malloc(x*sizeof(int));
	}while(y==0);
}

using namespace std;

int main ()
{
	int x = 0;
	while(cin >> x, x!=0)
	{
		int x_0 = 0, old_x = -1, c=0;
		bool err = false;
		while(cin >> x_0, x_0!=0){
			c++;
			//cout << "X Atual:" <<  x_0 << endl;
			if(c > 1)
			{
				cout << x_0 << "|" << old_x << "   " << x_0 - old_x << endl;
				if(abs(x_0 - old_x) > 3){
					err = true;
				}
			}
			if(c == x){
				if(!err){
					cout << "Yes" << endl;
				}
				else{
					cout << "No" << endl;
				}
				c=0;
			}
			
			old_x = x_0;
		}	
	}
	return 0;
}