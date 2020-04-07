#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char x[100000];
    scanf("%s",&x);
    int a[10],i,l;
    for(i=0;i<10;i++)
    {
        a[i]=0;
    }
    l=strlen(x);
    for(i=0;i<l;i++)
    {   int d=x[i]-'0';
        if (d>=0&&d<=9)
        {
            a[d]+=1;
        }
    }
    for(i=0;i<10;i++)
    {
        printf("%d ",a[i]);
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
