import bpy
from . up_roll_rotate_op import VIEW_OT_up_roll_rotate

class VIEW_OT_draw_handler_up_roll_rotate(bpy.types.Operator):
    bl_idname = "view.draw_handler_up_roll_rotate"
    bl_label = "Constant Draw Up Roll"
    bl_description = "Up rolls the view constantly"

    def draw_region(self, context):
        if bpy.context.scene.up_roll_rotate_addon.up_roll_per_frame:
            VIEW_OT_up_roll_rotate.execute(self, context)
  
    def execute(self, context):
        print("do while drawing")
        try:
            if self.handler_up_roll:
                bpy.types.SpaceView3D.draw_handler_remove(
                self.handler_up_roll,
                (context,),
                'WINDOW')
                self.handler_up_roll = None
        except AttributeError:
            print('making new')
        self.handler_up_roll = bpy.types.SpaceView3D.draw_handler_add(
            self.draw_region,
            (context,),
            'WINDOW', 'POST_VIEW')
        return {'FINISHED'}