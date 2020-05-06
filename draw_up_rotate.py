import bpy
import blf
from . up_roll_rotate_op import VIEW_OT_up_roll_rotate

class DrawUpRotate:
    def __init__(self, context, areatype):
        # self.handle = bpy.types.SpaceView3D.draw_handler_add(
        #            self.draw,(context,),
        #            'WINDOW', 'POST_PIXEL')
        
        self.areatype = areatype
        self.handle = self.create_handle(context)


    def create_handle(self, context):
        handle = self.areatype.draw_handler_add(
            self.draw_region,
            (context,),
           'WINDOW', 'POST_PIXEL')  
        return handle     

    def draw_region(self, context):
        print("drawing")
        print("context", context)
        if bpy.context.scene.up_roll_rotate_addon.up_roll_per_frame:
            VIEW_OT_up_roll_rotate.execute(self, context)
        else:
            print("nope")

    def remove_handle(self):
         bpy.types.SpaceView3D.draw_handler_remove(self.handle, 'WINDOW')
    
    def __del__(self):
        remove_handle(self)

        

context = bpy.context             
dns = bpy.app.driver_namespace

dns["drawUpRotate"] = DrawUpRotate(context, bpy.types.SpaceView3D)