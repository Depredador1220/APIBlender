import bpy
import bmesh

#Debo empezar en el modo objeto
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#Creo un cubo y entro al modo edicion
bpy.ops.mesh.primitive_cube_add(radius=1,location=(0, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')

#Establezco al modo Face para una visualizacion mas facil
bpy.ops.mesh.select_mode(type="FACE")

#Registro el objecto bmesh y selecciono varias partes
bm = bmesh.from_edit_mesh(bpy.context.object.data)

#Deselecciono todos los vertices, ejes y caras
bpy.ops.mesh.select_all(action="DESELECT")

#Selecciono una cara
bm.faces.ensure_lookup_table()
bm.faces[0].select = True

#Selecciono un eje
bm.edges.ensure_lookup_table()
bm.edges[7].select = True

#Selecciono un vertice
bm.verts.ensure_lookup_table()
bm.verts[5].select = True
