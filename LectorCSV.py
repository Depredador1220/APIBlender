#Declaracion de librerias
import bpy
import csv
import urllib.request

class act:
    """Clase para controlar los objetos activos"""

    def location(v):
        bpy.context.object.location = v

    def scale(v):
        bpy.context.object.scale = v

    def rotation(v):
        bpy.context.object.rotation_euler = v

    def rename(objName):
        bpy.context.object.name = objName

class create:
        """Clase para crear objetos primitivos personalizados"""
        
        def cube(objName):
            bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(0, 0, 0))
            act.rename(objName)

        def sphere(objName):
            bpy.ops.mesh.primitive_uv_sphere_add(size=0.5, location=(0, 0, 0))
            act.rename(objName)

        def cone(objName):
            bpy.ops.mesh.primitive_cone_add(radius1=0.5, location=(0, 0, 0))
            act.rename(objName)
                    
        def delete(objName):
            select(objName)
            bpy.ops.object.delete(use_global=False)

        def delete_all():
            if(len(bpy.data.objects) != 0):
                bpy.ops.object.select_all(action='SELECT')
                bpy.ops.object.delete(use_global=False)

#Lee los datos del CSV alojado en un url
url_str = 'http://blender.chrisconlan.com/iris.csv'
iris_csv = urllib.request.urlopen(url_str)
iris_ob = csv.reader(iris_csv.read().decode('utf-8').splitlines())

#Almacena la cabecera del CSV como una lista y los datos como una lista de listas.
iris_header = []
iris_data = []

#Recorre los elementos del archivo CSV
for v in iris_ob:
    if not iris_header:
        iris_header = v
    else:
        v = [float(v[0]),float(v[1]),float(v[2]),float(v[3]),str(v[4])]
        iris_data.append(v)

#Mi clase mando a llamar a eliminar todo en caso de tener objetos no deseados     
create.delete_all()

#De los datos obtenidos del CSV puedo hacer otro recorrido
#Esta vez creando esferas para ver el comportamiento del archivo CSV
for i in range(0, len(iris_data)):
    create.sphere('Esfera-' + str(i))
    v = iris_data[i]
    act.scale((0.25, 0.25, 0.25))
    act.location((v[0], v[1], v[2]))
