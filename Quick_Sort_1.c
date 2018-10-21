#include<stdio.h>

void swap();
int partition();
void qsort();

int main()
{
	int a[100];
	int n;
	
	printf("Enter the size of array : \n");
	scanf("%d",&n);
	
	int l , h, i, j;
	
	l = 0;
	h = n-1;
	
	printf("\nEnter the elements of the array  : \n\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	
	qsort(a, l, h);
	
	printf("\n\nThe sorted array is : \n\n");
	for(i=0;i<n;i++)
	{
		printf("%d ",a[i]);
	}
	
	return 0;
}

void qsort(int *a, int l, int h)
 {
 	int j;
 	
 	if(l<h)
 	{
 		j = partition(a, l, h);
 		
 		qsort(a, l, j - 1);
 		
 		qsort(a, j + 1, h);
	 }
 }
 
 int partition(int *a, int l,int h)
{
	int pivot;
	pivot = a[l];
	int i = l;
	int j = h + 1;
	
	while(i<j)
	{
		do
		{
			i++;
		}
		while(a[i]<=pivot);
		
		do
		{
			j--;
		}
		while(a[j]>pivot);
		
		if(i<j)
		{
			swap(&a[i],&a[j]);
		}
	}
	
	swap(&a[l],&a[j]);
	
	return j;
}

void swap(int *a, int *b)
{
	int c =*a;
	*a = *b;
	*b = c;
}
