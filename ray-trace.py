import numpy as np
import pygame


def normalize(v):
    return v / np.linalg.norm(v)


def dot(a, b):
    return np.dot(a, b)


def hit_sphere(center, radius, ray_origin, ray_dir):
    oc = ray_origin - center
    a = dot(ray_dir, ray_dir)
    c = dot(oc, oc) - radius * radius
    b = 2.0 * dot(ray_dir, oc)
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return -1
    # quatratic formula
    return (-b - np.sqrt(discriminant)) / (2 * a)


def main():
    aspect_ratio: float = 16.0 / 9.0
    width: int = 1000
    height: int = (int)(width / aspect_ratio)

    pygame.init()
    screen = pygame.display.set_mode((width, height))

    origin = np.array([0, 0, 0], dtype=float)

    # ray point would just be origin + t * direction
    sphere_center = np.array([0, 0, -1], dtype=float)
    sphere_radius = 0.5

    for y in range(height):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        for x in range(width):
            # gotta convert the pixels to viewport coordinates
            u = ((x / width) * 2 - 1) * aspect_ratio
            v = 1 - (y / height) * 2

            ray_dir = normalize(np.array([u, v, -1], dtype=float))
            t = hit_sphere(sphere_center, sphere_radius, origin, ray_dir)
            if t > 0:
                screen.set_at((x, y), (255, 0, 0))
            else:
                screen.set_at((x, y), (0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
