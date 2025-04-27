import mitsuba as mi
import numpy as np


def compile_per_emitter(scene: dict):
    emitters = [k for k in scene.keys() if k.startswith("emitter_")]
    sdict_no_emitters = {k: v for k, v in scene.items() if k not in emitters}
    scenes: list[mi.Scene] = []
    for key in emitters:
        new_dict = {**sdict_no_emitters, "emitter": scene[key]}
        scenes.append(mi.load_dict(new_dict))
    return scenes


def render(sdict: dict) -> tuple[list[np.ndarray], list[dict]]:

    emitters = [k for k in sdict.keys() if k.startswith("emitter")]
    sdict_no_emitters = {k: v for k, v in sdict.items() if k not in emitters}

    images = []
    scenes = []
    for key in emitters:

        new_dict = {**sdict_no_emitters, "emitter": sdict[key]}
        print(new_dict)
        new_scene = mi.load_dict(new_dict)
        print(new_scene)

        image = mi.render(new_scene)
        images.append(image.numpy())
        scenes.append(new_dict)

    return images, scenes
