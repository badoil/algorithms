#include <stdio.h>
#include <string.h>
#include <malloc.h>


typedef struct NODE
{
    void* pData;        // 관리대상 데이터

    NODE* prev;             // 그 관리대상 데이터를 관리하는 자료구조
    NODE* next;
} NODE;

NODE* g_pHead; 
NODE* g_pTail;
int g_nSize;

// void insertBefore(NODE* pTmp, USERDATA* pParam);
void insertBefore(NODE* pTmp, void* pParam);
int insertAtHead(USERDATA* pParam);
int insertAtTail(void* pParam);

typedef struct USERDATA
{
    const char* (*getKey)(void*);     // 멤버함수 포인터, 이를 넣음으로서 NODE 구조체에 함수가 포함된것처럼 쓸 수 있음, 그리고 NODE라는 자료구조를 USERDATA 자료로부터 분리해서 함수를 통해 접근 가능

    char szName[64];
    char szPhone[64];
    
} USERDATA;

const char* getKeyFromUserData(USERDATA* pUser) {
    return pUser->szName;
}

USERDATA* createUserData(const char* pszName, const char* pszPhone) 
{
    USERDATA* pNewData = (USERDATA*)malloc(sizeof(USERDATA));
    memset(pNewData, 0, sizeof(pNewData));
    strcpy_s(pNewData->szName, sizeof(pNewData->szName), pszName);
    strcpy_s(pNewData->szPhone, sizeof(pNewData->szPhone), pszPhone);

    // 구조체 멤버 함수 포인터 초기화
    pNewData->getKey = getKeyFromUserData;  // USERDATA 만들때 거기에 함수를 집어넣어버림

    // insertAtTail(pNewData);
    return pNewData;
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
    NODE* pTmp = g_pHead;
    while(pTmp!=NULL){
        USERDATA* pUser = pTmp->pData;
        printf("[%p], [%p], %s, [%p]", pTmp, pTmp->prev, 
                // pTmp->getKey(tmp->pData), 
                pUser->getKey(pUser),
                pTmp->next);
        pTmp = pTmp->next; 
    }
}

int insertAtHead(USERDATA* pParam) // 전에는 함수포인터 때문에 함수가 자료 의존적이었는데, 이를 삭제함(USERDATA에 함수포인터 넣으면서)
{
    NODE* pNewNode = malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));

    pNewNode->pData = pParam;
    // pNewNode->getKey = pfParam;


    pNewNode->prev = g_pHead;
    pNewNode->next = g_pHead->next;

    g_pHead->next = pNewNode;
    g_pHead->next->prev = pNewNode;

    g_nSize++;
    
    return g_nSize ;
}

int insertAtTail(void* pParam) 
{

    insertBefore(g_pTail, pParam);
     
    return g_nSize ;
}

NODE* findNode(const char *pszKey) 
{
    NODE* pTmp = g_pHead;

    const char* (*pfGetKey)(void*) = NULL;
    while(pTmp != g_pTail)
    {
        // 관리대상 데이터 구조체의 첮번째 멤버가 함수 포인터임을 전제!!
        pfGetKey = pTmp->pData;     // pData는  void*고 pfGetKey는 함수포인터라 형이 안맞아도 에러 안뜸, 문제 있음
        if(strcmp(pfGetKey(pTmp->pData), pszKey ) == 0)
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

void insertBefore(NODE* pTmp, void* pParam) 
{
    NODE* pNewNode = malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));
    pNewNode->pData = pParam;
    // pNewNode->getKey = pfParam;

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

    USERDATA* pNewData = NULL;
    pNewData = createUserData("hosung", "010");     // USERDATA 만 떨어져나오게 함, 즉 자료와 자료구조 분리
    insertAtTail(pNewData);

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


// 이번것은 저번것과 다르게 자료 구조체에 함수포인터를 옮겨버림
// 이렇게하면 자료의존적인 것을 피할 수 있음
// 다만 아직 유지보수성 및 재사용성은 떨어짐
// 전역변수도 있어서 멀티스레딩 고려하면 좋지 않음

// 여기서 createUserData 함수는 c++ 에서 생성자의 역할을 하는 것임