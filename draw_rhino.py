import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

def draw_brep(vertices,faces):
    breps = []
    for face in faces:
        points=[]
        for i in face:
            point = rg.Point3d(*vertices[i])
            points.append(point)
        
        points.append(points[0])
        polyline = rg.Polyline(points)
        curve = polyline.ToNurbsCurve()
        planar_breps = rg.Brep.CreatePlanarBreps(curve)
        if planar_breps:
            breps.extend(planar_breps)
    
    return breps

vertices_0 = [[-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5]]
faces_0 = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [1, 2, 6, 5], [3, 0, 4, 7]]
vertices_1 = [[-0.5, -0.5, -0.5], [0.20710678118654746, -1.2071067811865475, -0.5], [0.9142135623730949, -0.5000000000000001, -0.5], [0.20710678118654757, 0.20710678118654746, -0.5], [-0.5, -0.5, 0.5], [0.20710678118654746, -1.2071067811865475, 0.5], [0.9142135623730949, -0.5000000000000001, 0.5], [0.20710678118654757, 0.20710678118654746, 0.5]]
faces_1 = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [1, 2, 6, 5], [3, 0, 4, 7]]
a  = draw_brep(vertices_0,faces_0)
b = draw_brep(vertices_1,faces_1)