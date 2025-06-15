#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	int sum = 0;
	char arr[n];
	scanf("%s", arr);

	
	for (int i = 0; i < n; i++)
	{
		sum += arr[i] - '0';
	}
	printf("%d", sum);
	return 0;
}