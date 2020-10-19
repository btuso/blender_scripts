import bpy

Data = bpy.data
Ctx = bpy.context
Ops = bpy.ops


def load_unit():
    FILE_NAME = 'Unit'
    FILE_PATH = 'pieces\\simple_unit.blend'
    Ops.wm.append(
        filename=FILE_NAME,
        directory= bpy.path.abspath('//' + FILE_PATH + '\\Object\\'),
        )


def get_balcony_attach():
    GROUP_NAME = 'Balcony_Attach'

    object = Ctx.selected_objects[0]
    vertex_group = object.vertex_groups[GROUP_NAME]

    verticesInGroup = [ v for v in object.data.vertices if vertex_group.index in [ vg.group for vg in v.groups ] ]
    attachVertex = verticesInGroup[0]
    attachGlobalPosition = object.matrix_world @ attachVertex.co
    return attachGlobalPosition

def load_balcony():
    FILE_NAME = 'Balcony'
    FILE_PATH = 'pieces\\simple_balcony.blend'
    Ops.wm.append(
        filename=FILE_NAME,
        directory= bpy.path.abspath('//' + FILE_PATH + '\\Object\\'),
        )

def attach_balcony(balcony, attach_coord):
    Ops.transform.translate(value=attach_coord)
    
def create_floor(floor_nr):
    load_unit()
    height_offset = Ctx.selected_objects[0].dimensions[2]
    Ops.transform.translate(value=(0, 0, height_offset * floor_nr))
    attach_point = get_balcony_attach()
    load_balcony()
    attach_balcony(Ctx.selected_objects[0], attach_point)    


print('Starting')
FLOORS = 10
for i in range(FLOORS):
    create_floor(i)
