# Image-Point-Mesh

A complete pipeline for generating scene point clouds and meshes.

### 1.Register Image Pose[COLMAP]

Use My Desk data for example.

<img src="png/desk1.png" alt="image1" style="zoom:20%;" />

**Sparse Reconstruction**

Use imgs2poses.py(from llff https://github.com/Fyusion/LLFF) to call COLMAP to run structure from motion to get 6DoF image poses and near/far depth bounds for the scene.

`python imgs2poses.py --scenedir xxx/xxx/xxx `

Result will be saved in scenedir, and sparse model will be saved in scenedir/sparse/0

**Dense Reconstruction**

`python sparse2dense.py --scenedir xxx/xxx/xxx`

In this example, 6.6mins for stereo patch and 0.02mins for stereo fusion.

The results show that in low temperature textured regions, traditional depth restoration methods cannot achieve satisfactory results:

<img src="png/desk2.png" alt="image2" style="zoom:30%;" />

**CasMVSNet input from COLMAP SfM**

In order to use CasMVSNet, the data needs to be transformed by :

`python colmap2mvsnet.py --dense_folder data/nerf_llff/room/dense --save_folder data/nerf_llff/room/casmvsnet`

### 2.Generate Depth Image and Fusion[CasMVSNet]

**CasMVSNet-Stereo**

Use CasMVSNet to generate depth map:

`python test.py --dataset=general_eval --batch_size=1 --testpath_single_scene=../../data/nerf_llff/room/casmvsnet --loadckpt=../../checkpoints/casmvsnet.ckpt --testlist=all --outdir=../../data/nerf_llff/room/mvs.ply --interval_scale=1.06`

Only use 2mins to get fusion pointcloud.

<img src="png/desk3.png" alt="image3" style="zoom:50%;" />

**CasMVSNet_pl**

Also, you can use CasMVSNet_pl to get depth map:

### 3.Generate Mesh[ConvONet]

TODO



### 4.Easy Use

Just run the scripts to do all things!

```shell
# CasMVSNet depth pre
bash scripts/run_genpoints_casmvsnet.sh
# COLMAP depth pre
bash scripts/run_genpoints_colmap.sh
```



### 5.More Results

<img src="png/demo4.png" alt="image3" style="zoom:50%;" />
