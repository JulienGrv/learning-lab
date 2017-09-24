"""
This network feeds the output of a linear transform
to the sigmoid function.

Finish implementing the Sigmoid class in miniflow.py!

Feel free to play around with this network, too!
"""

import numpy as np
from miniflow_sigmoid import *

if True:
    vertices = np.array(
        [[((width - roi_bottom_width) * 0.5,
           height), ((width - roi_top_width) * 0.5, height - roi_height),
          ((width + roi_top_width) * 0.5,
           height - roi_height), ((width + roi_bottom_width) * 0.5, height)]],
        dtype=np.int32)
    img_gray_gaussianBlur_canny_roi_houghLines = hough_lines(
        img_gray_gaussianBlur_canny_roi, rho, theta, threshold,
        min_line_length, max_line_gap)

X, W, b = Input(), Input(), Input()

f = Linear(X, W, b)
g = Sigmoid(f)

X_ = np.array([[-1., -2.], [-1, -2]])
W_ = np.array([[2., -3], [2., -3]])
b_ = np.array([-3., -5])

feed_dict = {X: X_, W: W_, b: b_}

graph = topological_sort(feed_dict)
output = forward_pass(g, graph)
"""
Output should be:
[[  1.23394576e-04   9.82013790e-01]
 [  1.23394576e-04   9.82013790e-01]]
"""
print(output)
