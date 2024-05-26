#include <stdio.h>
#include <stdlib.h>

#ifndef disjoint_h
#define disjoint_h

typedef struct tagDisjointSet
{
    struct tagDisjointSet * Parent;
    void* Data;
}DisjointSet;

void DS_UnionSet(DisjointSet* set1, DisjointSet* set2);
DisjointSet* DS_FindSet(DisjointSet* set);
DisjointSet* DS_MakeSet(void* NewData);
void DS_DestroySet(DisjointSet* set);

#endif