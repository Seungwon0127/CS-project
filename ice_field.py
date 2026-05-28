class IceField:
    """빙하 면적, 감소량, 최소 면적을 관리하는 클래스."""

    def __init__(self):
        # 현재 빙하 면적입니다.
        self.area = None

        # 한 턴마다 감소하는 빙하 면적입니다.
        self.melt_rate = None

        # 빙하가 더 이상 줄어들지 않는 최소 면적입니다.
        self.min_area = None

    def melt(self):
        """
        빙하 면적을 melt_rate만큼 감소시킵니다.

        area 또는 melt_rate가 아직 설정되지 않았으면 계산하지 않고 None을 반환합니다.
        """
        if self.area is None or self.melt_rate is None:
            return None

        self.area -= self.melt_rate

        # 최소 면적이 정해져 있으면 그 아래로 내려가지 않게 고정합니다.
        if self.min_area is not None and self.area < self.min_area:
            self.area = self.min_area

        return self.area

    def is_melted(self):
        """빙하가 최소 면적까지 녹았는지 True/False로 반환합니다."""
        if self.area is None or self.min_area is None:
            return False

        return self.area <= self.min_area

    def contains(self, location):
        """
        location 좌표가 빙하 영역 안에 있는지 확인합니다.

        현재는 빙하를 원점에서 시작하는 정사각형 영역으로 단순화해 계산합니다.
        """
        if self.area is None or location is None:
            return False

        x, y = location
        side_length = self.area ** 0.5

        return 0 <= x <= side_length and 0 <= y <= side_length
