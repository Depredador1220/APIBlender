import bpy
import bmesh

def select(objName):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[objName].select = True

def activate(objName):
    bpy.context.scene.objects.active = bpy.data.objects[objName]
    
def coords(objName, space='GLOBAL'):
    obj = bpy.data.objects[objName]
    
    if obj.mode == 'EDIT':
        v = bmesh.from_edit_mesh(obj.data.verts)
    
    elif obj.mode == 'OBJECT':
        v = obj.data.vertices
        
    if space == 'GLOBAL':
        return [(obj.matrix_world * v.co).to_tuple() for v in v]
    
    elif space == 'LOCAL':
        return [v.co.to_tuple() for v in v]
    
def in_bbox(lbound, ubound, v, buffer=0.0001):
    return lbound[0] - buffer <= v[0] <= ubound[0] + buffer and \
           lbound[1] - buffer <= v[1] <= ubound[1] + buffer and \
           lbound[2] - buffer <= v[2] <= ubound[2] + buffer

class sel:
    """Function Class for operating on SELECTED objects"""
    
    def transform_apply():
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

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
    """Function Class for operating on ACTIVE objects"""
    
    def select_by_loc(lbound=(0, 0, 0), ubound=(0, 0, 0),
select_mode='VERT', coords='GLOBAL'):
        #Establece un modo de seleccion, eje, vertices o cara
        #selection_mode(select_mode)
        
        #Agarra la matriz de transformacion
        world = bpy.context.object.matrix_world
        
        #Hace una instancia al objeto bmesh y asegura la tabla del lookup
        #Ejecuta bm.faces.ensure_lookup_table() para que funcione para 
        #todas las partes
        bm = bmesh.from_edit_mesh(bpy.context.object.data)
        bm.faces.ensure_lookup_table()
        
        #inicializo la lista de vertices y la lista de las partes que seran
        #seleccionadas
        verts = []
        to_select = []
        
        #Para cada vertice, eje o cara
        #1.- Agarra la lista de coordenadas locales o globales
        #2.- Probar si la pieza es entera con el prisma rectangular
        #    El prisma es definido por lbound y ubound
        #3.- Seleccionar cada pieza que regrese Verdadero y deseleccionar
        #    cada pieza que regrese Falso en el paso 2
        if select_mode == 'VERT':
            if coords == 'GLOBAL':
                [verts.append((world * v.co).to_tuple()) for v in bm.verts]
            elif coords == 'LOCAL':
                [verts.append(v.co.to_tuple()) for v in bm.verts]

            [to_select.append(in_bbox(lbound, ubound, v)) for v in verts]
            for vertObj, select in zip(bm.verts, to_select):
                vertObj.select = select
                
        if select_mode == 'EDGE':
            if coords == 'GLOBAL':
                [verts.append([(world * v.co).to_tuple()
                    for v in e.verts]) for e in bm.edges]
            elif coords == 'LOCAL':
                [verts.append([v.co.to_tuple() for v in e.verts])
                    for e in bm.edges]

            [to_select.append(all(in_bbox(lbound, ubound, v)
                for v in e)) for e in verts]
            for edgeObj, select in zip(bm.edges, to_select):
                edgeObj.select = select
                
        
        if select_mode == 'FACE':
            if coords == 'GLOBAL':
                [verts.append([(world * v.co).to_tuple()
                    for v in f.verts]) for f in bm.faces]
            elif coords == 'LOCAL':
                [verts.append([v.co.to_tuple() for v in f.verts])
                    for f in bm.faces]
                    
            [to_select.append(all(in_bbox(lbound, ubound, v)
                for v in f)) for f in verts]
            for faceObj, select in zip(bm.faces, to_select):
                faceObj.select = select
                
    def location(v):
        bpy.context.object.location = v

    def scale(v):
        bpy.context.object.scale = v

    def rotation(v):
        bpy.context.object.rotation_euler = v

    def rename(objName):
        bpy.context.object.name = objName
        
class spec:
    """Function Class for operating on SPECIFIED objects"""

    def scale(objName, v):
        bpy.data.objects[objName].scale = v

    def location(objName, v):
        bpy.data.objects[objName].location = v

    def rotation(objName, v):
        bpy.data.objects[objName].rotation_euler = v
        
    class create:
        """Function Class for CREATING Objects"""
        
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
            
    if __name__ == "__main__":  
        create.cube('PerfectCube')
        
        sel.translate((0, 1, 2))
        sel.scale((1, 1, 2))
        sel.scale((0.5, 1, 1))
        sel.rotate_x(3.1415 / 8)
        sel.rotate_x(3.1415 / 7)
        sel.rotate_z(3.1415 / 3)
       
        create.cone('PointyCone')

        act.location((-2, -2, 0))
        #spec.scale('PointyCone', (1.5, 2.5, 2))
     
        create.sphere('SmoothSphere')
       
        #spec.location('SmoothSphere', (2, 0, 0))
        act.rotation((0, 0, 3.1415 / 3))
        act.scale((1, 3, 1))
