#include <stdio.h>

int main()
{
	int i, n;
	float sum=0;
	printf("Enter the size of your array: ");
	scanf("%d",&n);
	float arr[n];
	printf("Enter the %d values of the array\n", n);
	for(i=0;i<n;i++)
	    scanf("%f",&arr[i]);
	for(i=0;i<n;i++)
	    sum+=arr[i];
	 printf("The average of the values of the array is %.2f", sum/n);
	 return 0;
}