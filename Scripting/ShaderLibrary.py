bl_info = {
    "name" : "Object Adder",
    "author" : "Prabhakar",
    "version" : (1,0),
    "blender" : (2,90,0),
    "location" : "View3d > Tool",
    "description" : "Add shader to the object",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Shader",
}


import bpy

    #Create Shader Panel to add shader to object(mesh or text)
class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "Shader_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shader Library"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Select the shader to add.")
        row.operator('shader.diamond_operator')
        
        
    #Create the Custom operator for the Diamond Shader
class SHADER_TO_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = 'shader.diamond_operator'        
    
    def execute(self, context):
        
            #Creating the shader named "Diamond"
        material_diamond = bpy.data.materials.new(name = "Diamond")
            #Enabling use nodes
        material_diamond.use_nodes = True
            #Adding Principle BSDF
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
            #Creating refrence to material output
        material_output = material_diamond.node_tree.nodes.get('Material Output')
            #Set Location for node
        material_output.location = (750,300)
        
        
            #Adding glass1 node
        glass1_node = material_diamond.node_tree.nodes.new(type= "ShaderNodeBsdfGlass")
            #Set location for node
        glass1_node.location = (90,420)
            #Settinng default color
        glass1_node.inputs[0].default_value = (1, 0, 0, 1)
            #Setting default IOR Value
        glass1_node.inputs[2].default_value = 1.4
        
        
        
            #Adding glass2 node
        glass2_node = material_diamond.node_tree.nodes.new(type= "ShaderNodeBsdfGlass")
            #Set location for node
        glass2_node.location = (90,230)
            #Settinng default color
        glass2_node.inputs[0].default_value = (0, 1, 0, 1)
            #Setting default IOR Value
        glass2_node.inputs[2].default_value = 1.5
        
        
        
            #Adding glass3 node
        glass3_node = material_diamond.node_tree.nodes.new(type= "ShaderNodeBsdfGlass")
            #Set location for node
        glass3_node.location = (90,40)
            #Settinng default color
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)
            #Setting default IOR Value
        glass3_node.inputs[2].default_value = 1.6
        
           #Adding glass4 node
        glass4_node = material_diamond.node_tree.nodes.new(type= "ShaderNodeBsdfGlass")
            #Set location for node
        glass4_node.location = (380,220)
            #Settinng default color
        glass4_node.inputs[0].default_value = (1, 1, 1, 1)
            #Setting default IOR Value
        glass4_node.inputs[2].default_value = 1.7
        
        
        
            #Add Add_Shader node and refrence it as 'add1'
        add1_node = material_diamond.node_tree.nodes.new(type= "ShaderNodeAddShader")
            #Set Location for the node
        add1_node.location = (250,350)
            #Setting the label
        add1_node.label = "Add 1"
            #Minimising the shader
        add1_node.hide = True
            #Deselect the node
        add1_node.select = False
        
        
        
            #Add Add_Shader node and refrence it as 'add2'
        add2_node = material_diamond.node_tree.nodes.new(type= "ShaderNodeAddShader")
            #Set Location for the node
        add2_node.location = (400,320)
            #Setting the label
        add2_node.label = "Add 2"
            #Minimising the shader
        add2_node.hide = True
            #Deselect the node
        add2_node.select = False
        
        
        
            #Creating Mix_Shader node refrence as mix_node
        mix_node = material_diamond.node_tree.nodes.new(type= "ShaderNodeMixShader")
            #Setting the location
        mix_node.location = (570,300)
            #Deselect the node
        mix_node.select = False
        
        
        
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix_node.inputs[1])
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix_node.inputs[2])
        material_diamond.node_tree.links.new(mix_node.outputs[0], material_output.inputs[0])
        
        
        bpy.context.object.active_material = material_diamond
        
        return{'FINISHED'}

        
        

def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(SHADER_TO_DIAMOND)
    


def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(SHADER_TO_DIAMOND)


if __name__ == "__main__":
    register()