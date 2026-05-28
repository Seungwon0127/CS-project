class Camera:
    """월드 좌표와 화면 좌표 사이의 변환을 담당하는 카메라 클래스."""

    def __init__(self):
        # 카메라가 바라보는 월드 좌표의 왼쪽 위 x 위치입니다.
        self.x = None

        # 카메라가 바라보는 월드 좌표의 왼쪽 위 y 위치입니다.
        self.y = None

        # 화면에 보이는 가로 크기입니다.
        self.width = None

        # 화면에 보이는 세로 크기입니다.
        self.height = None

        # 확대/축소 배율입니다. None이면 계산에서 기본값 1로 처리합니다.
        self.zoom = None

        # 카메라 이동 속도입니다. 실제 이동량 계산에 사용할 수 있도록 보관합니다.
        self.move_speed = None

    def move(self, dx, dy):
        """카메라를 dx, dy만큼 이동하고, 이동 후 위치 보정과 상태 갱신을 수행합니다."""
        # 위치가 아직 설정되지 않았으면 원점에서 시작합니다.
        if self.x is None:
            self.x = 0
        if self.y is None:
            self.y = 0

        # None 이동값은 0으로 취급해 호출부가 비어 있어도 안전하게 둡니다.
        self.x += dx if dx is not None else 0
        self.y += dy if dy is not None else 0

        # 이동 후 화면 밖 음수 좌표로 벗어나지 않게 보정합니다.
        self.clamp()

        # 현재는 비어 있지만, 이후 애니메이션/스크롤 상태 갱신을 넣을 자리입니다.
        self.update()

        return None

    def world_to_screen(self, world_x, world_y):
        """월드 좌표를 카메라 위치와 줌 배율을 반영한 화면 좌표로 변환합니다."""
        camera_x = self.x if self.x is not None else 0
        camera_y = self.y if self.y is not None else 0
        zoom = self.zoom if self.zoom is not None else 1

        screen_x = (world_x - camera_x) * zoom
        screen_y = (world_y - camera_y) * zoom

        return screen_x, screen_y

    def screen_to_world(self, screen_x, screen_y):
        """화면 좌표를 카메라 위치와 줌 배율을 되돌려 월드 좌표로 변환합니다."""
        camera_x = self.x if self.x is not None else 0
        camera_y = self.y if self.y is not None else 0

        # 0으로 나누는 오류를 막기 위해 zoom이 비어 있거나 0이면 1배율로 계산합니다.
        zoom = self.zoom if self.zoom not in (None, 0) else 1

        world_x = screen_x / zoom + camera_x
        world_y = screen_y / zoom + camera_y

        return world_x, world_y

    def follow(self, target):
        """target 객체가 화면 중앙에 오도록 카메라 위치를 맞춥니다."""
        # target에 x/y가 없으면 원점으로 간주합니다.
        target_x = getattr(target, "x", 0)
        target_y = getattr(target, "y", 0)
        width = self.width if self.width is not None else 0
        height = self.height if self.height is not None else 0

        # 대상 좌표에서 화면 절반 크기를 빼면 대상이 중앙에 놓입니다.
        self.x = target_x - width / 2
        self.y = target_y - height / 2

        self.clamp()
        self.update()

        return None

    def update(self):
        """카메라 상태를 갱신하는 확장 지점입니다."""
        return None

    def clamp(self):
        """카메라 좌표가 음수가 되지 않도록 최소값을 0으로 제한합니다."""
        if self.x is not None and self.x < 0:
            self.x = 0
        if self.y is not None and self.y < 0:
            self.y = 0

        return None

    def set_zoom(self, zoom):
        """양수 zoom 값만 받아 카메라 확대/축소 배율로 저장합니다."""
        if zoom is not None and zoom > 0:
            self.zoom = zoom

        return self.zoom
