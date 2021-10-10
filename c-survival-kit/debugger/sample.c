#include <stdio.h>
#include <stdlib.h>

void test1() {
  int arr[10];

  for (int i = 0; i < 20; i++) {
    printf("%i ", arr[i]);
  }

  printf("\n");
}

void test2() {
  int arr[10];

  arr[11] = 0;

  printf("%i", arr[11]);
}

void test3() {
  int arr[10];

  arr[1000] = 0;

  printf("%i", arr[1000]);
}

void test4() {
  char *str = "blahblah";

  str[1] = 'f';
}

void test5() {
  int arr[3] = {1, 2, 3};

  printf("%i", 1 [arr]);
}

int main() {
  // test1();
  // test2();
  // test3();
  // test4();
  // test5();

  return 0;
}
