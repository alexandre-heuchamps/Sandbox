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
    }
    return NULL;
}