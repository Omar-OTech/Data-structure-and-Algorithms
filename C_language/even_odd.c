#include <stdio.h>
/*
The following example writes even integers to one file
and odd integers to another file
*/

int main() {
    FILE *even, *odds;
    int n = 100;
    size_t k = 0;

    even = fopen("even.txt", "w");
    odds = fopen("odd.txt", "w");

    // Check if files were opened successfully
    if (even == NULL || odds == NULL) {
        perror("Error opening file");
        return 1;
    }

    for (k = 1; k < n + 1; k++) {
        k % 2 == 0 ? fprintf(even, "\t%5d\n", k)
               : fprintf(odds, "\t%5d\n", k);
    }
    
    fclose(even);
    fclose(odds);

    return 0;
}
