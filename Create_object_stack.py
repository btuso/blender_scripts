import bpy

FLOORS = 10

D = bpy.data
C = bpy.context
O = bpy.ops

print('Starting')

selected_objects = C.selected_objects
print('Executing for {}'.format(selected_objects))

height_offset = selected_objects[0].dimensions[2]

for i in range(FLOORS):
    O.object.duplicate_move(False, TRANSFORM_OT_translate={"value": (0, 0, height_offset)})
