import mitsuba as mi


def scene_dict():
    return {
        "type": "scene",
        "integrator": {"type": "path", "max_depth": 6},
        "sensor": {
            "type": "perspective",
            "near_clip": 0.001,
            "far_clip": 100.0,
            "focus_distance": 1000,
            "fov": 45,
            "fov_axis": "smaller",
            "to_world": mi.ScalarTransform4f().look_at(
                origin=[0, 0, 4], target=[0, 0, 0], up=[0, 1, 0]
            ),
            "sampler": {"type": "independent", "sample_count": 128},
            "film": {
                "type": "hdrfilm",
                "width": 512,
                "height": 512,
                "rfilter": {"type": "tent"},
                "pixel_format": "rgb",
                "component_format": "float32",
            },
        },
        "shape": {
            "type": "sphere",
            "center": [0, 0, 0],
            "radius": 1.0,
            "to_world": mi.ScalarTransform4f().rotate([1, 0, 0], 90.0),
            "bsdf": {
                "type": "diffuse",
                "reflectance": {
                    "type": "checkerboard",
                    "color0": {"type": "rgb", "value": [0.9, 0.9, 0.9]},
                    "color1": {"type": "rgb", "value": [0.1, 0.1, 0.1]},
                    "to_uv": mi.ScalarTransform3f().scale([2, 2]),
                },
            },
        },
        # Multiple emitters – as a list of named entries
        "emitter_1": {
            "type": "point",
            "position": [2, 0, 4],
            "intensity": {"type": "rgb", "value": [30, 30, 30]},
        },
        "emitter_2": {
            "type": "point",
            "position": [-2, 0, 4],
            "intensity": {"type": "rgb", "value": [30, 30, 30]},
        },
        "emitter_3": {
            "type": "point",
            "position": [0, 2, 4],
            "intensity": {"type": "rgb", "value": [30, 30, 30]},
        },
        "emitter_4": {
            "type": "point",
            "position": [0, -2, 4],
            "intensity": {"type": "rgb", "value": [30, 30, 30]},
        },
    }
