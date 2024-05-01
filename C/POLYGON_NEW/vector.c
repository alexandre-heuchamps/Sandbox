#include <stdlib.h>
#include <stdio.h>
#include "point.h"
#include "vector.h"





struct Vector
{
    point *origin;
    point *end;
};





vector *alloc_vector(void)
{
    vector *vec = malloc(sizeof *vec);

    if(NULL == vec)
    {
        fprintf(stderr, "Could not allocate vector.\n");
        return NULL;
    }
    else
    {
        return vec;
    }
}





void *free_vector(vector *vec)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Could not free vector.\n");
    }
    else
    {
        free(vec);
        vec = NULL;
    }
    return NULL;
}





void *set_origin_vector(vector *vec, const point *origin)
{
    if(NULL == vec || NULL == origin)
    {
        fprintf(stderr, "Could not set vector origin.\n");
    }
    else
    {
        point *origin_copy = alloc_point();
        set_x_point(origin_copy, get_x_point(origin));
        set_y_point(origin_copy, get_y_point(origin));
        vec -> origin = origin_copy;
        free_point(origin_copy);
    }
    return NULL;
}





void *set_end_vector(vector *vec, const point *end)
{
    if(NULL == vec || NULL == end)
    {
        fprintf(stderr, "Could not set vector end.\n");
    }
    else
    {
        point *end_copy = alloc_point();
        set_x_point(end_copy, get_x_point(end));
        set_y_point(end_copy, get_y_point(end));
        vec -> end = end_copy;
        free_point(end_copy);
    }
    return NULL;
}