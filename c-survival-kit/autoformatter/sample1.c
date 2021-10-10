// This file contains declaration of a stack type and functions related to it

#include <stdio.h>
#include <stdlib.h>


typedef struct Stack{
    int head;
    int size;
    int b;
    int c;
    int num_elements;
    int* elements;
}stack;



// print stack (for debugging purposes)
void print_stack(stack* s){
  for (int i = s -> num_elements - 1; i >= 0; i--){
    printf("%d\n", s -> elements[i]);
  }
}


// add element to a stack. Returns -1 if stack is full and 0 if it worked fine
int push_stack(stack* s, int element){
  if (s -> head+1 < s -> size){
    s -> head ++;
    s -> num_elements ++;
    s -> elements[s -> head] = element;
    return 0;
  }
  else{
    return -1;
  }
}


int main(){
    printf("hello");
}
