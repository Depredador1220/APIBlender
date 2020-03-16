import bpy
import bmesh

#Debo empezar en el modo edicion
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#Creo un cubo y le roto una de sus caras en el eje y
bpy.ops.mesh.primitive_cube_add(radius=0-5, location=(-3, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")

#Establezco a modo cara o face para las transformaciones.
bpy.ops.mesh.select_mode(type = "FACE")

bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.faces.ensure_lookup_table()
bm.faces[1].select = True
bpy.ops.transform.rotate(value = 0.3, axis = (0, 1, 0))

bpy.ops.object.mode_set(mode='OBJECT')

#Creo un cubo y lo muevo una unidad de eje a lo largo del eje y
bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(0, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")

bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.edges.ensure_lookup_table()
bm.edges[4].select = True
bpy.ops.transform.translate(value = (0, 0.5, 0))

bpy.ops.object.mode_set(mode='OBJECT')

#Creo un cubo y lo muevo una unidad de vertice a lo largo de los ejes x y y
#Creo un cubo y lo muevo una unidad de eje a lo largo del eje y
bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(3, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")

bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.verts.ensure_lookup_table()
bm.verts[3].select = True
bpy.ops.transform.translate(value = (0, 1, 1))

bpy.ops.object.mode_set(mode='OBJECT')
