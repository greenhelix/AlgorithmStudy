#include <stdio.h>

void BubbleSort(int DataSet[], int length){
    int i, j, temp = 0; 
    for ( i = 0; i < (length-1); i++)
    {
        for ( j = 0; j < length-(i+1); j++)
        {
            if (DataSet[j] > DataSet[j+1])
            {
                temp = DataSet[j+1];
                DataSet[j+1] = DataSet[j];
                DataSet[j] = temp;
            }            
        }
    }
}


int main(void)
{
    int DataSet[] = {6,4,2,3,1,5};
    int length = sizeof DataSet / sizeof DataSet[0];
    int i = 0; 

    for ( i = 0; i < length; i++)
    {
        printf("%d ", DataSet[i]);
    }

    printf("\nBubbleSort\n");

    BubbleSort(DataSet, length);

    for ( i = 0; i < length; i++)
    {
        printf("%d ", DataSet[i]);
    }

    printf("\n");

    return 0;
}