import bpy
import mathutils
import math
from math import radians

def get_follow_object(context):
    if bpy.context.scene.up_roll_rotate_addon.up_roll_select:
        return bpy.context.scene.up_roll_rotate_addon.up_roll_select
        # Set to lock object if set
    lock_object = context.space_data.lock_object
    if lock_object:
        return lock_object
    return bpy.context.active_object

def up_roll_rotate(context):
    window = context.window
    screen = window.screen
    for area in screen.areas:        
        if area.type == 'VIEW_3D':
            for region in area.regions:
                if region.type == 'WINDOW':
                    override = {'window': window, 'screen': screen, 'area': area, 'region': region}
                    region_3d = area.spaces.active.region_3d

                    # get follow object
                    roll_follow_object = get_follow_object(context)
                    object_euler = roll_follow_object.matrix_world.to_euler('XYZ')
                    
                    rotation_euler = region_3d.view_rotation.copy().to_euler()
                    # subtract object rotation
                    rotation_invert = object_euler.copy().to_quaternion()
                    rotation_invert.invert()
                    rotation_euler.rotate(rotation_invert)
                    
                    # if past 90 or -90 do 180 else 0
                    if rotation_euler.y < math.radians(-90) or rotation_euler.y > math.radians(90):
                        rotation_euler.y = math.radians(180)
                    else:
                        rotation_euler.y = math.radians(0)
                    rotation_euler.rotate(object_euler)  
                    region_3d.view_rotation = rotation_euler.to_quaternion()
                    # print(rotation_euler.y)
                    break