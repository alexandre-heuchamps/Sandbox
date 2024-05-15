#ifndef POLYGON_H
#define POLYGON_H

typedef struct Polygon polygon;

polygon *polygon_alloc(unsigned);
void *polygon_free(polygon *);
void *polygon_init(polygon *, unsigned, float, point *);
void *polygon_print(const polygon *);
unsigned polygon_get_nside(const polygon *);
void *polygon_set_nside(polygon *, unsigned);
point *polygon_get_centre(const polygon *);
void *polygon_set_centre(polygon *, point *);
point *polygon_get_vertex(const polygon *, unsigned);
void *polygon_set_vertex(polygon *, unsigned, float, float);

#endif