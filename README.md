# mozio-geofence-api-hiring-project

Build a geofence API for Mozio.

## idea

Exact GeoFence search involves many operations, and includes things like occupancy trees. 

Why go to all the trouble ?

We can have an approximate geofence search, that is still mostly useful.

It's faster, and involves less code and operations.

And of course, if you want to change the internals to exact later on, well, of course you can!

## approximate how ?

Every polygon has a centre of mass, and a maximum diameter. So we approximate a polygon to a circle centered on the centre of mass and with a dimater equal to the maximum diameter. 

There are other approximations we can choose, and this is one place to start. 

It's straightforward, and can always be extended.

