import bpy

Data = bpy.data
Ctx = bpy.context
Ops = bpy.ops

def load_material(material):
    file_path = '..\\materials\\building.blend'
    Ops.wm.link(
        filename=material,
        directory= bpy.path.abspath('//' + file_path + '\\Material\\')
        )

def load_unit():
    file_name = 'Unit'
    file_path = '..\\pieces\\simple_unit.blend'
    Ops.wm.append(
        filename=file_name,
        directory= bpy.path.abspath('//' + file_path + '\\Object\\')
        )
    
print('Starting')

materials = ['White_Old', 'Brown_Dark_Tiles', 'Brown_Light_Tiles']
for material in materials:
    load_material(material)
defaultMat = bpy.data.materials.new(name='DefaultMat')

    
load_unit()
object = Ctx.selected_objects[0]
Ctx.view_layer.objects.active = object
bpy.ops.object.editmode_toggle()
object.data.materials.append(defaultMat)

face_map_materials = {
    "Main_1": "Brown_Dark_Tiles",
    "Main_2": "White_Old",
    "Accent_1": "Brown_Light_Tiles"    
}

for face_map, material in face_map_materials.items():
    Ops.mesh.select_all(action = 'DESELECT')
    face_map_index = object.face_maps.find(face_map)
    object.face_maps.active_index = face_map_index
    Ops.object.face_map_select()
    
    material_data = Data.materials[material]
    object.data.materials.append(material_data)
    material_index = object.material_slots.find(material)
    object.active_material_index = material_index
    Ops.object.material_slot_assign()
