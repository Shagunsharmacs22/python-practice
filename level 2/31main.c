#include <stdio.h>
int main() {
int a;
scanf("%d",&a);
 int c=0,d=0,e=0;
for (int i=1; i<a;i++)
{if (a%i==0 ) {
c=c+1;
break;}
}
for (int j=2;j<(a+2);j++)
{
  if ((a+2)%j==0) {
  d=d+1;
  break; }
}
for (int k=1;k<(a-2);k++)
{
  if ((a-2)%k==0) {
  e=e+1;
  break; }
}
if (c==1 &&  (d==1 || e==1))
{ printf("number is twin prime");}
else 
{ printf("number is not twin prime");}
 return 0;

}