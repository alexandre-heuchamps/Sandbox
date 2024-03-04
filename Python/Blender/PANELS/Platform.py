import bpy
from ..PROPERTY_GROUP.PlatformPanelProps import PLATFORM_PlatformPanelProps

class PLATFORM_PT_Platform(bpy.types.Panel):
    bl_idname = 'PLATFORM_PT_Platform'
    bl_label = 'Platforms'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'platform'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scn = context.scene

        box = layout.box()
        row = box.row(align = True)
        row.prop(scn.eff_file, "path", text = "Effector")

        box = layout.box()
        row = box.row(align = True)
        row.label(text = f"Red {PLATFORM_PlatformPanelProps.nred(context)}")
        row.label(text = f"Blue {PLATFORM_PlatformPanelProps.nblue(context)}")
        row.label(text = f"Total {PLATFORM_PlatformPanelProps.ntot(context)}")

        box.operator('platform.add_platform', text = "Add")

        # Iterate over the properties and keep the index for the "Delete" button
        for i, prop in enumerate(context.scene.platform_panel_props):
            row = layout.row()
            icon = 'TRIA_RIGHT' if not prop.is_expanded_platform else 'TRIA_DOWN'
            row.prop(prop, 'is_expanded_platform', icon = icon, icon_only = True)
            row.label(text = f'Platform {i + 1}')
            row.alert = True
            row.operator('platform.delete_platform', text = "Delete").index = i

            if prop.is_expanded_platform:
                # Show the side that the platform belongs to
                box = layout.box()
                split = box.split(factor = 0.25)
                c1, c2 = (split.column(), split.column())
                c1.label(text = "Side")
                r = c2.row(align = True)
                r.prop(prop, "side", expand = True)

                # Show the list of sensors
                split = box.split(factor = 0.25)
                c1, c2 = (split.column(), split.column())
                r = c2.row(align = True)
                r.prop(prop, "sensors")

                # Show the list of effectors
                split = box.split(factor = 0.25)
                c1, c2 = (split.column(), split.column())
                r = c2.row(align = True)
                r.prop(prop, "effectors")