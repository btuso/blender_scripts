import bpy
import math
import mathutils

Data = bpy.data
Ctx = bpy.context
Ops = bpy.ops

PATHS = 'Paths'

def load_corner():
    FILE_NAME = 'Corner'
    FILE_PATH = '..\\pieces\\simple_window.blend'
    Ops.wm.append(
        filename=FILE_NAME,
        directory= bpy.path.abspath('//' + FILE_PATH + '\\Object\\'),
        )
    return Ctx.selected_objects[0]
        
def load_frame():
    FILE_NAME = 'Filler'
    FILE_PATH = '..\\pieces\\simple_window.blend'
    Ops.wm.append(
        filename=FILE_NAME,
        directory= bpy.path.abspath('//' + FILE_PATH + '\\Object\\'),
        )
    return Ctx.selected_objects[0]

def load_glass():
    FILE_NAME = 'Glass'
    FILE_PATH = '..\\pieces\\simple_window.blend'
    Ops.wm.append(
        filename=FILE_NAME,
        directory= bpy.path.abspath('//' + FILE_PATH + '\\Object\\'),
        )
    return Ctx.selected_objects[0]

print('Starting')

def create_window_piece(origin, length, rotation):
    corner = load_corner()
    frame = load_frame()    
    frame_scale = (length - corner.dimensions.x * 2) / frame.dimensions.x
    Ops.transform.resize(value=(frame_scale,1.0, 1.0))
    Ops.object.transform_apply(location=False, rotation=False, scale=True, properties=False)
    frame_position = corner.matrix_world @ frame.location
    frame_position.x += corner.dimensions.x
    Ops.transform.translate(value=frame_position)
    corner.select_set(True)
    Ctx.view_layer.objects.active = corner
    Ops.object.join()
    Ops.transform.translate(value=origin)
    Ops.transform.rotate(value=rotation, orient_axis='Y')
    Ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False)
    return corner
    
def path_length(path):
    path_length = 0
    if path.data.splines[0].type == 'POLY':
        path_length = max(path.dimensions)
    else:
        raise Exception('Non poly paths not supported')
    return path_length

vertical = Data.collections[PATHS].objects['Vertical']
horizontal = Data.collections[PATHS].objects['Horizontal']

# lower left
lower_left = create_window_piece(horizontal.location, path_length(horizontal), 0)
# lower right
lower_right_pos = horizontal.location + mathutils.Vector((path_length(horizontal), 0, 0))
lower_right = create_window_piece(lower_right_pos, path_length(vertical), math.radians(90))
# upper right
upper_right_pos = horizontal.location + mathutils.Vector((path_length(horizontal), 0, path_length(vertical)))
upper_right = create_window_piece(upper_right_pos, path_length(horizontal), math.radians(180))
# upper left
upper_left_pos = horizontal.location + mathutils.Vector((0, 0, path_length(vertical)))
upper_left = create_window_piece(upper_left_pos, path_length(vertical), math.radians(270))

# join them
lower_left.select_set(True)
lower_right.select_set(True)
upper_right.select_set(True)
upper_left.select_set(True)
Ctx.view_layer.objects.active = lower_left
Ops.object.join()


# add glass
window_frame = Ctx.selected_objects[0]
vertex_group = window_frame.vertex_groups['windowpane_attach']
attach_coords = [ v.co for v in window_frame.data.vertices if vertex_group.index in [ vg.group for vg in v.groups ] ]
ll_attach_point = min(attach_coords)
ur_attach_point = max(attach_coords)

glass = load_glass()
scale_x = (ur_attach_point.x - ll_attach_point.x) / glass.dimensions.x
scale_z = (ur_attach_point.z - ll_attach_point.z) / glass.dimensions.z
Ops.transform.resize(value=(scale_x,1.0, scale_z))
Ops.object.transform_apply(location=False, rotation=False, scale=True, properties=False)
attachGlobalPosition = window_frame.matrix_world @ ll_attach_point
Ops.transform.translate(value=attachGlobalPosition)

glass.select_set(True)
window_frame.select_set(True)
Ctx.view_layer.objects.active = window_frame
Ops.object.join()
