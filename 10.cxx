#include <stdio.h>

int main()
{
	int i, n, sum=0;
	printf("Enter the size of your array: ");
	scanf("%d",&n);
	int arr[n];
	printf("Enter the %d values of the array\n", n);
	for(i=0;i<n;i++)
	    scanf("%d",&arr[i]);
	for(i=0;i<n;i++)
	    sum+=arr[i];
	 printf("The sum of the values of the array is %d", sum);
	 return 0;
}