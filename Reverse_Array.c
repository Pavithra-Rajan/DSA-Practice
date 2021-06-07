//Write a program to reverse an array or string
#include<stdio.h>
void reverse(int arr[],int n)
{
	int i,temp;
	int end=n-1;
	for(i=0;i<n/2;++i)
	{
		temp=arr[end];
		arr[end]=arr[i];
		arr[i]=temp;
		end--;
	}
	for(i=0;i<n;++i)
		printf("%d ",arr[i]);
}
int main()
{
 int arr[]={1,2,3,4,5,6};
 reverse(arr,6);
 return 0;
}
