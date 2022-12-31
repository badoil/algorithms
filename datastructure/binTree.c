#include <stdio.h>
#include <string.h>
#include <malloc.h>


typedef struct NODE
{
    char szData[64];

    NODE* left;
    NODE* right;
} NODE;


NODE* g_pRoot; 
int g_nSize;



void releaseTree(NODE *pParent) 
{
    if (pParent == NULL) return;

    releaseTree(pParent->left);
    releaseTree(pParent->right);

    printf("free(): %p, %s\n", pParent, pParent->szData);
    free(pParent);
    g_pRoot = NULL;
    g_nSize = 0;
}

void printTree(NODE *pParent) 
{
    if (pParent == NULL) return;

    printTree(pParent->left);

    printf("[%p] %p, %s [%p]", pParent->left, pParent, pParent->szData, pParent->right);

    printTree(pParent->right);

    return;
    putchar('\n');
    // printf("g_nSize: %d, g_pHead:[%p], g_pTail:[%p]", g_nSize, g_pHead, g_pTail);
    // NODE* tmp = g_pHead;
    // while(tmp!=NULL){
    //     printf("[%p], [%p], %s, [%p]", tmp, tmp->prev, tmp->szData, tmp->next);
    //     tmp = tmp->next; 
    // }
}

int insertNode(const char *pszData) 
{   
    NODE *pNewNode = (NODE*)malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));
    strcpy_s(pNewNode->szData, sizeof(pNewNode->szData), pszData);

    g_nSize++;

    if (g_pRoot == NULL)
    {
        g_pRoot = pNewNode;
    }

    NODE* pTemp = g_pRoot;
    while(pTemp != NULL)
    {
        // left
        if (strcmp(pTemp->szData, pNewNode->szData) > 0)
        {
            if (pTemp->left == NULL)
            {
                pTemp->left = pNewNode;
                break;
            }
            else
            {
                pTemp = pTemp->left;
                continue;
            }
        }
        // right
        else
        {
            if (pTemp->right == NULL)
            {
                pTemp->right = pNewNode;
                break;
            }
            else
            {
                pTemp = pTemp->right;
                continue;
            
        }
    }

    return 1;
}


NODE* findNode(const char *pszData) 
{
    // 선형 검색
    // NODE* pTmp = g_pHead;
    // while(pTmp != g_pTail)
    // {
    //     if(strcmp(pTmp->szData, pszData) == 0)
    //     {
    //         return pTmp;
    //     }
    //     pTmp = pTmp->next;
    // }    
    
    return NULL;
}

int deleteNode(const char *pszData)
{
    // 차후 구현
    return 0;
}

int getSize(void) {
    return g_nSize;
}

int getLength(void) {
    return getSize();
}

int main(void) 
{
    insertNode("5");        
    insertNode("4");
    insertNode("7");
    insertNode("6");
    insertNode("8");

    printTree(g_pRoot);
    releaseTree(g_pRoot);
    return 0;
}