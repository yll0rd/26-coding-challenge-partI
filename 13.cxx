#include<stdio.h>

int main()
{
	int i, n;
	printf("Enter the size of your array: ");
	scanf("%d",&n);
	int arr[n];
	printf("Enter the %d values of the array\n", n);
	for(i=0;i<n;i++)
	    scanf("%d",&arr[i]);
	int great = arr[0];
	for(i=1;i<n;i++)
	    if(great<arr[i])
	        great=arr[i];
	printf("The greatest number of this array is %d", great);
	return 0;
}