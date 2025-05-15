import numpy as np
from scipy.spatial.transform import Rotation as R

class Polyhedron:
    def __init__(self, name, vertices, faces):
        self.name = name
        self.vertices = np.array(vertices, dtype=float)
        self.faces = faces # 絶対に多面体に向かって時計回りで頂点を並べる
        self.edges = self._generate_edges()
        self.center = self._calculate_center()

    def _calculate_center(self):
        return np.mean(self.vertices, axis=0)
    
    def _generate_edges(self):
        edge_set = set()
        for face in self.faces:
            for i in range(len(face)):
                a,b = sorted((face[i],face[(i+1)%len(face)]))
                edge_set.add((a,b))
        return sorted(edge_set)
    
    def summary(self):
        print(f"{self.name}")
        print(f"Vertices ({len(self.vertices)}):")
        for i, v in enumerate(self.vertices):
            print(f"  {i}: {np.round(v, 4)}")
        print(f"Edges ({len(self.edges)}): {self.edges}")
        print(f"Faces ({len(self.faces)}): {self.faces}")
        print(f"Center: {np.round(self.center, 4)}")

    def summary_for_rhino(self,number):
        print(f"vertices_{number} = {self.vertices.tolist()}")
        print(f"faces_{number} = {self.faces}")

    def translate(self,start,end):
        def move_points(points,start,end):
            move_vector = np.array(end, dtype=float) - np.array(start, dtype=float)
            return np.array(points, dtype=float) + move_vector
        
        self.vertices = move_points(self.vertices,start,end)
        self.center = self._calculate_center()
    
    def rotate(self,origin,p0,p1):
        def rotate(points,axis,angle_rad,origin):
            points = np.array(points, dtype=float)
            axis = np.array(axis, dtype=float)
            origin = np.array(origin, dtype=float)

            # 回転オブジェクト作成（軸×角度）
            rotvec = angle_rad * axis / np.linalg.norm(axis)
            rot = R.from_rotvec(rotvec)

            # 原点中心に回転してから戻す
            rotated = rot.apply(points - origin) + origin
            return rotated
        
        def get_normal_vector(origin,p0,p1):
            v1 = np.array(p0) - np.array(origin)
            v2 = np.array(p1) - np.array(origin)
            normal = np.cross(v1, v2)
            # ゼロ割防止のためチェック
            norm = np.linalg.norm(normal)
            if norm == 0:
                raise ValueError("3点が同一直線上にあるため、法線ベクトルを定義できません。")
            
            return normal / norm
            
        def get_angle_rad(origin,p0,p1):
            v1 = np.array(p0) - np.array(origin)
            v2 = np.array(p1) - np.array(origin)
            inner = np.inner(v1,v2)
            v1_norm = np.linalg.norm(v1)
            v2_norm = np.linalg.norm(v2)
            theta = np.arccos(inner/(v1_norm*v2_norm))

            return theta
        
        axis = get_normal_vector(origin,p0,p1)
        angle_rad = get_angle_rad(origin,p0,p1)

        self.vertices = rotate(self.vertices,axis,angle_rad,origin)
        self.center = self._calculate_center()

    def attach_to_face(self, target_polyhedron, target_face_index, self_face_index):
        target_face = target_polyhedron.faces[target_face_index]
        self_face = self.faces[self_face_index]
        
        t0 = target_polyhedron.vertices[target_face[0]]
        t1 = target_polyhedron.vertices[target_face[1]]
        t2 = target_polyhedron.vertices[target_face[2]]

        s0 = self.vertices[self_face[-1]]
        s1 = self.vertices[self_face[-2]]
        s2 = self.vertices[self_face[-3]] #書きかけ



class Cube(Polyhedron): 
    def __init__(self):
        vertices = [
            [-0.5, -0.5, -0.5],
            [ 0.5, -0.5, -0.5],
            [ 0.5,  0.5, -0.5],
            [-0.5,  0.5, -0.5],
            [-0.5, -0.5,  0.5],
            [ 0.5, -0.5,  0.5],
            [ 0.5,  0.5,  0.5],
            [-0.5,  0.5,  0.5]
        ]
        faces = [
            [0, 1, 2, 3],
            [4, 7, 6, 5],
            [0, 4, 5, 1],
            [2, 6, 7, 3],
            [1, 5, 6, 2],
            [0, 3, 7, 4]
        ]
        super().__init__("Cube", vertices, faces)

cube = Cube()

cube.summary_for_rhino(0)
"""
cube.translate([0,0,0],[10,10,10])

cube.summary()

cube.rotate(cube.vertices[0],cube.vertices[1],cube.vertices[3])
cube.summary()

cube.rotate(cube.vertices[0],cube.vertices[3],cube.vertices[1])
cube.summary()
"""
cube.rotate(cube.vertices[0],cube.vertices[3],cube.vertices[2])
cube.summary_for_rhino(1)