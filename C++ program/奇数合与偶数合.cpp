#include<iostream>
using namespace std;
int main()
{int s1=0,s2=0,i;
 for(i=1;i<=100;i++)
 {if(i%2==0)
  s1=s1+i;
  else
  s2=s2+i;
 }
 cout<<"偶数合等于="<<s1<<endl;
 cout<<"奇数合等于="<<s2<<endl; 
 return 0;
 } 
