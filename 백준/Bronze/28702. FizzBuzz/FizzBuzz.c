#include <stdio.h>
#include <string.h>

int main() {
    char str[20];
    int arr[3], index = -1;

    for (int i = 0; i < 3; i++) {
        scanf("%s", str);
        int num = 0;
        int is_number = 1;
        for (int j = 0; str[j] != '\0'; j++) {
            if (str[j] < '0' || str[j] > '9') {
                is_number = 0;
                break;
            }
            num = num * 10 + (str[j] - '0');
        }

        if (is_number) {
            arr[i] = num;
            index = i;
        }
    }

    int next;
    if (index == 0) {
        next = arr[0] + 3;
    }
    else if (index == 1) {
        next = arr[1] + 2;
    }
    else if (index == 2) {
        next = arr[2] + 1;
    }
    else {
        printf("error\n");
        return 1;
    }

    if (next % 3 == 0 && next % 5 == 0) {
        printf("FizzBuzz\n");
    }
    else if (next % 3 == 0) {
        printf("Fizz\n");
    }
    else if (next % 5 == 0) {
        printf("Buzz\n");
    }
    else {
        printf("%d\n", next);
    }

    return 0;
}