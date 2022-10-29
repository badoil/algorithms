#include <stdio.h>


typedef struct NODE {
    
    int a;

    struct NODE* next;
} NODE;

int main() {

    NODE list[3] = { 0 };

    list[0].next = &list[1];
    list[1].next = &list[2];
    list[2].next = NULL;

    list[0].a = 100;
    list[1].a = 200;
    list[2].a = 300;

    NODE* pHead = &list[0];
    while (pHead != NULL)
    {
        printf("%p: %d\n", pHead, pHead->a);
        pHead = pHead->next;
    }
    

    return 0;
}