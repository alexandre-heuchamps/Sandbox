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
        free_point(vec -> origin);
        free_point(vec -> end);
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
    }
    return NULL;
}





void *init_origin_vector(vector *vec, float x, float y)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Could not initialise vector origin.\n");
    }
    else
    {
        set_x_point(vec -> origin, x);
        set_y_point(vec -> origin, y);
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
    }
    return NULL;
}





void *set_xorigin_vector(vector *vec, float x)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Cannot set x coordinate for vector origin.\n");
    }
    else
    {
        set_x_point(vec -> origin, x);
    }
    return NULL;
}





void *set_yorigin_vector(vector *vec, float y)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Cannot set y coordinate for vector origin.\n");
    }
    else
    {
        set_y_point(vec -> origin, y);
    }
    return NULL;
}





void *set_xend_vector(vector *vec, float x)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Cannot set x coordinate for vector end.\n");
    }
    else
    {
        set_x_point(vec -> end, x);
    }
    return NULL;
}





void *set_yend_vector(vector *vec, float y)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Cannot set y coordinate for vector end.\n");
    }
    else
    {
        set_y_point(vec -> end, y);
    }
    return NULL;
}





float get_xorigin_vector(const vector *vec)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Cannot get x coordinate for vector origin.\n");
        return -1;
    }
    else
    {
        return get_x_point(vec -> origin);
    }
}





float get_yorigin_vector(const vector *vec)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Cannot get y coordinate for vector origin.\n");
        return -1;
    }
    else
    {
        return get_y_point(vec -> origin);
    }
}





float get_xend_vector(const vector *vec)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Cannot get x coordinate for vector end.\n");
        return -1;
    }
    else
    {
        return get_x_point(vec -> end);
    }
}





float get_yend_vector(const vector *vec)
{
    if(NULL == vec)
    {
        fprintf(stderr, "Cannot get y coordinate for vector end.\n");
        return -1;
    }
    else
    {
        return get_y_point(vec -> end);
    }
}