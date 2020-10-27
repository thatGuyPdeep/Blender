#Import python
import bpy

# Clear all nodes in a mat
def clear_material( material ):
    if material.node_tree:
        material.node_tree.links.clear()
        material.node_tree.nodes.clear()


# Create a node corresponding to a defined group
def instanciate_group( nodes, group_name ):
    group = nodes.new( type = 'ShaderNodeGroup' )
    group.node_tree = bpy.data.node_groups[group_name]


#ref materials  
materials = bpy.data.materials
#name material
mat_name = 'Mat_Tile'
# get ref to material
material = materials.get( mat_name )

#if not our mat
if not material:
    material = materials.new( mat_name )

# We clear it as we'll define it completely
clear_material( material )

material.use_nodes = True

nodes = material.node_tree.nodes
links = material.node_tree.links

output = nodes.new( type = 'ShaderNodeOutputMaterial' )

diffuse = nodes.new( type = 'ShaderNodeBsdfDiffuse' )

#input = nodes.new( type = 'ShaderNodeTexImage')

#With names
link = links.new( diffuse.outputs['BSDF'], output.inputs['Surface'])
#Or with indices
#link = links.new( diffuse.outputs[0], output.inputs[0] )
python
