#include<iostream> 
#include<cmath>
using namespace std;
int main()
{float a,b,c,l,s;
 cout<<"请输入你想组成三角形的三个边："; 
 cin>>a>>b>>c;
 if((a+b>c)&&(a+c>b)&&(b+c>a))
 {cout<<"yes";
 l=(a+b+c)/2;
 s=sqrt(l*(l-a)*(l-b)*(l-c));
 cout<<"三角形面积为="<<s; 
 } 
 else
 cout<<"NO";
 return 0; 
}
