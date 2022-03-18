root_dir=/home/qk/Documents/NewPipeline/Image_Point_Mesh/data/CSEdesk
casmvsnet_ckpt=/home/qk/Documents/NewPipeline/Image_Point_Mesh/checkpoints/CasMVSNet/casmvsnet.ckpt

# 1.run colmap
python imgs2poses.py --scenedir ${root_dir}

# 2.sparse to dense(undistorter)
python sparse2dense.py --scenedir ${root_dir} \
--undistorter_image \
--patch_match \
--stereo_fusion
