import numpy as np
from scipy.spatial.transform import Rotation as R

class Polyhedron:
    def __init__(self, name, vertices, faces):
        self.name = name
        self.vertices = np.array(vertices, dtype=float)
        self.faces = faces # 絶対に多面体に向かって反時計回りで頂点を並べる
        self.edges = self._generate_edges()
        self.center = self._calculate_center()
        self._normalize_edge_length()

    def _calculate_center(self):
        return np.mean(self.vertices, axis=0)

    def _normalize_edge_length(self, target_length=1.0):
        # 1本目のエッジの長さを使用
        i, j = self.edges[0]
        v_i, v_j = self.vertices[i], self.vertices[j]
        current_length = np.linalg.norm(v_j - v_i)
        scale = target_length / current_length
        self.vertices *= scale
        self.center = self._calculate_center()

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

    def _rotate_around_axis(self, origin, axis, angle_rad):
        axis = np.array(axis, dtype=float)
        norm = np.linalg.norm(axis)
        axis = axis / norm
        rot = R.from_rotvec(angle_rad * axis)

        # 点群を原点中心に回転してから戻す
        origin = np.array(origin, dtype=float)
        self.vertices = rot.apply(self.vertices - origin) + origin
        self.center = self._calculate_center()

    def _rotate_to_align_points(self, center, point_to_rotate, target_point):
        v_before = point_to_rotate - center
        v_after = target_point - center

        norm_before = np.linalg.norm(v_before)
        norm_after = np.linalg.norm(v_after)

        v_before = v_before / norm_before
        v_after = v_after / norm_after

        cos_angle = np.clip(np.dot(v_before, v_after), -1.0, 1.0)
        angle = np.arccos(cos_angle)

        rotation_axis = np.cross(v_before, v_after)
        norm_axis = np.linalg.norm(rotation_axis)
        rotation_axis = rotation_axis / norm_axis

        self._rotate_around_axis(center, rotation_axis, angle)

    def _rotate_around_axis_to_align_points(self, axis_point1, axis_point2, point_to_rotate, target_point):
        # 回転軸を計算
        axis = axis_point2 - axis_point1
        axis = axis / np.linalg.norm(axis)

        # 回転前後の点を軸の始点に対する相対ベクトルに変換
        p1 = point_to_rotate - axis_point1
        p2 = target_point - axis_point1

        # 軸方向の成分を除去（軸に垂直な平面上に投影）
        p1_proj = p1 - np.dot(p1, axis) * axis
        p2_proj = p2 - np.dot(p2, axis) * axis

        # 投影ベクトルの長さをチェック
        norm_p1 = np.linalg.norm(p1_proj)
        norm_p2 = np.linalg.norm(p2_proj)

        # 正規化
        p1_proj = p1_proj / norm_p1
        p2_proj = p2_proj / norm_p2

        # 内積から角度を計算
        cos_angle = np.clip(np.dot(p1_proj, p2_proj), -1.0, 1.0)
        angle = np.arccos(cos_angle)

        # 回転方向を決定（軸に対する外積方向）
        cross_prod = np.cross(p1_proj, p2_proj)
        if np.dot(cross_prod, axis) < 0:
            angle = -angle

        # 回転を実行
        self._rotate_around_axis(axis_point1, axis, angle)

    #多面体の面同士を合わせる
    def attach_to_face(self, target_polyhedron, target_face_index, self_face_index):

        # 対象の面を取得
        target_face = target_polyhedron.faces[target_face_index]
        self_face = self.faces[self_face_index]

        # 1点目同士を合わせる
        t0 = target_polyhedron.vertices[target_face[0]]
        s0 = self.vertices[self_face[0]]
        self.translate(s0, t0)

        # 1点目を中心に2点目が合うように回転
        t1 = target_polyhedron.vertices[target_face[1]]
        s1 = self.vertices[self_face[-1]]
        self._rotate_to_align_points(t0, s1, t1)

        # 1-2点目の軸周りに3点目が合うように回転
        t2 = target_polyhedron.vertices[target_face[-1]]
        s2 = self.vertices[self_face[1]]
        self._rotate_around_axis_to_align_points(t0, t1, s2, t2)

        return self


# 正四面体
class Tetrahedron(Polyhedron):
    def __init__(self):
        vertices = [
            [-0.81649658,-0.47140452 ,0.33333333],
            [0.81649658,-0.47140452,0.33333333],
            [0.00000000,0.0000000,-1.00000000],
            [0.00000000,0.94280904,0.33333333]
        ]
        faces = [
            [0, 1, 3],
            [0, 3, 2],
            [0, 2, 1],
            [1, 2, 3]
        ]
        super().__init__("Tetrahedron", vertices, faces)

# 正六面体
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
            [3, 2, 1, 0],
            [5, 6, 7, 4],
            [1, 5, 4, 0],
            [3, 7, 6, 2],
            [2, 6, 5, 1],
            [4, 7, 3, 0]
        ]
        super().__init__("Cube", vertices, faces)

# 正八面体　
class Octahedron(Polyhedron):
    def __init__(self):
        vertices = [
            [-0.70710678, -0.70710678, 0.0],
            [-0.70710678, 0.70710678, 0.0],
            [0.70710678, 0.70710678, 0.0],
            [0.70710678, -0.70710678, 0.0],
            [0.0, 0.0, -1.0],
            [0.0, 0.0, 1.0],
        ]
        faces = [
            [0, 1, 4],
            [0, 4, 3],
            [0, 3, 5],
            [0, 5, 1],
            [1, 2, 4],
            [1, 5, 2],
            [2, 3, 4],
            [2, 5, 3],
        ]
        super().__init__("Octahedron", vertices, faces)

# 正三角柱
class TriangularPrism(Polyhedron):
    def __init__(self):
        vertices = [
            [-0.65465367, -0.37796447, 0.65465367],
            [0.0, 0.75592895, 0.65465367],
            [0.65465367, -0.37796447, 0.65465367],
            [-0.65465367, -0.37796447, -0.65465367],
            [0.0, 0.75592895, -0.65465367],
            [0.65465367, -0.37796447, -0.65465367],
        ]
        faces = [
            [0, 1, 4, 3],
            [0, 3, 5, 2],
            [0, 2, 1],
            [1, 2, 5, 4],
            [3, 4, 5],
        ]
        super().__init__("TriangularPrism", vertices, faces)

# 正六角柱
class HexagonalPrism(Polyhedron):
    def __init__(self):
        vertices = [
            [-0.4472136, -0.77459667, 0.4472136],
            [-0.89442719, 0.0, 0.4472136],
            [-0.4472136, 0.77459667, 0.4472136],
            [0.4472136, 0.77459667, 0.4472136],
            [0.89442719, -0.0, 0.4472136],
            [0.4472136, -0.77459667, 0.4472136],
            [-0.4472136, -0.77459667, -0.4472136],
            [-0.89442719, 0.0, -0.4472136],
            [-0.4472136, 0.77459667, -0.4472136],
            [0.4472136, 0.77459667, -0.4472136],
            [0.89442719, -0.0, -0.4472136],
            [0.4472136, -0.77459667, -0.4472136],
        ]
        faces = [
            [0, 1, 7, 6],
            [0, 6, 11, 5],
            [0, 5, 4, 3, 2, 1],
            [1, 2, 8, 7],
            [2, 3, 9, 8],
            [3, 4, 10, 9],
            [4, 5, 11, 10],
            [6, 7, 8, 9, 10, 11],
        ]
        super().__init__("HexagonalPrism", vertices, faces)

# 正八角柱
class OctagonalPrism(Polyhedron):
    def __init__(self):
        vertices = [
            [-0.35740674, -0.86285621, 0.35740674],
            [-0.86285621, -0.35740674, 0.35740674],
            [-0.86285621, 0.35740674, 0.35740674],
            [-0.35740674, 0.86285621, 0.35740674],
            [0.35740674, 0.86285621, 0.35740674],
            [0.86285621, 0.35740674, 0.35740674],
            [0.86285621, -0.35740674, 0.35740674],
            [0.35740674, -0.86285621, 0.35740674],
            [-0.35740674, -0.86285621, -0.35740674],
            [-0.86285621, -0.35740674, -0.35740674],
            [-0.86285621, 0.35740674, -0.35740674],
            [-0.35740674, 0.86285621, -0.35740674],
            [0.35740674, 0.86285621, -0.35740674],
            [0.86285621, 0.35740674, -0.35740674],
            [0.86285621, -0.35740674, -0.35740674],
            [0.35740674, -0.86285621, -0.35740674],
        ]
        faces = [
            [0, 1, 9, 8],
            [0, 8, 15, 7],
            [0, 7, 6, 5, 4, 3, 2, 1],
            [1, 2, 10, 9],
            [2, 3, 11, 10],
            [3, 4, 12, 11],
            [4, 5, 13, 12],
            [5, 6, 14, 13],
            [6, 7, 15, 14],
            [8, 9, 10, 11, 12, 13, 14, 15],
        ]
        super().__init__("OctagonalPrism", vertices, faces)

# 正十二角柱 座標、面データなし
class DodecagonalPrism(Polyhedron):
    def __init__(self):
        vertices = [
            [1.93185165, 0.0, 0.5],
            [1.67303261, 0.96592583, 0.5],
            [0.96592583, 1.67303261, 0.5],
            [0.0, 1.93185165, 0.5],
            [-0.96592583, 1.67303261, 0.5],
            [-1.67303261, 0.96592583, 0.5],
            [-1.93185165, 0.0, 0.5],
            [-1.67303261, -0.96592583, 0.5],
            [-0.96592583, -1.67303261, 0.5],
            [-0.0, -1.93185165, 0.5],
            [0.96592583, -1.67303261, 0.5],
            [1.67303261, -0.96592583, 0.5],
            [1.93185165, 0.0, -0.5],
            [1.67303261, 0.96592583, -0.5],
            [0.96592583, 1.67303261, -0.5],
            [0.0, 1.93185165, -0.5],
            [-0.96592583, 1.67303261, -0.5],
            [-1.67303261, 0.96592583, -0.5],
            [-1.93185165, 0.0, -0.5],
            [-1.67303261, -0.96592583, -0.5],
            [-0.96592583, -1.67303261, -0.5],
            [-0.0, -1.93185165, -0.5],
            [0.96592583, -1.67303261, -0.5],
            [1.67303261, -0.96592583, -0.5]
        ]

        faces = [
            [0, 1, 13, 12],
            [1, 2, 14, 13],
            [2, 3, 15, 14],
            [3, 4, 16, 15],
            [4, 5, 17, 16],
            [5, 6, 18, 17],
            [6, 7, 19, 18],
            [7, 8, 20, 19],
            [8, 9, 21, 20],
            [9, 10, 22, 21],
            [10, 11, 23, 22],
            [11, 0, 12, 23],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]
        ]
        super().__init__("DodecagonalPrism", vertices, faces)
"""
tetrahedron = Tetrahedron()
tetrahedron.summary_for_rhino(0)
cube = Cube()
cube.summary_for_rhino(1)
"""
octahedron = Octahedron()
octahedron.summary_for_rhino(2)
triangularprism = TriangularPrism()
triangularprism.summary_for_rhino(3)
"""
hexagonalprism = HexagonalPrism()
hexagonalprism.summary_for_rhino(4)
octagonalprism = OctagonalPrism()
octagonalprism.summary_for_rhino(5)
dodecagonalprism = DodecagonalPrism()
dodecagonalprism.summary_for_rhino(6)
"""
triangularprism.translate((0,0,0),(3,3,3))
triangularprism.summary_for_rhino(7)
triangularprism = triangularprism.attach_to_face(octahedron,0,2)
triangularprism.attach_to_face(octahedron,0,2)
triangularprism.summary_for_rhino(8)