#include <stdio.h>

int print(int i) {
    printf("Print function %d\n", i);
    return 1;
}

int main(void) {
    int a = 20;

    // `print(a)` is not called since `a != 20` is false, so the short-circuit skips the call to `print(a)`
    if (a != 20 && print(a)) {
        printf("I won't be printed!\n");
    }

    // `print(a)` is called since `a == 20` is true, so the second condition is evaluated
    if (a == 20 && print(a)) {
        printf("I will be printed!\n");
    }

    return 0;
}
