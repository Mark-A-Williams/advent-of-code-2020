#include <stdio.h>

int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    else if (n > 1) {
        return n * factorial(n - 1);
    }
}

char* foo(int n) {
    if (n == 1) {
        return "one";
    }
    else if (n == 2) {
        return "two";
    }
    else {
        return "that's a huge number";
    }
}

int main() {
    int y = -1;
    char* numberThing = foo(1);
    printf("%d factorial = %d\n", y, factorial(y));
    printf(numberThing);
    return 0;
}