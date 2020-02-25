#include <iostream>
using namespace std;
int main()
{int t,i,j,k,a[101]={0},sum=0; 
 for(i=1;i<=100;i++)
 {  k=0; sum=0;
  for(j=2;j<=i;j++)
    if(i%j==0) //是否是整数   
     a[++k]=i/j; 
  for(t=1;t<=k;t++)
   sum=sum+a[t];
  if(sum==i)
 { cout<<i<<"=0"; 
  for(t=1;t<=k;t++)
  cout<<"+"<<a[t];
  cout<<endl;
 }
 
}    
 return 0;
}    
