import numpy as np
import cv2

def Splitarray(array):
    # 初始化数组列表来存储分割后的数组
    split_arrays = []
    current_subarray = []

    # 遍历数组并根据间隔大于100的条件进行分割
    for num in array:
        if current_subarray and num - current_subarray[-1] > 100:
            split_arrays.append(np.array(current_subarray))
            current_subarray = [num]
        else:
            current_subarray.append(num)

    # 添加最后一个子数组
    if current_subarray:
        split_arrays.append(np.array(current_subarray))

    return split_arrays

def Sort_points(contourroad):
    list = [[0,0],[0,0],[0,0],[0,0]]
    # 计算每个子数组中两个数的和
    sums = np.sum(contourroad, axis=2)
    # 根据和的大小进行排序
    minpointidx = np.argmin(sums[:, 0])
    list[0] = contourroad[minpointidx]
    contourroad = np.delete(contourroad, minpointidx, axis=0)
    sums = np.sum(contourroad, axis=2)
    maxpointidx = np.argmax(sums[:, 0])
    list[2] = contourroad[maxpointidx]
    contourroad = np.delete(contourroad, maxpointidx, axis=0)
    if contourroad[0][0][0]-contourroad[0][0][1] >= 0:
        list[1] = contourroad[0]
        list[3] = contourroad[1]
    else:
        list[3] = contourroad[0]
        list[1] = contourroad[1]
    return np.array(list).astype(np.float32)

def Crop_image(image, border):
    """
    裁剪图像边上一圈的框。

    Args:
        image: 输入图像。
        border: 要裁剪的边框宽度。

    Returns:
        裁剪后的图像。
    """

    # 检查图像类型
    if not isinstance(image, np.ndarray):
        raise TypeError("Input image must be a NumPy array.")

    # 检查边框宽度
    if border < 0 or border >= image.shape[0] or border >= image.shape[1]:
        raise ValueError("Border width must be non-negative and less than the image size.")
    returned = cv2.resize(image[border:-border, border:-border,:],(image.shape[0],image.shape[1]))
    # 裁剪图像
    return returned