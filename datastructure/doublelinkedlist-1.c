#include <stdio.h>
#include <string.h>
#include <malloc.h>


typedef struct NODE
{
    char szData[64];

    NODE* prev;
    NODE* next;
} NODE;


NODE* g_pHead; 
NODE* g_pTail;
int g_nSize;

void insertBefore(NODE* pTmp, const char* pszData);

void initList(void) 
{
    g_pHead = (NODE*)malloc(sizeof(NODE));
    g_pTail = (NODE*)malloc(sizeof(NODE));
    
    g_nSize = 0;
    memset(g_pHead, 0, sizeof(NODE));
    memset(g_pTail, 0, sizeof(NODE));

    strcpy_s(g_pHead->szData, sizeof(g_pHead->szData), "dummy head");
    strcpy_s(g_pTail->szData, sizeof(g_pTail->szData), "dummy tail"); 
    
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
        printf("[%p], [%p], %s, [%p]", tmp, tmp->prev, tmp->szData, tmp->next);
        tmp = tmp->next; 
    }
}

int insertAtHead(const char *pszData) 
{
    NODE* pNewNode = malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));

    strcpy_s(pNewNode->szData, sizeof(pNewNode->szData), pszData);

    pNewNode->prev = g_pHead;
    pNewNode->next = g_pHead->next;

    g_pHead->next = pNewNode;
    g_pHead->next->prev = pNewNode;

    g_nSize++;
    
    return g_nSize ;
}

int insertAtTail(const char *pszData) 
{
    // NODE* pNewNode = malloc(sizeof(NODE));
    // memset(pNewNode, 0, sizeof(NODE));

    // strcpy_s(pNewNode->szData, sizeof(pNewNode->szData), pszData);

    // pNewNode->prev = g_pTail->prev;
    // pNewNode->next = g_pTail;

    // g_pTail->prev = pNewNode;
    // pNewNode->prev->next = pNewNode;

    // g_nSize++;

    insertBefore(g_pTail, pszData);
     
    return g_nSize ;
}

NODE* findNode(const char *pszData) 
{
    NODE* pTmp = g_pHead;
    while(pTmp != g_pTail)
    {
        if(strcmp(pTmp->szData, pszData) == 0)
        {
            return pTmp;
        }
        pTmp = pTmp->next;
    }    
    
    return NULL;
}

int deleteNode(const char *pszData)
{
    NODE* pNode = findNode(pszData);

    pNode->prev->next = pNode->next;
    pNode->next->prev = pNode->prev;

    printf("deleteNode(): %p", pNode);
    free(pNode);

    g_nSize--;
    return 0;
}

void insertBefore(NODE* pTmp, const char* pszData) 
{
    NODE* pNewNode = malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));

    strcpy_s(pNewNode->szData, sizeof(pNewNode->szData), pszData);

    pNewNode->prev = pTmp->prev;
    pNewNode->next = pTmp;

    pTmp->prev = pNewNode;
    pNewNode->prev->next = pNewNode;

    g_nSize++;
}

int insertAt(int idx, const char* pszData)
{

    int i=0;
    NODE* pTmp = g_pHead->next;
    while(pTmp != g_pTail)
    {
        if (i==idx)
        {
            insertBefore(pTmp, pszData);
            return i;
        }
        i++;
        pTmp = pTmp->next;
    }

    insertAtTail(pszData);
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

    insertAtHead("test01");
    insertAtHead("test02");
    insertAtHead("test03");

    printList();
    
    printf("findNode()", findNode("test01")); 

    releaseList();

    return 0;
}