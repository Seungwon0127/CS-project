class IceField:
    """
    빙하 상태를 관리하는 클래스
    """

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

        pass

    def is_melted(self):
        """
        반환: True / False
        """

        pass

    def contains(self, location):
        """
        반환: True / False
        """

        pass
