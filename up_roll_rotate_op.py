import bpy
import mathutils
import math
from math import radians

class Up_Roll_Rotate_Operator(bpy.types.Operator):
    bl_idname = "view.region_3d_roll"
    bl_label = "Up roll rotate"
    bl_description = "Up rolls the view"

    def execute(self, context):
        window = context.window
        screen = window.screen
        for area in screen.areas:        
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'window': window, 'screen': screen, 'area': area, 'region': region}
                        region_3d = area.spaces.active.region_3d
                        active_object = bpy.context.active_object
                        
                        rotation_euler = region_3d.view_rotation.copy().to_euler()
                        object_euler = active_object.rotation_euler.copy()
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
                        break
        return {'FINISHED'}