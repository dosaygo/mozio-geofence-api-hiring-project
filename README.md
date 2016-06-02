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


