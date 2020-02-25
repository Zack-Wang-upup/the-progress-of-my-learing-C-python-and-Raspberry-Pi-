#include<iostream>
using namespace std;
int main()
{int i,a,b,s,min;
 cout<<"请输入a=";
 cin>>a;
 cout<<"请输入b=" ;
 cin>>b; 
 min=a;
 if(min>b) 
 min=b;
 i=min; 
  while((a%i!=0)||(b%i!=0))
  i--;
  cout<<"最大公约数="<<i<<endl;
  return 0; 
 } 
