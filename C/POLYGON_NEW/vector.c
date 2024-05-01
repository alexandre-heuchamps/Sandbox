#include <stdlib.h>
#include <stdio.h>
#include "point.h"
#include "vector.h"





struct Vector
{
    const point *origin;
    const point *end;
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
        vec -> origin = origin;
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
        vec -> end = end;
    }
    return NULL;
}