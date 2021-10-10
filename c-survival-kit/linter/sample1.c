#include <stdio.h>

void printArr(int *arr, int size) {
  for (int i = 0; i < size; i++) {
    printf("%i ", arr[i]);
  }

  printf("\n");
}

void bubbleSort(int *arr, int size) {
  int tmp;
  for (int i = 0; i < size - 1; i++) {
    for (int j = 0; j < size - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        tmp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = arr[j];
      }
    }
  }
}

int main() {
  int arr[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  int size = 10;
  printArr(arr, size);
  bubbleSort(arr, size);
  printArr(arr, size);
}
