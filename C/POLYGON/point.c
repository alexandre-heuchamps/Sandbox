#include <stdlib.h>
#include <stdio.h>
#include "point.h"

#define GET_VALUE_ERROR (2L)



struct Point
{
    float x;
    float y;
};



point *point_alloc(void)
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



void *point_free(point *pt)
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



void *point_init(point *pt, float x, float y)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot initiate point.\n");
        return NULL;
    }
    else
    {
        pt -> x = x;
        pt -> y = y;
        return NULL;
    }
}



void *point_print(const point *pt)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot print point.\n");
        return NULL;
    }
    else
    {
        printf("Point at (%f, %f)\n", pt -> x, pt -> y);
        return NULL;
    }
}



float point_get_x(const point *pt)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot get point.\n");
        return GET_VALUE_ERROR;
    }
    else
    {
        return pt -> x;
    }
}



float point_get_y(const point *pt)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot get point.\n");
        return GET_VALUE_ERROR;
    }
    else
    {
        return pt -> y;
    }
}



void *point_set_x(point *pt, float x)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot get point.\n");
        return NULL;
    }
    else
    {
        pt -> x = x;
        return NULL;
    }
}



void *point_set_y(point *pt, float y)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot get point.\n");
        return NULL;
    }
    else
    {
        pt -> y = y;
        return NULL;
    }
}