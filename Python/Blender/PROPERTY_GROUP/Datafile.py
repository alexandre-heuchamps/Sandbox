import bpy

class PLATFORM_DataFile(bpy.types.PropertyGroup):
    file : bpy.props.StringProperty(
            name="",
            description="Path to data file",
            default="",
            maxlen=1024,
            subtype='FILE_PATH',
    )