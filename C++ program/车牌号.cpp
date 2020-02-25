#include <iostream>
using namespace std;
int main()
{int r,i,j,f;
 for(i=0;i<=9;i++)
    {for(j=0;j<=9;j++)
        {r=i*1000+i*100+j*10+j;
        for(f=32;f<=99;f++)
            if(f*f==r) 
			cout<<r<<" "<<f<<endl; 
		} 
	}
return 0;
 } 
