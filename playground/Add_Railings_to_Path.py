import bpy
import math

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
    fence_length = fence.dimensions.x
    path_length = 0
    if path.data.splines[0].type == 'POLY':
        # Non poly curve length should be calculated in another way
        path_length = max(path.dimensions.x, path.dimensions.y)
    position = path.matrix_world @ fence.location
    Ops.transform.translate(value=position)
    

    remainder = path_length % fence_length
    divisions = math.floor(path_length / fence_length)
    Ctx.view_layer.objects.active = fence    
    
    scale = 1.0
    if remainder / fence_length >= 0.5:
        scale = (path_length / (divisions + 1)) / fence_length 
    else:
        scale =  (path_length / divisions) / fence_length

    Ops.transform.resize(value=(scale,1.0, 1.0))
    Ops.object.transform_apply(location=False, rotation=False, scale=True, properties=False)

    Ops.object.modifier_add(type='ARRAY')
    Ctx.object.modifiers['Array'].fit_type = 'FIT_LENGTH'
    Ctx.object.modifiers['Array'].fit_length = path_length - 0.001
    
    Ops.object.modifier_add(type='CURVE')
    Ctx.object.modifiers['Curve'].object = path
