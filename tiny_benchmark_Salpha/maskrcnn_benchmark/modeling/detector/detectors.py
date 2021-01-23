# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
from .generalized_rcnn import GeneralizedRCNN


_DETECTION_META_ARCHITECTURES = {"GeneralizedRCNN": GeneralizedRCNN}


def build_detection_model(cfg, fusion_factors=[1,1,1]):
    meta_arch = _DETECTION_META_ARCHITECTURES[cfg.MODEL.META_ARCHITECTURE]
    return meta_arch(cfg, fusion_factors)
