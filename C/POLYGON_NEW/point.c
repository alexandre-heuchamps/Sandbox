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





void *set_x_point(point *pt, float x)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot set 'x' of point.\n");
        return NULL;
    }
    else
    {
        pt -> x = x;
        return NULL;
    }
}





void *set_y_point(point *pt, float y)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot set 'y' of point.\n");
        return NULL;
    }
    else
    {
        pt -> y = y;
        return NULL;
    }
}




float get_x_point(const point *pt)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot get 'x' from point.\n");
        return -1.0;
    }
    else
    {
        return pt -> x;
    }
}





float get_y_point(const point *pt)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot get 'y' from point.\n");
        return -1.0;
    }
    else
    {
        return pt -> y;
    }
}