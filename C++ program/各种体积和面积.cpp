#include<iostream> 
using namespace std;
float v;
int main()
{const float PI=3.1415926;
 float r,h,s,v1,v2,v3;
 cout<<v;
 cout<<"请输入半径：";
 cin>>r;
 cout<<"请输入高：";
 cin>>h;
  v1=PI*r*r *h;
  v2=PI*r*r*h/3;
  v3=PI*r*r*r*4/3;
  s=2*PI*r*h+PI*r*r*2;
  cout<<"圆柱的体积="<<v1<<endl;
  cout<<"圆柱的表面积="<<s<<endl;
  cout<<"球的体积=" <<v3<<endl;
  cout<<"圆锥的体积="<<v2<<endl;   
	    return 0;
}
