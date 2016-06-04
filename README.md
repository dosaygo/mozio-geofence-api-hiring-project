# mozio-geofence-api-hiring-project

Build a geofence API for Mozio.

## idea

Exact GeoFence search involves many operations, and includes things like occupancy trees. 

*Why go to all the trouble ?*

We can have an approximate geofence search, that is still mostly useful.

It's faster, and involves less code and operations. That's FAST, capital letters fast.

And of course, if you want to change the internals to exact later on, well, of course you can!

## approximate how ?

Every polygon has a centre of mass, and a maximum diameter. So we approximate a polygon to a circle centered on the centre of mass and with a dimater equal to the maximum diameter. 

There are other approximations we can choose, and this is one place to start. 

It's straightforward, and can always be extended.

## some details, please

Okay well we get a bag of x,y points. We can use k-means to group these into clusters. And each cluster we can make a circle centered on the mean point, with the cluster radius. That effectively decomposes the polygon into circles. Now, these aren't guaranteed to be overlapping circles. But maybe we can find a way to do it that does guarantee overlap, minimum covering of a polygon with circles. We could do the min cover with squares, then expand them into circles that cover those squares, guaranteeing the cover is preserved.

But hey, that's an improvement. And we are just doing the most straightforward method, which is...

Finding the centroid, and the distance to the fursthes point, and making a circle based on those two co-ordinates to approximate the territory. 

Search on these circles is guaranteed fast, and we use Google App Engine's Search API's GeoPt class, combined with the distance function to perform these searches. 

## an update

In fact, there is a more workable improvement that the proposed decomposition into circles. One reason it works to choose this improvement is because of a limitation of the datastore. We cannot perform searches on repeated or list properties. That is, we cannot perform a property query on a named property which is a list, and hope to match that query against all items in that list in all entities. This is because there are no repeat properties in this datastore. 

Despite this limitation it is true that not all territories are most effectively approximated by a circle. Some may be better approximated by a triangle of some shape. How can this be achieved having only a distance function ? 

In addition to our method of "circulation", where we approximate territories by circles, and use a single centroid and a maximum radius as the bound against which to query the given point, we can employ a method of "triangulation", where we approximate territories by the intersection of three circles, and  use three centroids. Even if these all must share the same radius  ( being the maximum radius we choose ), still a great many types of triangular intersecting regions of the three circles are possible. 

It is also a way we can ensure our point falls in a far smaller area than the given radius, since the fulfillment of the query of distance to three circles more greatly limits the size of the area that will fulfill it. This means we can also increase the length of the maximum radius to provide perhaps greater convenience for providers who can then enter territories covering larger areas. 

## query examples

*Note : We formulate these automatically using the given point.*

**Circulation query**

`distance(centroid, geopoint(x, y)) < 100`

**Triangulation query**

```
 distance(centroid1, geopoint(x, y)) < 100 AND
 distance(centroid2, geopoint(x, y)) < 100 AND
 distance(centroid3, geopoint(x, y)) < 100
```

## How to employ this improvement

There are two parts to using this:

1. Decide which territories are better approximated by a circle, mark them as `circulated` and given them one centroid, and decide which are better approximated by a triangle and given them three centroids, and mark them as 'triangulated'

2. Decide how to choose the three centroids in a way which provides a tight approximation.


