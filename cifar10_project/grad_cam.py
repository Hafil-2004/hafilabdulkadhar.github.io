import torch
import numpy as np
import cv2

def apply_grad_cam(model, input_tensor, target_class, output_path):
    input_tensor.requires_grad = True
    model.zero_grad()

    output = model(input_tensor)
    output[:, target_class].backward()

    gradients = input_tensor.grad.data
    activations = input_tensor.data

    weights = torch.mean(gradients, dim=[2, 3], keepdim=True)
    cam = torch.sum(weights * activations, dim=1).squeeze()

    cam = np.maximum(cam.detach().cpu().numpy(), 0)
    cam = cv2.resize(cam, (32, 32))
    cam = (cam - cam.min()) / (cam.max() - cam.min()) * 255
    cam = np.uint8(cam)
    heatmap = cv2.applyColorMap(cam, cv2.COLORMAP_JET)

    cv2.imwrite(output_path, heatmap)
