#include<math.h>

int reverse(int x){
    long int rev=0;
    int flag=0;
    long int temp;
    if (x<0)
    {
        flag=1;
        temp=(long)x*(-1);
    }
    else
        temp=x;
    while(temp!=0)
    {
        if ((rev*10)>pow(2,31)-1)
        {   
           rev=0;
           break;
        }
        else 
        {
            rev*=10;
            rev=rev+temp%10;
            temp/=10;
            
        } 
    }
    
    if (rev>=pow(-2,31) && rev<=pow(2,31)-1)
      return (flag==1?rev*(-1):rev);
    return 0;
}