#include <stdio.h>

int main() {
    int n, m, i, j, temp, start, end;
    scanf("%d %d", &n, &m);

    int baskets[n];

    for (i = 0; i < n; i++) 
    {
        baskets[i] = i + 1; 
    }

    for (i = 0; i < m; i++) 
    {
        scanf("%d %d", &start, &end); 
        for (j = 0; j < (end - start + 1) / 2; j++) 
        {
            temp = baskets[start + j - 1]; 
            baskets[start + j - 1] = baskets[end - j - 1];
            baskets[end - j - 1] = temp;
        }
    }
    for (i = 0; i < n; i++) 
    {
        printf("%d ", baskets[i]);
    }
    return 0;
}
