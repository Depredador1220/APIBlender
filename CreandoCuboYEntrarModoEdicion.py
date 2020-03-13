import bpy
import bmesh

#Debemos estar en modo objeto, fallara si la escena esta vacia
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#Creamos un cubo y entramos al modo edicion
bpy.ops.mesh.primitive_cube_add(radius=1, location=(0, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')

#Almacena una referencia al mesh datablock
mesh_datablock = bpy.context.object.data

#Creamos un objetos bmesh llamado bm para usarlo
bm = bmesh.from_edit_mesh(mesh_datablock)

#Imprime el objeto bmesh
print(bm)
