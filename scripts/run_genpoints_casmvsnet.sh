root_dir=/home/qk/Documents/NewPipeline/Image-3DRecon/data/ZQK2
casmvsnet_ckpt=/home/qk/Documents/NewPipeline/Image_Point_Mesh/checkpoints/CasMVSNet/casmvsnet.ckpt

# 1.run colmap
python imgs2poses.py --scenedir ${root_dir}

# 2.sparse to dense(undistorter)
python sparse2dense.py \
--scenedir ${root_dir} \
--undistorter_image

# 3.colmap to casmvsnet
python colmap2mvsnet.py --dense_folder ${root_dir}/dense --save_folder ${root_dir}/casmvsnet

# 4.casmvsnet pre and fusion
cd cascade-stereo/CasMVSNet
python test.py \
--dataset=general_eval \
--batch_size=1 \
--testpath_single_scene=${root_dir}/casmvsnet \
--loadckpt=${casmvsnet_ckpt} \
--testlist=all \
--outdir=${root_dir}/mvs \
--interval_scale=1.06

cd ../..
echo "Pipeline Finsih!!!"
