import bpy

class Up_Roll_Rotate_Panel(bpy.types.Panel):
    bl_idname = "Up_Roll_Rotate_Panel"
    bl_label = "Up Roll Rotate Panel"
    bl_category = "Up Roll Rotate"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('view.region_3d_roll', text="Fix Up Roll")