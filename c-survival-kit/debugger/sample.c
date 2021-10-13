#include <stdio.h>
#include <stdlib.h>

// arr[10] = *(arr + 10)

void test1() {
  // array the indexes: 0 - 9
  // we did not initialise the values
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

// 10[arr] == *(10 + arr)
// arr[10]
//  []  []   []   [] [] [] []
//  10       arr

void test5() {
  int arr[3] = {1, 2, 3};
  2 [arr] = 6;
  printf("%i", 2 [arr]);
}
//
void test6() {
  int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int arr2[3] = {69, 69, 69};
  int arr3[3] = {1, 2, 3};

  arr2[5] = 123;

  for (int i = 0; i < 70; i++) {
    printf("%i\n", arr3[i]);
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

// 140735989497936
// 140726747484528
// 140735993497932
int main() {
  int arr[1000000];

  for (int i = 0; i < 1000000; i++) {
    arr[i] = 0;
  }
  int *ptr = 0x7ffce75f2c70;
  printf("%p \n", arr);
  printf("%p \n", ptr);
  printf("%p \n", arr + 999999);
  printf("%i \n", *(arr + 999999));

  int val = ptr[0];
  printf("%i \n", val);

  return 0;
}
