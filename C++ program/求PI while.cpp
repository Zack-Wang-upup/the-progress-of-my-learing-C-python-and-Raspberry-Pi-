#include<iostream>
using namespace std;
int main()
{float s=0;
 int i,j=1;
 while(1.0/i>0.1)
 {s=s+1.0/i*j;
 j=-j;
 i++;
 }
 cout<<"PI="<<s*4;
 return 0;
}
