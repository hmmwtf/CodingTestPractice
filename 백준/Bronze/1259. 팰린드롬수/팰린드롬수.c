#include <stdio.h>
#include <string.h>

int main() {
	int i, j, result;
	char arr[100000];

	//처음 리스트의 인덱스 값이 0이 되면 안되므로 arr[0] != '0'를 추가했습니다.
	//원래는 while(1) or while(true)를 하고 안에 if(arr[0] == 1)을 하려고 했지만 이게 더 코드를 줄일 수 있었습니다. 
	while (scanf("%s", arr) && arr[0] != '0') {
		result = 1;
		j = strlen(arr);

		for (i = 0; i < j / 2; i++) {
			if (arr[i] != arr[j - 1 - i]) {
				result = 0;
				break;
			}
		}

		if (result == 1) {
			printf("yes\n");
		}
		else if (result == 0) {
			printf("no\n");
		}
	}

	return 0;
}