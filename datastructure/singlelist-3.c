#include <stdio.h>
#include <string.h>
#include <malloc.h>

typedef struct NODE 
{

    char szData[64];
    
    struct NODE* next;

} NODE;

NODE g_head = { 0 };

int IsEmpty() 
{
    if (g_head.next == NULL) {
        return 1;
    }
    return 0;
}

int InsertAtHead(char* pszData)
{
    NODE* pNode = (NODE*)malloc(sizeof(NODE));
    memset(pNode, 0, sizeof(NODE));
    strcpy_s(pNode->szData, sizeof(pNode->szData) , pszData);
    if (IsEmpty())
    {
        g_head.next = pNode;
    } else
    {
        pNode->next = g_head.next;
        g_head.next = pNode;    
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
    
    NODE* pHead = &g_head;
    while(pHead != NULL) {
        printf("[%p]: %s, next[%p]", pHead, pHead->szData, pHead->next);
        pHead = pHead->next;
    }

}

NODE* FindData(char* pszData)
{
    NODE* pPrev = &g_head;
    NODE* pCur = g_head.next;

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

void ReleaseData(void) {
    NODE* pTmp = g_head.next;
    while(pTmp != NULL) {
        NODE* pDelete = pTmp;
        pTmp = pTmp->next;
        
        printf("Delete: [%p] %s\n", pDelete, pDelete->szData);
        free(pDelete);
    }
    g_head.next = 0;      // g_pHead->next가 메모리 해제 되었기 때문에 이것을 안해주면 쓰레기 값을 가리키게됨, 후에 InsertNode하면 삽입된 노드가 이 쓰레기 노드에 접근하는데 이때 에러 발생
    
}

void PushData(char* pszData) 
{
    InsertAtHead(pszData);
}

int PopData(NODE* pPopNode)
{
    NODE* sp = g_head.next;
    if (sp == NULL) return 0;

    memcpy(pPopNode, sp, sizeof(NODE));

    g_head.next = sp->next;
    free(sp);
    return 0;
}

void main() {
    // stack 테스트

    PushData("test01");
    PushData("test02");
    PushData("test03");

    NODE popNode = { 0 };
    PopData(&popNode);
    printf("pop data: %s", popNode.szData);
    PopData(&popNode);
    printf("pop data: %s", popNode.szData);
    PopData(&popNode);
    printf("pop data: %s", popNode.szData);

    ReleaseData();
    return 0;
}


// 이것은 g_pHead가 아니라 더미노드 이용해서 연결리스트 만듬  
// 나머지는 singlelist-2 와 비슷한데
// 위의 것들은 다름

// 