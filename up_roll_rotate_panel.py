import bpy
import sys

class UPROLLROTATE_PT_panel(bpy.types.Panel):
    bl_idname = "UPROLLROTATE_PT_panel"
    bl_label = "Up Roll Rotate Panel"
    bl_category = "Up Roll Rotate"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.prop(bpy.context.scene.up_roll_rotate_addon, "up_roll_per_frame")
        row.operator('view.draw_handler_up_roll_rotate', text="Constant Fix Up Roll")

        row = layout.row()
        row.operator('view.up_roll_rotate', text="Fix Up Roll")

        layout.use_property_split = True

        layout.use_property_decorate = False  # No animation.

        view = context.space_data

        col = layout.column(align=True)
        subcol = col.column()
        subcol.active = bool(view.region_3d.view_perspective != 'CAMERA' or view.region_quadviews)
        subcol.prop(view, "lock_object")
        
        subcol2 = col.column()
        subcol2.active = bool(view.region_3d.view_perspective != 'CAMERA' or view.region_quadviews)
        subcol2.prop(bpy.context.scene.up_roll_rotate_addon, "up_roll_select")

        # switch turntable/trackball
        prefs = context.preferences
        inputs = prefs.inputs
        view = prefs.view

        flow = layout.grid_flow(row_major=False, columns=0, even_columns=True, even_rows=False, align=False)

        flow.row().prop(inputs, "view_rotate_method", expand=True)
        
        if inputs.view_rotate_method == 'TURNTABLE':
            flow.prop(inputs, "view_rotate_sensitivity_turntable")
        else:
            flow.prop(inputs, "view_rotate_sensitivity_trackball")