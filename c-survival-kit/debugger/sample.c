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
  2 [arr] = 6;
  printf("%i", 2 [arr]);
}

void test6() {
  int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int arr2[3] = {69, 69, 69};
  for (int i = 0; i < 70; i++) {
    printf("%i\n", arr2[i]);
  }
}

void test7() {
  int i, j, num;
  num = 12;
  for (i = 1; i < num; i++) {
    j = j * i;
  }
  printf("%i \n", j);
}

int main() {
  // test1();
  // test2();
  // test3();
  // test4();
  // test5();
  // test6();
  // test7();

  return 0;
}
