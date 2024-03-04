import bpy

# Custom update callback unecessary, as numbers are computed on the fly
class PLATFORM_PlatformPanelProps(bpy.types.PropertyGroup):
    # Static methods were used.
    # Another choice is to make global functions.
    # Yet another option is to use the functions directly inside the draw method
    # A cache feature, together with an update on prop modification can be used,
    # but the computation cost is negligible
    @staticmethod
    def ntot(context):
        return len(context.scene.platform_panel_props)

    @staticmethod
    def nred(context):
        return len(
                    [
                        prop
                        for prop in context.scene.platform_panel_props
                        if prop.side == "platform_red"
                    ]
                )

    @staticmethod
    def nblue(context):
        return len(
                    [
                        prop
                        for prop in context.scene.platform_panel_props
                        if prop.side == "platform_blue"
                    ]
                )

    side: bpy.props.EnumProperty(
        name = "Side",
        description = "Choose the platform side (either 'blue' or 'red')",
        items = [
            ("platform_blue", "Blue", "Set the platform to 'blue' side"),
            ("platform_red", "Red", "Set the platform to 'red' side")
        ],
        default = "platform_blue",
    )
    is_expanded_platform: bpy.props.BoolProperty(
        name = "Platform expand",
        description = "Expands a platform panel to show all its attributes",
        default = False,
    )
    sens_dir: bpy.props.StringProperty(
        name = "Sensors",
        description = "(Excel) file containing the sensors",
        subtype = 'DIR_PATH', # to get File Dialog instead of Folder Dialog, set subtype from DIR_PATH to FILE_PATH
    )
    sensors: bpy.props.EnumProperty(
        name = "Sensors",
        description = "Choose the set of sensors belonging to the platform",
        items = [
            ("platform_radar", "RADAR", "Place a RADAR on the platform", 0),
            ("platform_lidar", "LiDAR", "Place a LiDAR on the platform", 1),
        ],
        default = None,
    )
    eff_dir: bpy.props.StringProperty(
        name = "Effectors",
        description = "(Excel) file containing the effectors",
        subtype = 'DIR_PATH', # to get File Dialog instead of Folder Dialog, set subtype from DIR_PATH to FILE_PATH
    )
    effectors: bpy.props.EnumProperty(
        name = "Effectors",
        description = "Choose the set of effectors belonging to the platform",
        items = [
            ("platform_jammer", "Jammer", "Place a jammer on the platform", 0),
            ("platform_HPM", "HPM", "Place a HPM on the platform", 1),
        ],
        default = None,
    )