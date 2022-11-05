#include <stdio.h>
#include <string.h>
#include <malloc.h>

typedef struct USERDATA {
    
    unsigned int nHeight;
    char szName[12];
    char szPhone[12];


} USERDATA;


int main() {

    USERDATA a;
    a.nHeight = 180;
    strcpy_s(a.szName, sizeof(USERDATA), "jinoo-joo");
    strcpy_s(a.szPhone, sizeof(USERDATA), "jinoo-joo");
    
    // 위와 아래는 동일함
    // 아래처럼 포인터 사용해서 하는거 알아야함
    char buffer[sizeof(USERDATA)];
    USERDATA *pBuffer = (USERDATA*)buffer;
    pBuffer->nHeight = 180;
    strcpy_s(pBuffer->szName, sizeof(pBuffer->szName), "jinoo-joo");
    strcpy_s(pBuffer->szPhone, sizeof(pBuffer->szPhone), "jinoo-joo");
    
    return 0;
}


// 구조체는 자료형들의 세트, 즉 자료구조임
// 다른 형식의 자료형들의 세트