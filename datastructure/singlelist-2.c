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
        // pNode->next = g_pHead->next;     이거는 내가 했는데 틀린건가??
        // g_pHead->next = pNode;

        pNode->next = g_pHead;
        g_pHead = pNode;
    }
    
    return 1;
}

void ReleaseData(void) {
    NODE* pTmp = g_pHead->next;
    while(pTmp != NULL) {
        NODE* pDelete = pTmp;
        pTmp = pTmp->next;
        
        printf("Delete: [%p] %s\n", pDelete, pDelete->szData);
        free(pDelete);
    }
    g_pHead->next = 0;      // g_pHead->next가 메모리 해제 되었기 때문에 이것을 안해주면 쓰레기 값을 가리키게됨, 후에 InsertNode하면 삽입된 노드가 이 쓰레기 노드에 접근하는데 이때 에러 발생
    
}

int FindData(char* pszData)
{
    NODE* pTmp = g_pHead;
    while(pTmp != NULL) 
    {
        if (strcmp(pTmp->next, pszData) == 0)
            return 1;
        pTmp = pTmp->next;
    }
    return 0;
}

int DeleteData(char* pszData)
{
    NODE* pTmp = g_pHead;
    NODE* prev = NULL;
    while(pTmp != NULL) 
    {
        if (strcmp(pTmp->next, pszData) == 0)
        {
            if (prev!=NULL) prev->next = pTmp->next;
            else g_pHead = pTmp->next;
            
            free(pTmp);  
        }
        prev = pTmp;
        pTmp = pTmp->next;
    }
    return 0;
}

int main() {

    // 테스트
    InsertNode("test01");
    PrintList();

    InsertNode("test02");
    PrintList();

    InsertNode("test03");
    PrintList();

    if (FindData("test03")==1) printf("test03 found!\n");

    ReleaseData();
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


// 이것은 g_pHead에 처음 노드를 할당해서 연결리스트 만듬