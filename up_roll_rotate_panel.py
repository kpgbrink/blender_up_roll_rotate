import bpy

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
        row.operator('view.up_roll_rotate', text="Fix Up Roll")

        layout.use_property_split = True

        layout.use_property_decorate = False  # No animation.

        view = context.space_data

        col = layout.column(align=True)
        subcol = col.column()
        subcol.active = bool(view.region_3d.view_perspective != 'CAMERA' or view.region_quadviews)

        subcol.prop(view, "lock_object")

        props = self.layout.operator('view.up_roll_rotate')
        props.my_string = "test"
        print(props.my_string)
        subcol2 = col.column()
        subcol2.active = bool(view.region_3d.view_perspective != 'CAMERA' or view.region_quadviews)
        subcol2.prop(bpy.context.scene, "my_addon")

        # subcol.prop(props, "my_pointer")

         # You can set the property values that should be used when the user
        # presses the button in the UI.
        # self.my_bool = True
        # self.my_string = "Shouldn't that be 47?"

        # You can set properties dynamically:
        # if context.object:
        #     self.my_float = context.object.location.x
        # else:
        #     self.my_float = 327
        # selt.my_object_select_string
        

        # layout.prop_search(self, "my_object_select_string", scene, "objects")

        # import sys
        # prefs = context.preferences
        # inputs = prefs.inputs
        # view = prefs.view

        # flow = layout.grid_flow(row_major=False, columns=0, even_columns=True, even_rows=False, align=False)

        # flow.row().prop(inputs, "view_rotate_method", expand=True)
        # if inputs.view_rotate_method == 'TURNTABLE':
        #     flow.prop(inputs, "view_rotate_sensitivity_turntable")
        # else:
        #     flow.prop(inputs, "view_rotate_sensitivity_trackball")

        # flow.prop(inputs, "use_rotate_around_active")
        # flow.prop(inputs, "use_auto_perspective")
        # flow.prop(inputs, "use_mouse_depth_navigate")
        # if sys.platform == "darwin":
        #     flow.prop(inputs, "use_trackpad_natural", text="Natural Trackpad Direction")

        # flow.separator()

        # flow.prop(view, "smooth_view")
        # flow.prop(view, "rotation_angle")
        # if lock_object:
        #     if lock_object.type == 'ARMATURE':
        #         subcol.prop_search(
        #             view, "lock_bone", lock_object.data,
        #             "edit_bones" if lock_object.mode == 'EDIT'
        #             else "bones",
        #             text="",
        #         )
        # else:
        #     subcol.prop(view, "lock_cursor", text="Lock to 3D Cursor")
        
# def register():
#     bpy.utils.register_module(__name__)
#     bpy.types.Scene.theChosenObject = bpy.props.StringProperty()
#     print('register the panel kris')

# def unregister():
#     bpy.utils.unregister_module(__name__)
#     del bpy.types.Object.theChosenObject
#     print('unregister the panel kris')

# if __name__ == "__main__":
#     register()



# This stuff doesn't do anything

class USERPREF_PT_navigation_orbit(UPROLLROTATE_PT_panel, bpy.types.Panel):
    bl_label = "Orbit & Pan"

    def draw_centered(self, context, layout):
        import sys
        prefs = context.preferences
        inputs = prefs.inputs
        view = prefs.view

        flow = layout.grid_flow(row_major=False, columns=0, even_columns=True, even_rows=False, align=False)

        flow.row().prop(inputs, "view_rotate_method", expand=True)
        if inputs.view_rotate_method == 'TURNTABLE':
            flow.prop(inputs, "view_rotate_sensitivity_turntable")
        else:
            flow.prop(inputs, "view_rotate_sensitivity_trackball")

        flow.prop(inputs, "use_rotate_around_active")
        flow.prop(inputs, "use_auto_perspective")
        flow.prop(inputs, "use_mouse_depth_navigate")
        if sys.platform == "darwin":
            flow.prop(inputs, "use_trackpad_natural", text="Natural Trackpad Direction")

        flow.separator()

        flow.prop(view, "smooth_view")
        flow.prop(view, "rotation_angle")

# def register():
#     bpy.utils.register_class(UPROLLROTATE_PT_panel)
#     # bpy.types.Scene.show_options_01 = bpy.props.BoolProperty(name='Show 1st panel', default=False)
#     bpy.types.Scene.theChosenObject = bpy.props.StringProperty()

# def unregister():
#     # del bpy.types.Scene.show_options_01
#     bpy.utils.unregister_class(UPROLLROTATE_PT_panel)
#     del bpy.types.Object.theChosenObject

# if __name__ == "__main__":
#     register()