from pip import main
import cv2
import os

if __name__ == '__main__':
    mov_path = "/home/qk/Documents/NewPipeline/Image-3DRecon/data/ZQK2/IMG_2519.MOV"
    out_path = "/home/qk/Documents/NewPipeline/Image-3DRecon/data/ZQK2/images"

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    frame_interval = 10
    vc = cv2.VideoCapture(mov_path)
    fps = vc.get(cv2.CAP_PROP_FPS)
    frame_all = vc.get(cv2.CAP_PROP_FRAME_COUNT)
    
    rval, frame = vc.read()

    print(f"Video have {frame_all} frames.")
    print(f"Video FPOS {fps}")
    print(f"Video time {frame_all/fps} s")
    
    frame_count = 1
    save_count = 0
    while rval:
        rval, frame = vc.read()
        if frame_count % frame_interval == 0:
            save_path = os.path.join(out_path, f"{save_count}.png")
            save_count += 1
            cv2.imwrite(save_path, frame)

        frame_count += 1
    vc.release()
    print(f"Save {save_count} images in {out_path}")
    print("Done")