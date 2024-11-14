#include <limits.h>
#include <stdio.h>

/*
Mask refers to the process of extracting the desired bits from (or transforming the desired bits in)
Masking is used in many different ways:
1- To decide the bit pattern of an int variable.
2- To copy a portion of a given bit pattern to a new variable while the remainder of the new var is filled with 0s using bitwise AND.
3- To copy a portion of a given bit pattern to a new variable while the remainder of the original bit pattern is inverted within the new var using bitwise OR.
*/

void bit_pattern(int n) {
    int i, x, word;
    unsigned mask = 1;
    word = CHAR_BIT * sizeof(int);
    mask = mask << (word - 1); // Shift mask to the left-most position

    for (i = 1; i <= word; i++) {
        x = (n & mask) ? 1 : 0;
        printf("%d", x);
        mask >>= 1;
    }
    printf("\n");
}

int main(void) {
    int test_number = 29;
    bit_pattern(test_number);

    return 0;
}
