#include<iostream>
//#include<iomanip>
using namespace std;
int main()
{int i,j;
double t,s;
for(i=1;i<=10;i++)
{t=1;
 for(j=1;j<=i;j++)
    t=t*j;
s=s+1/t;
}
//cout<<fixed<<setprecision(5)<<s<<endl;
cout<<s;
return 0;
 } 
