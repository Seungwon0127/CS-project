class IceField:

    def __init__(self):

        # 현재 빙하 면적 (float)
        self.area = None

        # 턴마다 감소하는 빙하 면적 (float)
        self.melt_rate = None

        # 빙하 소멸 기준 면적 (float)
        self.min_area = None

    def melt(self):
        """
        - 현재 area 감소
        - 최소 면적 이하로 감소하지 않도록 처리
        """
        if self.area is None or self.melt_rate is None:
            return None

        self.area -= self.melt_rate

        if self.min_area is not None and self.area < self.min_area:
            self.area = self.min_area

        return self.area

    def is_melted(self):
        """
        반환: True / False
        """
        if self.area is None or self.min_area is None:
            return False

        return self.area <= self.min_area

    def contains(self, location):
        """
        반환: True / False
        """
        if self.area is None or location is None:
            return False

        x, y = location
        side_length = self.area ** 0.5

        return 0 <= x <= side_length and 0 <= y <= side_length
