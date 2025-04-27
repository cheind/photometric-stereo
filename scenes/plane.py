import mitsuba as mi


def scene_dict():
    off = 1e2
    intensity = 3e4
    return {
        "type": "scene",
        "integrator": {"type": "path", "max_depth": 6},
        "sensor": {
            "type": "perspective",
            "near_clip": 0.001,
            "far_clip": 1000.0,
            "fov": 45,
            "fov_axis": "smaller",
            "to_world": mi.ScalarTransform4f().look_at(
                origin=[0, 0, 3], target=[0, 0, 0], up=[0, 1, 0]
            ),
            "sampler": {"type": "independent", "sample_count": 128},
            "film": {
                "type": "hdrfilm",
                "width": 512,
                "height": 512,
                # "rfilter": {"type": "tent"},
                "pixel_format": "rgb",
                "component_format": "float32",
            },
        },
        "shape": {
            "type": "sphere",
            # "to_world": mi.ScalarTransform4f().rotate([1, 0, 0], 20.0),
            "bsdf": {
                "type": "diffuse",
                "reflectance": {"type": "rgb", "value": 1.0},
            },
        },
        # Multiple emitters – as a list of named entries
        "emitter_1": {
            "type": "point",
            "position": [off, 0, off],
            "intensity": {"type": "rgb", "value": intensity},
        },
        "emitter_2": {
            "type": "point",
            "position": [-off, 0, off],
            "intensity": {"type": "rgb", "value": intensity},
        },
        "emitter_3": {
            "type": "point",
            "position": [0, off, off],
            "intensity": {"type": "rgb", "value": intensity},
        },
        "emitter_4": {
            "type": "point",
            "position": [0, -off, off],
            "intensity": {"type": "rgb", "value": intensity},
        },
    }
