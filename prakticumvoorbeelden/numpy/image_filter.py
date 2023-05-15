import io
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

class ImageFilter(object):
    
    def __init__(self, kernel):
        self.imgKernel = kernel
    
    def convolve(self, imgTensor):
        # imgTensorRGB = self.convert2RGB(imgTensor.copy())    
        imgTensorRGB = imgTensor.copy() 
        outputImgRGB = np.empty_like(imgTensorRGB)

        for dim in range(imgTensorRGB.shape[-1]):  # loop over rgb channels
            outputImgRGB[:, :, dim] = sp.signal.convolve2d (
                imgTensorRGB[:, :, dim], self.imgKernel, mode="same", boundary="symm"
            )

        return outputImgRGB

    def convert2RGB(self, imgTensor, fillValue=1):
        """Add an alpha channel to an RGB array"""
        # arr = plt.imread(imgFile).astype(float)
            
        if imgTensor.shape[-1] >= 4:
            return imgTensor
        
        imgTensorFilled = np.full (
            shape=(*imgTensor.shape[:-1], 4),
            fill_value=fillValue,
            dtype=imgTensor.dtype
        )
        
        imgTensorFilled[:, :, :-1] = imgTensor

        return imgTensorFilled