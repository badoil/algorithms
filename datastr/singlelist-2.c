#include <stdio.h>
#include <string.h>
#include <malloc.h>

typedef struct NODE {

    char szData[64];
    
    struct NODE* next;

} NODE;

NODE* g_pHead = NULL;

void PrintList(void) {
    
    NODE* pHead = g_pHead;
    while(pHead != NULL) {
        printf("[%p]: %s, next[%p]", pHead, pHead->szData, pHead->next);
        pHead = pHead->next;
    }

}

int InsertNode(int pszData)
{
    NODE* pNode = (NODE*)malloc(sizeof(NODE));
    strcpy_s(pNode->szData, sizeof(pNode->szData) , pszData);

    if (g_pHead == NULL) {
        g_pHead = pNode;
    } else {
        // pNode->next = g_pHead->next;     이거는 내가 했는데 틀린듯??
        // g_pHead->next = pNode;

        pNode->next = g_pHead;
        g_pHead = pNode;
    }
    
    return 1;
}

int main() {

    // 테스트
    InsertNode("test01");
    PrintList();

    InsertNode("test02");
    PrintList();

    InsertNode("test03");
    PrintList();

    return 0;
}



// 연결리스트 코딩순서
/*
1. 전체리스트 출력함수 작성
2. 새 노 드추가 함수 작성
3. 전체리스트 삭제함수 작성
4. 각 함수를 작성할때마다 main함수에서
    테스트 코드를 실행한다
*/