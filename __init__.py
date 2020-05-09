# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "uprotate",
    "author" : "Kristofer Brink",
    "description" : "Addon for fixing roll of camera to follow objects.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . up_roll_rotate_op import VIEW_OT_up_roll_rotate
from . up_roll_rotate_panel import UPROLLROTATE_PT_panel
# from . draw_up_rotate import DrawUpRotate
from . draw_handler_up_roll_rotate_op import VIEW_OT_draw_handler_up_roll_rotate

# bpy.types.Scene.up_roll_rotate_selected_object = bpy.props.PointerProperty(name="Object to use for up roll rotate", type=bpy.types.Object)

class UpRotateAddonProperties(bpy.types.PropertyGroup):
    up_roll_per_frame: bpy.props.BoolProperty(name="Toggle Up Roll")
    up_roll_select: bpy.props.PointerProperty(name="Up Roll Rotate", type=bpy.types.Object)

bpy.utils.register_class(UpRotateAddonProperties)
bpy.types.Scene.up_roll_rotate_addon = bpy.props.PointerProperty(type=UpRotateAddonProperties)

classes = (VIEW_OT_up_roll_rotate, UPROLLROTATE_PT_panel, VIEW_OT_draw_handler_up_roll_rotate)

register, unregister = bpy.utils.register_classes_factory(classes)