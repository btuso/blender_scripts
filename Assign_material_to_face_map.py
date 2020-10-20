import bpy

Data = bpy.data
Ctx = bpy.context
Ops = bpy.ops

print('Starting')

object = Ctx.selected_objects[0]
material = Data.materials['WhiteOld']

Ctx.view_layer.objects.active = object
bpy.ops.object.editmode_toggle()
object.face_maps.active_index = 1
Ops.object.face_map_select()

# First material will be applied to all faces
defaultMat = bpy.data.materials.new(name='DefaultMat')
object.data.materials.append(defaultMat)

object.data.materials.append(material)

object.active_material_index = 1
bpy.ops.object.material_slot_assign()
