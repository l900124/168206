#include <iostream>
int main()
{
    using namespace std;
    char *man[]={"A","B","C","D"};
    for(int n=0;n<4;n++)                                                     //n既为循环控制变量，也表示第N个人
       {if ((n!=0)+(n==2)+(n==3)+(n!=2)==3)                     //如果4句话有3句为假，则是该人说真话
           cout<<"说真话的人是："<<man[n]<<endl;}
    return 0;
}
