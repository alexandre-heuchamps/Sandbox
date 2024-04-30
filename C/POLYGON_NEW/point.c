#include <stdlib.h>
#include <stdio.h>
#include "point.h"





struct Point
{
    float x;
    float y;
};





point *alloc_point(void)
{
    point *pt = malloc(sizeof *pt);

    if(NULL == pt)
    {
        fprintf(stderr, "Could not allocate point.\n");
        return NULL;
    }
    else
    {
        return pt;
    }
}





void *free_point(point *pt)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Could not free point.\n");
        return NULL;
    }
    else
    {
        free(pt);
        pt = NULL;
        return NULL;
    }
}