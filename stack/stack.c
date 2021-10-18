#include <stdio.h>
#include <stdlib.h>
// our stack code will be here
//
//   item1
//   item2
//   item3
//
// pop(stack_name)
//  go to the head
//  remove an element from head
//  update head to be the next element
//  return the value
//
//  item1[val,next]
//             |
//            \/
//             item2[val, next]
// push(item, stack_name)
/*

arr[index] = (*(arr + index))


address,
value,



*/

typedef struct Element {
  int val;
  struct Element *next;

} element;

// stack *s
//        s->name
//  stack s
//        s.name

typedef struct Stack {
  element *head;
  int size;

} stack;

void printStack(stack *s) {
  element *current = s->head;
  while (current != NULL) {
    printf("%i\n", current->val);
    current = current->next;
  }
}

// void* malloc(bytes) - amount of bytes so allocate in memory

stack *createStack() {
  // typecasting
  // malloc - what it does

  stack *s = (stack *)(malloc(sizeof(stack)));

  s->size = 0;
  s->head = NULL;

  return s;
}

/*


  head-> 3


  [1,1,1,1,1,1,"1,1,1,1,1"]
               |
               pointer

               int a

 */

int pop(stack *s) {
  element *e = s->head;

  int val = e->val;

  s->head = e->next;

  free(e);

  return val;
}

/*

     element - val, next
                     |
            [whatever head is pointing to]

              stack head -> e2 \/
                            e-\/
                          element


 */

void push(int val, stack *s) {
  element *e = (element *)malloc(sizeof(element));

  e->val = val;
  e->next = s->head;

  s->head = e;
  s->size++;
}

int main() {
  stack *s = createStack();
  int num;
  for (int i = 0; i < 1000000; i++) {
    push(i, s);
  }

  for (int i = 0; i < 1000000; i++) {
    pop(s);
  }

  for (int i = 0; i < 1000000; i++) {
    push(i, s);
  }

  for (int i = 0; i < 1000000; i++) {
    pop(s);
  }

  free(s);
  return 0;
}
