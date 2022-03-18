import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--scenedir', type=str,
                    help='input scene directory')
parser.add_argument('--undistorter_image', default='False', action='store_true')
parser.add_argument('--patch_match', default='False', action='store_true')
parser.add_argument('--stereo_fusion', default='False', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args()
    scenedir = args.scenedir
    
    # create dense folder
    densedir = os.path.join(scenedir, "dense")
    if not os.path.exists(densedir):
        os.mkdir(densedir)
    
    undistorter_image = args.undistorter_image
    # patch_match = args.patch_match
    # stereo_fusion = args.stereo_fusion
    patch_match = False
    stereo_fusion = False

    # Undistorter image
    if undistorter_image:
        image_path = os.path.join(scenedir, "images")
        input_path = os.path.join(scenedir, "sparse/0")
        cmd_for_colmap = f"colmap image_undistorter "
        cmd_for_colmap += f"--image_path {image_path} "
        cmd_for_colmap += f"--input_path {input_path} "
        cmd_for_colmap += f"--output_path {densedir} "
        cmd_for_colmap += "--output_type COLMAP"
        os.system(cmd_for_colmap)
        print(" Image Undistorter Done!")
        del cmd_for_colmap

    # patch_match_stereo
    if patch_match:
        cmd_for_colmap = "colmap patch_match_stereo "
        cmd_for_colmap += f"--workspace_path {densedir} "
        cmd_for_colmap += f"--workspace_format COLMAP "
        cmd_for_colmap += f"--PatchMatchStereo.geom_consistency true"
        os.system(cmd_for_colmap)
        print(" Patch Match Stereo Done!")
        del cmd_for_colmap

    # stereo_fusion
    if stereo_fusion:
        output_ply_path = os.path.join(densedir, "fused.ply")
        cmd_for_colmap = "colmap stereo_fusion "
        cmd_for_colmap += f"--workspace_path {densedir} "
        cmd_for_colmap += f"--workspace_format COLMAP "
        cmd_for_colmap += f"--input_type geometric "
        cmd_for_colmap += f"--output_path {output_ply_path}"
        os.system(cmd_for_colmap)
        print(" Stereo Fusion Done!")
        print(f" Result ply saved in {output_ply_path} ")
        del cmd_for_colmap
    