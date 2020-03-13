import bpy

def select(objName):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[objName].select = True

def activate(objName):
    bpy.context.scene.objects.active = bpy.data.objects[objName]
    
class create:
        """Clase para crear Objetos"""
        
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
         
        #Para determinar si esta en modo edicion u objeto       
        def mode(mode_name):
            bpy.ops.object.mode_set(mode=mode_name)
            if mode_name == "EDIT":
                bpy.ops.mesh.select_all(action="DESELECT")
                
               

class sel:
    """Clase que maneja los objetos seleccionados"""

    def translate(v):
        bpy.ops.transform.translate(
        value=v, constraint_axis=(True, True, True))

    def scale(v):
        bpy.ops.transform.resize(value=v, constraint_axis=(True, True, True))

    def rotate_x(v):
        bpy.ops.transform.rotate(value=v, axis=(1, 0, 0))

    def rotate_y(v):
        bpy.ops.transform.rotate(value=v, axis=(0, 1, 0))
        
    def rotate_z(v):
        bpy.ops.transform.rotate(value=v, axis=(0, 0, 1))
        
class act:
    """Clase que maneja los objetos activos"""

    def location(v):
        bpy.context.object.location = v

    def scale(v):
        bpy.context.object.scale = v

    def rotation(v):
        bpy.context.object.rotation_euler = v

    def rename(objName):
        bpy.context.object.name = objName
        
class spec:
    """Clase que maneja objetos especificos"""

    def scale(objName, v):
        bpy.data.objects[objName].scale = v

    def location(objName, v):
        bpy.data.objects[objName].location = v

    def rotation(objName, v):
        bpy.data.objects[objName].rotation_euler = v
            
    if __name__ == "__main__":  
        create.cube('Cubo')
        
        sel.translate((0, 1, 2))
        sel.scale((1, 1, 2))
        sel.scale((0.5, 1, 1))
        sel.rotate_x(3.1415 / 8)
        sel.rotate_x(3.1415 / 7)
        sel.rotate_z(3.1415 / 3)
       
        create.cone('Cono')

        act.location((-2, -2, 0))
        #spec.scale('Cono', (1.5, 2.5, 2))
     
        create.sphere('EsferaDelDragon')
       
        #spec.location('EsferaDelDragon', (2, 0, 0))
        act.rotation((0, 0, 3.1415 / 3))
        act.scale((1, 3, 1))
