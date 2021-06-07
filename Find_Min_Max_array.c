//Maximum and minimum of an array using minimum number of comparisons
#include<stdio.h>
struct find
{
	int min;
	int max;
};
struct find minmax(int arr[],int size)
{
	struct find ptr;
	int i;
	ptr.max=arr[0];
	ptr.min=arr[0];
	
	for(i=1;i<size;++i)
	{
		if(arr[i]>ptr.max)
			ptr.max=arr[i];
		if(arr[i]<ptr.min)
			ptr.min=arr[i];
			
	}
	return ptr;
	
}
int main()
{
	int arr[]={1,2,7,6,21,34,12};
	int size=7;
	struct find find_ptr=minmax(arr,size);
	printf("%d %d",find_ptr.min,find_ptr.max);
	return 0;
}
