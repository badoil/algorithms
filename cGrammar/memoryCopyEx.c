#include <stdio.h>
#include <string.h>
#include <malloc.h>


int main() {
    char srcData[12] = {'hello'};
    char dstData[12] = { 0 };


    // deep copy: 내용 자체를 복사
    memcpy(dstData, srcData, sizeof(dstData));

    // dstData = srcData;  dstData는 r-value라 불가능

    // shallow copy: 주소만 복사
    char* pDstData = srcData;

    char* pDstData2 = malloc(sizeof(char) * 12);

    char* pDstData3 = malloc(sizeof(char) * 12);
    
    memcpy(pDstData2, srcData, sizeof(char)*12);

    pDstData3 = srcData;    // 이렇게 하면 오류, 이건 단지 주소만 복사한것, 더 큰 문제는 기존에 할당받은 pDstData3가 가리키는 메모리는 남아있고 메모리 릭 일으킴

    put(pDstData2);
    free(pDstData2);
    
    return 0;
}


// deep copy와 shallow copy 차이
// pDstData3 = srcData;    // 이렇게 하면 오류, 이건 단지 주소만 복사한것, 더 큰 문제는 기존에 할당받은 pDstData3가 가리키는 메모리가 지워지지 않고 남게되어 메모리 릭