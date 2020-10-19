import bpy

Data = bpy.data
Ctx = bpy.context
Ops = bpy.ops

FILE_NAME = 'Unit'
FILE_PATH = 'pieces\\simple_unit.blend'

GROUP_NAME = 'Balcony_Attach'

print('Starting')

Ops.wm.append(
    filename=FILE_NAME,
    directory= bpy.path.abspath('//' + FILE_PATH + '\\Object\\'),
    )


object = Ctx.selected_objects[0]
vertex_group = object.vertex_groups[GROUP_NAME]

verticesInGroup = [ v for v in object.data.vertices if vertex_group.index in [ vg.group for vg in v.groups ] ]
attachVertex = verticesInGroup[0]
attachGlobalPosition = object.matrix_world @ attachVertex.co

print(attachGlobalPosition)
