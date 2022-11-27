#include <stdio.h>
#include <string.h>
#include <malloc.h>


typedef struct NODE
{
    void* pData;        // 관리대상 데이터

    const char* (*getKey)(void*);     // 멤버함수 포인터, 이를 넣음으로서 NODE 구조체에 함수가 포함된것처럼 쓸 수 있음, 그리고 NODE라는 자료구조를 USERDATA 자료로부터 분리해서 함수를 통해 접근 가능

    NODE* prev;             // 그 관리대상 데이터를 관리하는 자료구조
    NODE* next;
} NODE;

NODE* g_pHead; 
NODE* g_pTail;
int g_nSize;

// void insertBefore(NODE* pTmp, USERDATA* pParam);
void insertBefore(NODE* pTmp, void* pParam, const char* (*pfParam)(void*));
int insertAtTail(void* pParam, const char* (*pfParam)(void*));

typedef struct USERDATA
{
    char szName[64];
    char szPhone[64];
    
} USERDATA;

const char* getKeyFromUserData(USERDATA* pUser) {
    return pUser->szName;
}

void createUserData(const char* pszName, const char* pszPhone) {
    USERDATA* newData = (USERDATA*)malloc(sizeof(USERDATA));
    memset(newData, 0, sizeof(newData));
    strcpy_s(newData->szName, sizeof(newData->szName), pszName);
    strcpy_s(newData->szPhone, sizeof(newData->szPhone), pszPhone);

    insertAtTail(newData, getKeyFromUserData);

}

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
        printf("[%p], [%p], %s, [%p]", tmp, tmp->prev, tmp->getKey(tmp->pData) , tmp->next);
        tmp = tmp->next; 
    }
}

int insertAtHead(USERDATA* pParam, const char* (*pfParam)(void*)) // 전 함수가 자료 의존적
{
    NODE* pNewNode = malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));

    pNewNode->pData = pParam;
    pNewNode->getKey = pfParam;

    // strcpy_s(pNewNode->szData, sizeof(pNewNode->szData), pszData); 호출자가 메모리 동적할당 + 값설정까지 해서 전달하기 때문에 이것은 불필요

    pNewNode->prev = g_pHead;
    pNewNode->next = g_pHead->next;

    g_pHead->next = pNewNode;
    g_pHead->next->prev = pNewNode;

    g_nSize++;
    
    return g_nSize ;
}

int insertAtTail(void* pParam, const char* (*pfParam)(void*)) 
{

    insertBefore(g_pTail, pParam, pfParam);
     
    return g_nSize ;
}

NODE* findNode(const char *pszKey) 
{
    NODE* pTmp = g_pHead;
    while(pTmp != g_pTail)
    {
        if(strcmp(pTmp->getKey(pTmp->pData), pszKey ) == 0)
        {
            return pTmp;
        }
        pTmp = pTmp->next;
    }    
    
    return NULL;
}

int deleteNode(const char *pszKey)
{
    NODE* pNode = findNode(pszKey);

    pNode->prev->next = pNode->next;
    pNode->next->prev = pNode->prev;

    printf("deleteNode(): %p", pNode);
    free(pNode->pData);
    free(pNode);

    g_nSize--;
    return 0;
}

void insertBefore(NODE* pTmp, void* pParam, const char* (*pfParam)(void*)) 
{
    NODE* pNewNode = malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));
    pNewNode->pData = pParam;
    pNewNode->getKey = pfParam;

    // strcpy_s(pNewNode->szData, sizeof(pNewNode->szData), pszData);

    pNewNode->prev = pTmp->prev; 
    pNewNode->next = pTmp;

    pTmp->prev = pNewNode;
    pNewNode->prev->next = pNewNode;

    g_nSize++;
}

int insertAt(int idx, void* pParam, const char* (*pfParam)(void*))
{

    int i=0;
    NODE* pTmp = g_pHead->next;
    while(pTmp != g_pTail)
    {
        if (i==idx)
        {
            insertBefore(pTmp, pParam, pfParam); 
            return i;
        }
        i++;
        pTmp = pTmp->next;
    }

    insertAtTail(pParam, pfParam );
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

    createUserData("hosung", "010");

    printList();
    
    printf("findNode()", findNode("test01")); 

    releaseList();

    return 0;
}


// ADT란??
// 이전 더블링크드리스트 파일과 다르게
// USERDATA 를 NODE와 분리해서
// 데이터와 자료구조를 구분하는것


//멤버함수 포인터, 이를 넣음으로서 NODE 구조체에 함수가 포함된것처럼 쓸 수 있음, 그리고 NODE라는 자료구조를 USERDATA 자료로부터 분리해서 함수를 통해 접근 가능
// 함수들 보면 더이상 USERDATA에 의존하지 않고 있음
// 대신 함수 포인터를 넘겨야함
// 함수포인터를 NODE가 아니라 USERDATA 넣을지 고민해 볼것