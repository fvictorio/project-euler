#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;
typedef unsigned long long ui;
 
const ui MAX=100000000;
bool f[MAX];
bool z[MAX];
 
int main()
{
    double time=clock();

    for(ui i=2;i<MAX;i++) 
    {
    z[i]=1;
    f[i]=0;
    }

    for(ui i=2;i<MAX;i++)
    {
    if(z[i]==1)
       {
       ui q=2;
       for(ui j=q*i;q<=i && j<MAX;j+=i) 
          {
          z[j]=0;
          if(z[q]==1) f[j]=1;
          q++;
          }

       for(ui j=q*i;j<=MAX;j+=i) z[j]=0;  
       }
    }

    ui x=0;
    for(ui i=2;i<MAX;i++) {if(f[i]==1) x++;}

    cout<<x<<" in "<<clock()-time<<"ms"<<endl;
    system("Pause");
    return 0;
}
