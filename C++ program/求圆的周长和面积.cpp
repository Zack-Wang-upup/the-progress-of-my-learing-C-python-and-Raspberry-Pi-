#include<iostream>
//为变量开辟空间 
using namespace std;
//主程序 
int main()
//常量 
{const float PI=3.1415926;
//变量 
 float r,length=0,area=0;
 cout<<"请输入半径:";
//输入圆的的半径 
 cin>>r;
 length=2*PI*r;
//输出圆的周长 
 cout<<"Length="<<length<<endl;
 area=PI*r*r;
 cout<<"Area="<<area<<endl;
 return 0; 
 } 
