#include <stdlib.h>
#include <stdio.h>
#include <math.h>
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
    }
    else
    {
        free(pt);
        pt = NULL;
    }
    return NULL;
}





void *set_x_point(point *pt, float x)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot set 'x' of point.\n");
    }
    else
    {
        pt -> x = x;
    }
    return NULL;
}





void *set_y_point(point *pt, float y)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot set 'y' of point.\n");
    }
    else
    {
        pt -> y = y;
    }
    return NULL;
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





void *init_point(point *pt, float x, float y)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot initialise point.\n");
    }
    else
    {
        pt -> x = x;
        pt -> y = y;
    }
    return NULL;
}





void *print_point(const point *pt)
{
    if(NULL == pt)
    {
        fprintf(stderr, "Cannot print point information");
    }
    else
    {
        printf("(x, y) = (%lf, %lf)\n", get_x_point(pt), get_y_point(pt));
    }
    return NULL;
}





void *rotate_point(point *pt, const point *origin, float ang)
{
    if(NULL == pt || NULL == origin)
    {
        fprintf(stderr, "Cannot rotate point.\n");
    }
    else
    {
        float x_origin = get_x_point(origin);
        float y_origin = get_y_point(origin);

        float x_pt = get_x_point(pt);
        float y_pt = get_y_point(pt);

        float x_to_origin = x_pt - x_origin;
        float y_to_origin = y_pt - y_origin;

        float x_pt_rot = x_to_origin * cos(ang) - y_to_origin * sin(ang);
        float y_pt_rot = x_to_origin * sin(ang) + y_to_origin * cos(ang);

        set_x_point(pt, x_pt_rot + x_origin);
        set_y_point(pt, y_pt_rot + y_origin);
    }
    return NULL;
}