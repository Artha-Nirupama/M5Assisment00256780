#include <stdio.h>

int calculate_Sum(int *arr, int size);

int main() {
    int numbers[10] = {1,2,3,4,5,6,7,8,9,10};  
    int size = 10;
    
    int sum = calculate_Sum(numbers, size);
    printf("The sum of the array elements is: %d\n", sum);
    
    return 0;
}

int calculate_Sum(int *arr, int size) {
    int sum = 0;
    int *pArr = arr;  
    
    for (int i = 0; i < size; i++) {
        sum += *(pArr + i);  
    }
    
    return sum;
}
