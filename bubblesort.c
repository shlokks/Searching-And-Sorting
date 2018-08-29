#include<stdio.h>
void swap(int *a,int *b);
int main()

{
	int arr[100],n,i,j ,temp;
	printf("Enter the number of elements in the array :");
	scanf("%d",&n);
	printf("\nEnter the elements of the array :");
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	
	printf("\nThe unsorted array is :");
	for(i=0;i<n;i++)
	{
		printf("%d ",arr[i]);
	}
	
	for(j=0;j<n;j++)
	{
		for(i=0;i<n-1;i++)
		{
			if (arr[i]>arr[1+i])
			{
				swap(&arr[i],&arr[i+1]);
				
			}
		
		}
	}
	
	printf("\nSorted array is :");
	for(i=0;i<n;i++)
	{
		printf("%d ",arr[i]);
	}
}

void swap(int *a,int *b)
{
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
}
