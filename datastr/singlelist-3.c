#include <stdio.h>
#include <string.h>
#include <malloc.h>

typedef struct NODE 
{

    char szData[64];
    
    struct NODE* next;

} NODE;

NODE* g_head = { 0 };

int IsEmpty() 
{
    if (g_head->next == NULL) {
        return 1;
    }
    return 0;
}

int InsertAtHead(char* pszData)
{
    NODE* pNode = (NODE*)malloc(sizeof(NODE));
    memset(pNode, 0, sizeof(NODE));
    strcpy_s(pNode->szData, sizeof(pNode->szData) , pszData);
    if (IsEmpty)
    {
        g_head = pNode;
    } else
    {
        pNode->next = g_head->next;
        g_head->next = pNode;    
    }

    return 1;

}

int InsertAtTail(char* pszData)
{
    NODE* pTmp = &g_head;
    while(pTmp->next != NULL){
        pTmp = pTmp->next;
    }

    NODE* pNode = (NODE*)malloc(sizeof(NODE));
    memset(pNode, 0, sizeof(NODE));
    strcpy_s(pNode->szData, sizeof(pNode->szData) , pszData);

    pTmp->next = pNode;
}

void PrintList(void) 
{
    
    NODE* pHead = g_head;
    while(pHead != NULL) {
        printf("[%p]: %s, next[%p]", pHead, pHead->szData, pHead->next);
        pHead = pHead->next;
    }

}

NODE* FindData(char* pszData)
{
    NODE* pPrev = g_head;
    NODE* pCur = g_head->next;

    while (pCur != NULL) {
        if (strcmp(pCur->szData, pszData)==0){
            return pPrev;
        }
        pPrev = pPrev->next;
        pCur = pCur->next;
    }
    return 0;
}

int DeleteData(char* pszData)
{
    NODE* pPrev = FindData(pszData);
    if (pPrev != 0) {
        NODE* deleteNode = pPrev->next;
        pPrev->next = deleteNode->next;

        free(deleteNode);    
        return 1;
    }
    return 0;
}

// 이것은 g_pHead가 아니라 더미노드 이용해서 연결리스트 만듬  
// 나머지는 singlelist-2 와 비슷한데
// 위의 것들은 다름

// 