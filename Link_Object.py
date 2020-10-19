import bpy

Data = bpy.data
Ctx = bpy.context
Ops = bpy.ops

FILE_NAME = 'Floor'
FILE_PATH = 'pieces\\simple_unit.blend'

print('Starting')

Ops.wm.link(
    filename=FILE_NAME,
    directory= bpy.path.abspath('//' + FILE_PATH + '\\Object\\')
    )
