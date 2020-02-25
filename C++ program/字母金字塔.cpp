#include<iostream>
using namespace std;
int main()
{char p,i,j;
 cout<<"请输入一个大写字母=";
 cin>>p;
 for(i='A';i<=p;i++)
 {for(j='A'-64;j<=p-i;j++)
    cout<<' ';
  for(j='A';j<=i;j++)
    cout<<j;
  for(j=i-1;j>='A';j--) 
    cout<<j;
  cout<<endl;
	} 
	return 0;
}
