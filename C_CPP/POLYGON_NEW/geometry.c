#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "point.h"
#include "vector.h"





void *translate_point(point *pt, const vector *vec)
{
    if(NULL == pt || NULL == vec)
    {
        fprintf(stderr, "Cannot translate point.\n");
    }
    else
    {
        float xdir = get_xend_vector(vec) - get_xorigin_vector(vec);
        float ydir = get_yend_vector(vec) - get_yorigin_vector(vec);
        set_x_point(pt, get_x_point(pt) + xdir);
        set_y_point(pt, get_y_point(pt) + ydir);
    }
    return NULL;
}





void *rotate_point(point *pt, const point *origin_rot, float ang)
{
    if(NULL == pt || NULL == origin_rot)
    {
        fprintf(stderr, "Cannot rotate point.\n");
    }
    else
    {
        float x_origin = get_x_point(origin_rot);
        float y_origin = get_y_point(origin_rot);

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