#include<iostream>
using namespace std;
int main()
{float g;
cout<<"请输入成绩(满分100)：";
cin>>g;
if(g>=80) 
  {if(g>=90)
     {if(g==100)
          cout<<"满分"; 
       else
          cout<<"优秀"; 
     }
   else
   cout<<"良好"; 
  }
else
           if(g>=60)
             {cout<<"及格";} 
		   else
			  cout<<"不及格"; 
		     
return 0;          
}
