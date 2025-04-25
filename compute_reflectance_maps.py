import mitsuba as mi
import matplotlib.pyplot as plt
import numpy as np

from scenes import plane
from pms import rendering


def compute_reflectance_map(
    pq: np.ndarray, rho: float, J: float, r2: float, s: np.ndarray
):
    n = np.concat(
        (pq, np.ones(pq.shape[:-1] + (1,))),
        -1,
    )
    lens = np.linalg.norm(n, axis=-1, keepdims=True)
    n = n / lens
    return (rho / np.pi) * (J / r2) * (n @ s)


def main():
    mi.set_variant("cuda_ad_rgb" if "cuda_ad_rgb" in mi.variants() else "scalar_rgb")
    sdict = plane.scene_dict()
    images, sdicts = rendering.render(sdict)

    # imgs = [img / img.max() for img in images]

    albedo = sdict["shape"]["bsdf"]["reflectance"]["value"][0]
    P, Q = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100), indexing="ij")
    pq = np.stack((P, Q), -1)

    maps = []

    for idx in range(len(sdicts)):

        light_pos = np.array(sdicts[idx]["emitter"]["position"])
        light_intensity = np.array(sdicts[idx]["emitter"]["intensity"]["value"])
        r2 = np.dot(light_pos, light_pos)
        s = light_pos / light_pos[-1:]
        s /= np.linalg.norm(s)

        R = compute_reflectance_map(pq, albedo, light_intensity, r2, s)
        maps.append(R)

    loc = [200, 200]
    intensities = [img[loc[1], loc[0]][0] for img in images]

    fig, axs = plt.subplots(2, len(images) + 1)

    for idx, (img, r) in enumerate(zip(images, maps)):
        axs[1, idx].imshow(img)
        # axs[0, idx].contourf(P, Q, r)
        axs[0, idx].contour(P, Q, r)
        axs[0, idx].contour(P, Q, r, levels=[intensities[idx]])
        axs[0, idx].set_aspect("equal")
        axs[1, idx].set_aspect("equal")

        axs[0, -1].contour(P, Q, r, levels=[intensities[idx]])

    axs[0, -1].set_aspect("equal")
    axs[1, -1].set_aspect("equal")

    plt.show()

    print(intensities)

    # fig, axs = plt.subplots(1, 2)
    # axs[0].imshow(images[0])
    # axs[1].imshow(r, extent=(-1, 1, -1, 1))
    # plt.show()

    # print(r)

    # J =
    # print(albedo)

    # print(sdicts[0]["emitter"]["position"])
    # print(sdicts[0]["emitter"]["intensity"])


if __name__ == "__main__":
    main()


# fig, axs = plt.subplots(1, len(images))
# for img, ax in zip(images, axs):
#     ax.imshow(img ** (1.0 / 2.2))  # approximate sRGB tonemapping
#     ax.set_aspect("equal")
#     # ax.imshow(img)  # approximate sRGB tonemapping

# # plt.axis("off")
# plt.show()
