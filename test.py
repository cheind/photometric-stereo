import mitsuba as mi
import matplotlib.pyplot as plt

from scenes import sphere, plane
from pms import rendering


mi.set_variant("cuda_ad_rgb")
sdict = plane.scene_dict()

images, sdicts = rendering.render(sdict)

print(sdicts[0]["emitter"]["position"])
print(sdicts[0]["emitter"]["intensity"])


fig, axs = plt.subplots(1, len(images))
for img, ax in zip(images, axs):
    ax.imshow(img ** (1.0 / 2.2))  # approximate sRGB tonemapping
    ax.set_aspect("equal")
    # ax.imshow(img)  # approximate sRGB tonemapping

# plt.axis("off")
plt.show()
