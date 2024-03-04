import bpy
from .PROPERTY_GROUP.Datafile import PLATFORM_DataFile
from .PROPERTY_GROUP.PlatformPanelProps import PLATFORM_PlatformPanelProps
from .PANELS.Platform import PLATFORM_PT_Platform
from .OPERATORS.AddPlatform import PLATFORM_OT_AddPlatform
from .OPERATORS.DeletePlatform import PLATFORM_OT_DeletePlatform
# import bpy
# from PROPERTY_GROUP.Datafile import PLATFORM_DataFile
# from PROPERTY_GROUP.PlatformPanelProps import PLATFORM_PlatformPanelProps
# from PANELS.Platform import PLATFORM_PT_Platform
# from OPERATORS.AddPlatform import PLATFORM_OT_AddPlatform
# from OPERATORS.DeletePlatform import PLATFORM_OT_DeletePlatform

__all__ = ["PLATFORM_DataFile",
            "PLATFORM_PlatformPanelProps",
            "PLATFORM_PT_Platform",
            "PLATFORM_PT_Platform",
            "PLATFORM_OT_AddPlatform",
            "PLATFORM_OT_DeletePlatform",]

def register():
    for my_class in __all__:
        bpy.utils.register_class(my_class)
    bpy.types.Scene.eff_file = bpy.props.PointerProperty(type=PLATFORM_DataFile)
    bpy.types.Scene.platform_panel_props = bpy.props.CollectionProperty(
                                                type = PLATFORM_PlatformPanelProps,
                                            )

def unregister():
    for my_class in __all__:
        bpy.utils.unregister_class(my_class)
    del bpy.types.Scene.eff_file

if __name__ == '__main__':
    register()