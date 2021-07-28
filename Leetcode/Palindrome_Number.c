

bool isPalindrome(int x){
    if(x<0)
        return 0;
    else
    {
        long int rev=0;
        int copy=x;
        while(copy!=0)
        {
            if ((rev*10)>pow(2,31)-1)
            {   
               rev=0;
               break;
            }
            else 
            {
                rev*=10;
                rev=rev+copy%10;
                copy/=10;

            } 
            
        }
        if(rev==x)
            return 1;
        return 0;
    }
}