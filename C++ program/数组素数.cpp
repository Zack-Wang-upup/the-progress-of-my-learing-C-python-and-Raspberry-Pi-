#include <iostream>
using namespace std;
int main()
{int a[100]={0},j,i,k;
 for(int i=2;i<=100;i++)
     a[i]=i;
 for(i=2;i<=100;i++)
       {if(a[i]!=0)
            for(j=1;j<=100-i;j++)
                if(a[i+j]%a[i]==0)
                a[i+j]=0;
			}
 for(i=2;i<=100;i++)
	    if(a[i]!=0)
	        {k++;
            cout<<a[i]<<endl;
           
   } 
 cout<<"Ò»¹²ÓÐ="<<k<<endl; 
 return 0;

    
 } 
