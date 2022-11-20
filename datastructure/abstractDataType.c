#include <stdio.h>
#include <string.h>
#include <malloc.h>


typedef struct USERDATA
{
    char szName[64];
    char szPhone[64];
    
} USERDATA;

typedef struct NODE
{
    USERDATA* pData;        // 관리대상 데이터

    NODE* prev;             // 그 관리대상 데이터를 관리하는 자료구조
    NODE* next;
} NODE;

NODE* g_pHead; 
NODE* g_pTail;
int g_nSize;

void insertBefore(NODE* pTmp, USERDATA* pParam);

void initList(void) 
{
    g_pHead = (NODE*)malloc(sizeof(NODE));
    g_pTail = (NODE*)malloc(sizeof(NODE));
    
    g_nSize = 0;
    memset(g_pHead, 0, sizeof(NODE));
    memset(g_pTail, 0, sizeof(NODE));

    // strcpy_s(g_pHead->szData, sizeof(g_pHead->szData), "dummy head");
    // strcpy_s(g_pTail->szData, sizeof(g_pTail->szData), "dummy tail"); 
    
    g_pHead->next = g_pTail;
    g_pTail->prev = g_pHead;
}

void releaseList(void) 
{
    NODE* tmp = g_pHead;
    while(tmp!=NULL){
        NODE* pDelete = tmp;
        tmp = tmp->next;

        printf("delete[%p]", pDelete);
        free(pDelete->pData);
        free(pDelete);
    }

    g_pHead = NULL;
    g_pTail = NULL;
    g_nSize = 0;

    puts("releaseList()");
}

void printList(void) 
{
    printf("g_nSize: %d, g_pHead:[%p], g_pTail:[%p]", g_nSize, g_pHead, g_pTail);
    NODE* tmp = g_pHead;
    while(tmp!=NULL){
        printf("[%p], [%p], %s, [%p]", tmp, tmp->prev, tmp->pData->szName , tmp->next);
        tmp = tmp->next; 
    }
}

int insertAtHead(USERDATA* pParam) // 전 함수가 자료 의존적
{
    NODE* pNewNode = malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));

    pNewNode->pData = pParam;

    // strcpy_s(pNewNode->szData, sizeof(pNewNode->szData), pszData); 호출자가 메모리 동적할당 + 값설정까지 해서 전달하기 때문에 이것은 불필요

    pNewNode->prev = g_pHead;
    pNewNode->next = g_pHead->next;

    g_pHead->next = pNewNode;
    g_pHead->next->prev = pNewNode;

    g_nSize++;
    
    return g_nSize ;
}

int insertAtTail(USERDATA* pParam ) 
{

    insertBefore(g_pTail, pParam);
     
    return g_nSize ;
}

NODE* findNode(const char *pszName) 
{
    NODE* pTmp = g_pHead;
    while(pTmp != g_pTail)
    {
        if(strcmp(pTmp->pData->szName, pszName) == 0)
        {
            return pTmp;
        }
        pTmp = pTmp->next;
    }    
    
    return NULL;
}

int deleteNode(const char *pszName)
{
    NODE* pNode = findNode(pszName);

    pNode->prev->next = pNode->next;
    pNode->next->prev = pNode->prev;

    printf("deleteNode(): %p", pNode);
    free(pNode->pData);
    free(pNode);

    g_nSize--;
    return 0;
}

void insertBefore(NODE* pTmp, USERDATA* pParam) 
{
    NODE* pNewNode = malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));
    pNewNode->pData = pParam;

    // strcpy_s(pNewNode->szData, sizeof(pNewNode->szData), pszData);

    pNewNode->prev = pTmp->prev; 
    pNewNode->next = pTmp;

    pTmp->prev = pNewNode;
    pNewNode->prev->next = pNewNode;

    g_nSize++;
}

int insertAt(int idx, USERDATA* pParam)
{

    int i=0;
    NODE* pTmp = g_pHead->next;
    while(pTmp != g_pTail)
    {
        if (i==idx)
        {
            insertBefore(pTmp, pParam);
            return i;
        }
        i++;
        pTmp = pTmp->next;
    }

    insertAtTail(pParam);
    return i;
}

int getAt(int idx) 
{
    int i = 0;
    NODE* pTmp = g_pHead->next;
    while(pTmp != g_pTail)
    {
        if (i==idx)
        {
            return pTmp;
        }
        i++;
        pTmp = pTmp->next;
    }

    return NULL;
}

int getSize(void) {
    return g_nSize;
}

int getLength(void) {
    return getSize();
}

int main(void) 
{
    initList();

    USERDATA* newData = (USERDATA*)malloc(sizeof(USERDATA));
    memset(newData, 0, sizeof(newData));
    strcpy_s(newData->szName, "hosung", sizeof(newData->szName));
    strcpy_s(newData->szPhone, "010", sizeof(newData->szPhone));

    insertAtTail(newData);

    printList();
    
    printf("findNode()", findNode("test01")); 

    releaseList();

    return 0;
}


// ADT란??
// 이전 더블링크드리스트 파일과 다르게
// USERDATA 를 NODE와 분리해서
// 데이터와 자료구조를 구분하는것