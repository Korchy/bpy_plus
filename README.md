# BPY plus
BPY plus - a set of modules to extend the Blender Python API.

<img src="https://b3d.interplanety.org/wp-content/upload_content/2021/02/preview_00_1200x600-560x280.jpg"><p>

BPY plus is an Open Source project based on Blender API and extending it with several new features and making it easier to use some of "bpy" functions.

Only your Patreon support helps the project developing and extending with new modules and classes.

You can support BPY plus on <a href="https://www.patreon.com/interplanety">patreon.com/interplanety</a>

Documentation
-
See the <a href="https://b3d.interplanety.org/en/bpy-plus-2/">BPY plus web-page</a> for more info. 

Current version
-
1.8.3.

For Blender
-
2.93, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6

Usage example
-
Copy "bpy_plus" to your project directory. Now you can import "bpy_plus" modules as usual and use their functionality.

For example, let's find the bounding sphere around selected objects.

Import the "Bounding" class from the "bounding" module.

Now we can calculate the bounding sphere around the selected objects using the "sphere" method.

This method returns the location and radius of the bounding sphere. Let's add an empty with the type of sphere to the scene and set the resulting location and radius to it, to display the bounding sphere we found.

    import bpy

    from bpy_plus.bounding import Bounding
    
    b_sphere = Bounding.sphere(
        objects=bpy.context.selected_objects,
        mode='GEOMETRY'
        )
    
    empty = bpy.data.objects.new(name='empty', object_data=None)
    empty.empty_display_type = 'SPHERE'
    empty.location = b_sphere[0]
    empty.empty_display_size = b_sphere[1]
    bpy.context.collection.objects.link(object=empty)

<img src="https://b3d.interplanety.org/wp-content/upload_content/2021/02/bounding_sphere-390x315.jpg"><p>

Version history
-
[version_history](version_history.md)
