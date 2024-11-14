#include <stdio.h>

int main(void) {
    unsigned int a = 29;
    unsigned int b = 48;
    int c = 0;

    c = a & b; // bitwise AND
    printf("%d & %d = %d\n", a, b, c);

    c = a | b; // bitwise inclusive OR
    printf("%d | %d = %d\n", a, b, c);

    c = a ^ b; // bitwise exclusive OR (XOR)
    printf("%d ^ %d = %d\n", a, b, c);

    c = ~a; // bitwise NOT (one's complement)
    printf("~%d = %d\n", a, c);

    c = a << 2; // logical left shift
    printf("%d << 2 = %d\n", a, c); // Corrected to use 'c' instead of 'b'

    c = a >> 2; // logical right shift
    printf("%d >> 2 = %d\n", a, c);

    return 0;
}
