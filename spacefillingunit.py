import find_coordinates as fc

def make_spacefillingunit(unit_num):
    if unit_num == 26:
        truncatedcube = fc.TruncatedCube()
        octagonalprism_1 = fc.OctagonalPrism()
        octagonalprism_2 = fc.OctagonalPrism()
        octagonalprism_3 = fc.OctagonalPrism()
        cube_1 = fc.Cube()
        cube_2 = fc.Cube()
        cube_3 = fc.Cube()
        rhombicuboctahedron = fc.Rhombicuboctahedron()
        octagonalprism_1.attach_to_face(truncatedcube,0,2)
        octagonalprism_2.attach_to_face(truncatedcube,2,2)
        octagonalprism_3.attach_to_face(truncatedcube,8,2)
        rhombicuboctahedron.attach_to_face(truncatedcube,1,3)
        cube_1.attach_to_face(octagonalprism_1,0,0)
        cube_2.attach_to_face(octagonalprism_1,8,0)
        cube_3.attach_to_face(octagonalprism_3,0,0)
        truncatedcube.summary_for_rhino(1)
        octagonalprism_1.summary_for_rhino(2)
        octagonalprism_2.summary_for_rhino(3)
        octagonalprism_3.summary_for_rhino(4)
        cube_1.summary_for_rhino(5)
        cube_2.summary_for_rhino(6)
        cube_3.summary_for_rhino(7)
        rhombicuboctahedron.summary_for_rhino(8)

make_spacefillingunit(26)