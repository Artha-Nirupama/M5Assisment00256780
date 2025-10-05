#include <stdio.h>

int validateAndFindLargest(int A, int B, int C,char *largestVar);

int main() {
    int A, B, C;
    int result;
    char largestVar;

    char characters[]={'A','B','C'};
    int *vars[] = {&A, &B, &C}; 

    for (int i = 0; i < 3; i++)
    {
        printf("Enter variable %c for check: ",characters[i]);
        scanf("%d", vars[i]);
    }

    result = validateAndFindLargest(A, B, C, &largestVar);

    if (result == 0) {
        printf("Validation Error: One or more numbers exceed 100.\n");
    } else {
        printf("The largest number is: %d (Variable %c) \n", result,largestVar);
    }

    return 0;
}

int validateAndFindLargest(int A, int B, int C,char *largestVar) {

    if (A > 100 || B > 100 || C > 100) {
        return 0;  
    }

    if (A >= B && A >= C){
        *largestVar = 'A';
        return A;
    }
    else if (B >= A && B >= C){
        *largestVar = 'B';
        return B;
    }
    else{
        *largestVar = 'C';
        return C;
    }
}
