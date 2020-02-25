#include <iostream>
using namespace std;
int main()
{int r,i,j;
 for(i=0;i<=9;i++)
    {for(j=0;j<=9;j++)
        {r=1*10000+4*1000+7*100+i*10+j;
        if((r%57==0)||(r%67==0))
        cout<<r<<endl;
		}
    }
 system("pause"); 
 return 0;
}
