class Camera:
    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.zoom = None
        self.move_speed = None

    def move(self, dx, dy):
        if self.x is None:
            self.x = 0
        if self.y is None:
            self.y = 0

        self.x += dx if dx is not None else 0
        self.y += dy if dy is not None else 0

        self.clamp()
        self.update()

        return None

    def world_to_screen(self, world_x, world_y):
        camera_x = self.x if self.x is not None else 0
        camera_y = self.y if self.y is not None else 0
        zoom = self.zoom if self.zoom is not None else 1

        screen_x = (world_x - camera_x) * zoom
        screen_y = (world_y - camera_y) * zoom

        return screen_x, screen_y

    def screen_to_world(self, screen_x, screen_y):
        camera_x = self.x if self.x is not None else 0
        camera_y = self.y if self.y is not None else 0
        zoom = self.zoom if self.zoom not in (None, 0) else 1

        world_x = screen_x / zoom + camera_x
        world_y = screen_y / zoom + camera_y

        return world_x, world_y

    def follow(self, target):
        target_x = getattr(target, "x", 0)
        target_y = getattr(target, "y", 0)
        width = self.width if self.width is not None else 0
        height = self.height if self.height is not None else 0

        self.x = target_x - width / 2
        self.y = target_y - height / 2

        self.clamp()
        self.update()

        return None

    def update(self):
        return None

    def clamp(self):
        if self.x is not None and self.x < 0:
            self.x = 0
        if self.y is not None and self.y < 0:
            self.y = 0

        return None

    def set_zoom(self, zoom):
        if zoom is not None and zoom > 0:
            self.zoom = zoom

        return self.zoom
