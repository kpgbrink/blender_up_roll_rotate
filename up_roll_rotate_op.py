import bpy
import mathutils
import math
from math import radians
from . up_roll_rotate import up_roll_rotate

class VIEW_OT_up_roll_rotate(bpy.types.Operator):
    bl_idname = "view.up_roll_rotate"
    bl_label = "Fix Up Roll"
    bl_description = "Up rolls the view"
  
    def execute(self, context):
        up_roll_rotate(context)
        return {'FINISHED'}