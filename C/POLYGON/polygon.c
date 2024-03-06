#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "point.h"
#include "polygon.h"

#ifndef M_PI
    #define M_PI (3.14159265358979323846264338327950288)
#endif

#define GET_NSIDE_ERROR (2U)



struct Polygon
{
    unsigned nside;
    point *centre;
    point **vertices;
};



polygon *polygon_alloc(unsigned nside)
{
    if(nside == 0)
    {
        fprintf(stderr, "Cannot have a 0-sided polygon.\n");
        return NULL;
    }
    else
    {
        polygon *poly = malloc(sizeof(*poly));

        if(NULL == poly)
        {
            fprintf(stderr, "Cannot allocate polygon.\n");
            return NULL;
        }
        else
        {
            poly -> nside = nside;
            poly -> centre = point_alloc();
            if(NULL == poly -> centre)
            {
                fprintf(stderr, "Cannot allocate polygon centre.\n");
                free(poly);
                poly = NULL;
                return NULL;
            }
            else
            {
                poly -> vertices = malloc(nside * sizeof(point*));
                if(NULL == poly -> vertices)
                {
                    fprintf(stderr, "Cannot allocate polygon vertices.\n");
                    free(poly -> centre);
                    poly -> centre = NULL;
                    free(poly);
                    poly = NULL;
                    return NULL;
                }
                else
                {
                    for(unsigned i = 0; i < nside; i++)
                    {
                        poly -> vertices[i] = point_alloc();
                        if(NULL == poly -> vertices[i])
                        {
                            fprintf(stderr, "Cannot allocate node %u.\n", i);
                            for(unsigned j = 0; j < i; j++)
                            {
                                free(poly -> vertices[j]);
                                poly -> vertices[j] = NULL;
                            }
                            free(poly -> centre);
                            poly -> centre = NULL;
                            free(poly -> vertices);
                            poly -> vertices = NULL;
                            free(poly);
                            poly = NULL;
                        }
                    }
                }
            }
        }

        return poly;
    }
}



void *polygon_free(polygon *poly)
{
    if(NULL == poly)
    {
        fprintf(stderr, "Cannot free polygon.\n");
        return NULL;
    }
    else
    {
        if(NULL == poly -> centre)
        {
            fprintf(stderr, "Cannot free polygon centre.\n");
            return NULL;
        }
        else
        {
            free(poly -> centre);
            poly -> centre = NULL;

            if(NULL == poly -> vertices)
            {
                fprintf(stderr, "Cannot free polygon vertices.\n");
                return NULL;
            }
            else
            {
                for(unsigned i = 0; i < poly -> nside; i++)
                {
                    if(NULL == poly -> vertices[i])
                    {
                        fprintf(stderr, "Cannot free vertex %u.\n", i);
                        return NULL;
                    }
                    else
                    {
                        free(poly -> vertices[i]);
                        poly -> vertices[i] = NULL;
                    }
                }

                free(poly -> vertices);
                poly -> vertices = NULL;
            }
        }

        free(poly);
        poly = NULL;
    }

    return NULL;
}



void *polygon_init(polygon *poly, unsigned nside, float radius, point *centre)
{
    if(NULL == poly)
    {
        fprintf(stderr, "Polygon not existing.\n");
        return NULL;
    }
    else if(NULL == centre)
    {
        fprintf(stderr, "Polygon centre not existing.\n");
        polygon_free(poly);
        return NULL;
    }
    else
    {
        polygon_set_nside(poly, nside);
        // polygon_set_centre(poly, centre);   // This causes a problem

        for(unsigned i = 0; i < poly -> nside; i++)
        {
            float angle = (1 + 2 * i) * (M_PI / poly -> nside);
            float x = radius * cos(angle);
            float y = radius * sin(angle);
            polygon_set_vertex(poly, i, x, y);
        }

        return NULL;
    }
}



void *polygon_print(const polygon *poly)
{
    if(NULL == poly)
    {
        fprintf(stderr, "Try printing non-existing polygon.\n");
        return NULL;
    }
    else
    {
        printf("\n%u-sided polygon centered at (%f, %f)\n",
                    poly -> nside,
                    point_get_x(poly -> centre),
                    point_get_y(poly -> centre)
        );

        printf("Vertices:\n");
        for(unsigned i = 0; i < poly -> nside; i++)
        {
            float angle = 180 * (1 + 2 * i) / poly -> nside;
            printf("\t Vertex %u: (%f, %f) (angle: %f degree)\n",
                        i,
                        point_get_x(poly -> vertices[i]),
                        point_get_y(poly -> vertices[i]),
                        angle
                );
        }

        return NULL;
    }
}



unsigned polygon_get_nside(const polygon *poly)
{
    if(NULL == poly)
    {
        fprintf(stderr, "Cannot get polygon number of sides.\n");
        return GET_NSIDE_ERROR;
    }
    else
    {
        return poly -> nside;
    }
}



void *polygon_set_nside(polygon *poly, unsigned nside)
{
    if(NULL == poly)
    {
        fprintf(stderr, "Cannot set polygon number of sides.\n");
        return NULL;
    }
    else
    {
        poly -> nside = nside;
        return NULL;
    }
}



point *polygon_get_centre(const polygon *poly)
{
    if(NULL == poly)
    {
        fprintf(stderr, "Cannot get polygon centre.\n");
        return NULL;
    }
    else
    {
        return poly -> centre;
    }
}



void *polygon_set_centre(polygon *poly, point *centre)
{
    if(NULL == poly)
    {
        fprintf(stderr, "Cannot set polygon number of sides.\n");
        return NULL;
    }
    else
    {
        poly -> centre = centre;
        return NULL;
    }
}



point *polygon_get_vertex(const polygon *poly, unsigned index)
{
    if(NULL == poly)
    {
        fprintf(stderr, "Cannot access polygon.\n");
        return NULL;
    }
    else if(index >= poly -> nside)
    {
        fprintf(stderr, "Try to access vertex out of polygon scope.\n");
        return NULL;
    }
    else
    {
        return (poly -> vertices[index]);
    }
}



void *polygon_set_vertex(polygon *poly, unsigned index, float x, float y)
{
    if(NULL == poly)
    {
        fprintf(stderr, "Cannot access polygon.\n");
        return NULL;
    }
    else if(index >= poly -> nside)
    {
        fprintf(stderr, "Try to access vertex out of polygon scope.\n");
        return NULL;
    }
    else
    {
        point_set_x(poly -> vertices[index], x);
        point_set_y(poly -> vertices[index], y);
        return NULL;
    }
}