import argparse
import open3d as o3d


def compress_stl(input_file, output_file, target_triangles):
    # Function to compress STL files
    mesh = o3d.io.read_triangle_mesh(input_file)
    simplified_mesh = mesh.simplify_quadric_decimation(target_triangles)
    simplified_mesh.compute_triangle_normals()
    simplified_mesh.compute_vertex_normals()
    o3d.io.write_triangle_mesh(output_file, simplified_mesh)

def main():
    parser = argparse.ArgumentParser(description="Compress STL files using quadric decimation.")
    parser.add_argument("-i", "--input", help="Input STL file path", required=True)
    parser.add_argument("-o", "--output", help="Output STL file path", required=True)
    parser.add_argument("-t", "--triangles", type=int, help="Target number of triangles", default=3000)

    args = parser.parse_args()

    print(f"Processing {args.input}...")
    compress_stl(args.input, args.output, args.triangles)
    
    print("Compression complete.")

if __name__ == '__main__':
    main()