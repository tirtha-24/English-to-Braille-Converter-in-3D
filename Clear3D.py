import bpy

# select 3D model, delete, save
bpy.ops.object.select_by_layer()
bpy.ops.object.delete(use_global=False)
bpy.ops.wm.save_as_mainfile()
