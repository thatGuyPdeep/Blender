bl_info = {
    "name" : "Object Adder",
    "author" : "Prabhakar",
    "version" : (1,0),
    "blender" : (2,90,0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh"
}




import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Add an object", icon= 'OBJECT_ORIGIN')
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon = 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_ico_sphere_add", icon= 'MESH_ICOSPHERE')
        row = layout.row()
        row.operator("mesh.primitive_circle_add", icon = 'MESH_CIRCLE')
        row = layout.row()
        row.operator("object.text_add", icon = 'TEXT')
        


class NewPanel(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_NewPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    bl_parent_id = 'PT_TestPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Select a Special Options", icon= 'COLOR_BLUE')
        row = layout.row()
        row.operator("object.shade_smooth", icon = 'MOD_SMOOTH', text = "Set Smooth Shading")
        row = layout.row()
        row.operator("object.subdivision_set")
        row = layout.row()
        row.operator("object.modifier_add")



class NewPanelZ(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_NewPanelZ"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    bl_parent_id = 'PT_TestPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text= "Select an object to scale your object.", icon= 'FONT_DATA')
        row = layout.row()
        row.operator('transform.resize')
        row = layout.row()
        layout.scale_y = 1
        
        col = layout.column()
        col.prop(obj, "scale")
        


def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(NewPanel)
    bpy.utils.register_class(NewPanelZ)

def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(NewPanel)
    bpy.utils.unregister_class(NewPanelZ)



if __name__ == "__main__":
    register()