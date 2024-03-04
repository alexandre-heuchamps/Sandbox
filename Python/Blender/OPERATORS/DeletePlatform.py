import bpy

class PLATFORM_OT_DeletePlatform(bpy.types.Operator):
    """ Delete a platform with its sensor(s) and/or effector(s) """
    bl_idname = "platform.delete_platform"
    bl_label = "Delete platform"

    # Index so that a specific item can be deleted from the list
    index: bpy.props.IntProperty()

    def execute(self, context):
        context.scene.platform_panel_props.remove(self.index)
        return {'FINISHED'}