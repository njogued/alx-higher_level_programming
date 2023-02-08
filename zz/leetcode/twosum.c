#include <stdio.h>
#include <stdlib.h>

int *twoSum(int* nums, int numsSize, int target, int *returnSize)
{
	int index = 0, index1 = 0, ind1 = 0, ind2 = 0;
	int *new_array = malloc(sizeof(returnSize));
	*(new_array) = 0;
	*(new_array + 1) = 0;
	printf("Target : %d\nExpected indices: 1, 3\n", target);
	for(index = 0; index < numsSize; index++)
	{
		printf("First loop index: %d\n", index);
		for(index1 = 0; index1 < numsSize; index1++)
		{
			printf("Second loop index: %d\n", index1);
			if(nums[index] + nums[index1] == target)
			{
				ind1 = index;
				ind2 = index1;
				printf("ind1: %d\nind2: %d\n", ind1, ind2);
				index1 = index = numsSize;

			}
		}
	}
	*(new_array) = ind1;
	*(new_array + 1) = ind2;
	return (new_array);
}
int main()
{
	int array[] = {3, 5, 2, 69, 4};
	int *indices = twoSum(array, 5, 74, array);
	printf("[");
	for(int i = 0; i < 2; i++)
	{
		printf(" %d ", *(indices + i));
	}
	printf("]\n");
	return 0;
}
