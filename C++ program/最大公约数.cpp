#include<iostream>
using namespace std;
int main()
{int i,a,b,s,min;
 cout<<"������a=";
 cin>>a;
 cout<<"������b=" ;
 cin>>b; 
 min=a;
 if(min>b) 
 min=b;
 i=min; 
  while((a%i!=0)||(b%i!=0))
  i--;
  cout<<"���Լ��="<<i<<endl;
  return 0; 
 } 
