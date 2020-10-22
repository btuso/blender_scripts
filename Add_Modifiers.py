import bpy

Data = bpy.data
Ctx = bpy.context
Ops = bpy.ops

PATHS = 'Paths'

def load_fence():
    FILE_NAME = 'Fence_long'
    FILE_PATH = '..\\pieces\\fence.blend'
    Ops.wm.append(
        filename=FILE_NAME,
        directory= bpy.path.abspath('//' + FILE_PATH + '\\Object\\'),
        )
        
def load_railing_paths():
    FILE_NAME = PATHS
    FILE_PATH = '..\\pieces\\simple_balcony.blend'
    Ops.wm.append(
        filename=FILE_NAME,
        directory= bpy.path.abspath('//' + FILE_PATH + '\\Collection\\'),
        )

print('Starting')
load_railing_paths()

for path in Data.collections[PATHS].objects:
    load_fence()    
    fence = Ctx.selected_objects[0]
    position = path.matrix_world @ fence.location
    Ops.transform.translate(value=position)
    
    Ctx.view_layer.objects.active = fence
    Ops.object.modifier_add(type='ARRAY')
    Ctx.object.modifiers['Array'].fit_type = 'FIT_CURVE'
    Ctx.object.modifiers['Array'].curve = path
    
    Ops.object.modifier_add(type='CURVE')
    Ctx.object.modifiers['Curve'].object = path
