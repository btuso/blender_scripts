import bpy

Data = bpy.data
Ctx = bpy.context
Ops = bpy.ops

FILE_NAME = 'WhiteOld'
FILE_PATH = 'materials\\white_old.blend'

print('Starting')

Ops.wm.link(
    filename=FILE_NAME,
    directory= bpy.path.abspath('//' + FILE_PATH + '\\Material\\')
    )

material = Data.materials[FILE_NAME]

object = Ctx.active_object
object.data.materials[0] = material
