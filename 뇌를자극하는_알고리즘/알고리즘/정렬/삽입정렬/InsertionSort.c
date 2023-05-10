#include <stdio.h>
#include <string.h>

void insertionSort(int dataSet[], int length)
{
    int i, j, value = 0;

    for(i=1; i<length; i++)
    {
        if(dataSet[i-1] <= dataSet[i]) continue; // 이 부분이 버블 정렬과 차이다. 비교자체를 안할 수 있음.

        value = dataSet[i];

        for(j=0; j<i; j++)
        {
            if(dataSet[j] > value)
            {
                memmove(&dataSet[j+1], &dataSet[j], sizeof(dataSet[0]) * (i-j));
                dataSet[j] = value;
                break;
            }
        }
    }
}

/*
memmove() function 
메모리의 내용을 이동시키는 기능이다. 
배열처럼 연속된 데이터를 단번에 이동시킬 때 유용하다. 
memmove()대신 순환문으로 대체할 수 있지만 성능이 훨씬 떨어진다. 

memmove() param1 : 원본 데이터가 옮길 새로운 메모리의 주소
memmove() param2 : 매개 변수는 원본 데이터가 있는 주소
memmove() param3 : 이동시킬 데이터의 양(byte)

이와 비슷한 함수 memcpy() 가 있다. 
memmove()가 원본 데이터를 대상 메모리 주소로 이동 시키는 반면,
memcpy()는 원본 데이터를 대상 메모리 주소로 복사 시킨다.
이러한 차이가 있을뿐 기능한 같다. 
*/

int main(void)
{
    int dataset[] = {6,4,2,3,1,5};
    int length = sizeof dataset / sizeof dataset[0];
    int i =0;
    for(i = 0; i<length; i++)
    {
        printf("%d ", dataset[i]);
    }

    printf("\nINSERTION SORT\n");

    insertionSort(dataset, length);

    for(i = 0; i<length; i++)
    {
        printf("%d ", dataset[i]);
    }

    printf("\n");

    return 0; 
}