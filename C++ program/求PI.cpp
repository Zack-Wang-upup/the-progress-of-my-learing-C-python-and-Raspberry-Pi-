#include<iostream>
#include<iomanip>
using namespace std;
int main()
{double s=0;
 int j=1,i;
 for(i=1;i<=10000000000000;i++)
 {s=s+(1.0/i)*j;
  j=-j;
  i++;
 }
 cout<<"PI="<<fixed<<setprecision(4)<<s*4<<endl; 
 return 0;
 } 
