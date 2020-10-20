import bpy

Data = bpy.data
Ctx = bpy.context
Ops = bpy.ops

print('Starting')

object = Ctx.selected_objects[0]
Ctx.view_layer.objects.active = object

bpy.ops.object.editmode_toggle()

object.face_maps.active_index = 3
Ops.object.face_map_select()
