#include <iostream>
using namespace std;
int jie(int a) 
{int i,k=1;
 for(i=1;i<=a;i++)
 k=k*i; 
 return k;
}
int main()
{int a,j,m=0;
cout<<"输入一个数";
 cin>>a;
 for(j=1;j<=a;j++)
 m=m+jie(j);
 cout<<m; 
  return 0;
}
