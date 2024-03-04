import bpy

class PLATFORM_OT_AddPlatform(bpy.types.Operator):
    """ Create a new platform with its sensor(s) and/or effector(s) """
    bl_idname = "platform.add_platform"
    bl_label = "Create new platform"

    def execute(self, context):
        context.scene.platform_panel_props.add()
        return {'FINISHED'}