
int find_sqsum(int n)
{
    int sum=0;
    while(n!=0)
    {
        sum=(n%10)*(n%10)+sum;
        n=n/10;
    }
    return sum;
}
bool isHappy(int n){
    
    while(find_sqsum(n)!=1)
    {
        n=find_sqsum(n);
        if(n==4)
            return false;
        
    }
    return true;

}