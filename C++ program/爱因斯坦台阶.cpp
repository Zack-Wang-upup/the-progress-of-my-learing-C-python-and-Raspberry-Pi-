#include <iostream>
using namespace std;
int main()
{int r;
 for(r=11;r<=1000;r++) 
 {if((r%2==1)&&(r%3==2)&&(r%4==3)&&(r%5==4)&&(r%6==5)&&(r%7==0))
 cout<<r<<endl;
}
 return 0;
 } 
