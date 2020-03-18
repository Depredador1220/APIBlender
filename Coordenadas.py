import ut
import importlib
importlib.reload(ut)

import bpy

#Fallara si la escena esta vacia
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(0, 0, 0))
bpy.context.object.name = 'Cube-1'

print('\n\n\n')
print('***********************************DEPREDADOR1220***********************************')

#Verifico las coordenadas global y las coordenadas locales
print('\nCOORDENADAS GLOBALES Y LOCALES')
print('\nAntes de la transformacion:')
print('Global:', ut.coords('Cube-1', 'GLOBAL')[0:2])
print('Local:', ut.coords('Cube-1', 'LOCAL')[0:2])

#Muevo a lo largo de x y z y veo el cubo moverse por el espacio 3D
bpy.ops.transform.translate(value = (3, 3, 3))

#Verifico las coordenadas globales y locales nuevamente
print('\nDespues de la transformacion: Aun no aplicada')
print('Global:', ut.coords('Cube-1', 'GLOBAL')[0:2])
print('Local:', ut.coords('Cube-1', 'LOCAL')[0:2])

#Aplicando la transformacion, nada cambia en el espacio 3D
ut.sel.transform_apply()

#Vetifico las coordenadas globales y locales otra vez
print('\nDespues de la transformacion: Aplicada')
print('Global:', ut.coords('Cube-1', 'GLOBAL')[0:2])
print('Local:', ut.coords('Cube-1', 'LOCAL')[0:2])
print('\n')
print('***********************************DEPREDADOR1220***********************************')
print('\n\n\n')
