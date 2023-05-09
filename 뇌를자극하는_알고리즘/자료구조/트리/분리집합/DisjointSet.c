#include "DisjointSet.h"

void DS_UnionSet(DisjointSet *set1, DisjointSet *set2)
{
    set2 = DS_FindSet(set2);
    set2->Parent = set1;
}

DisjointSet *DS_FindSet(DisjointSet *set)
{
    while(set->Parent != NULL){
        set = set->Parent;
    }
    return set;
}

DisjointSet *DS_MakeSet(void *NewData)
{
    DisjointSet* NewNode = (DisjointSet*)malloc(sizeof(DisjointSet));
    NewNode->Data = NewData;
    NewNode->Parent = NULL;
    return NewNode;
}

void DS_DestroySet(DisjointSet *set)
{
    free(set);
}
