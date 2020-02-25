#include<iostream>
using namespace std;
int main()
{int s=0,i,j,k; 
 for(i=1;i<=1000;i++)
 {  s=0; 
    for(j=1;j<=i-1;j++)
       if(i%j==0)  
	      s=s+j;
    if(s==i) 
       {
	   cout<<i<<"=0";
    for(j=1;j<=i-1;j++)
    if(i%j==0)
	cout<<"+"<<j;
	cout<<" ";}  
	
  } 
  return 0;    
 }
