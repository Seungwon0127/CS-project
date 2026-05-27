class ArcticEnvironment:
    """
    극지방 생태계의 전체 환경을 관리하는 클래스.
    IceField와 HunterEvent 객체를 포함하여
    빙하 감소, 기온 변화, 개체 밀도, 종료 조건을 관리한다.
    """

    def __init__(self):
        # 현재 턴 수 (int)
        self.turn = None

        # 현재 기온 (float)
        self.temperature = None

        # 현재 생태계 개체 밀도 (float)
        self.density = None

        # 턴마다 증가하는 온난화 정도 (float)
        self.global_warming_rate = None

        # 빙하 상태를 관리하는 IceField 객체
        self.ice_field = None

        # 사용자 개입 종료 이벤트를 관리하는 HunterEvent 객체
        self.hunter_event = None

    def update(self, animals):
        """
        - turn 증가
        - temperature 변화
        - ice_field의 melt() 호출
        - calculate_density(animals) 호출
        """

        pass

    def calculate_density(self, animals):
        """
        - alive가 True인 생물 수 계산
        - ice_field.area를 이용해 density 계산
        """

        pass

    def handle_event(self, key, animals):
        """
        - hunter_event.trigger(key) 호출
        - hunter_event가 active 상태가 되면 eliminate_all(animals) 호출
        """

        pass

    def check_end_condition(self):
        """
        반환: True/False
        종료 조건:  ice_field.is_melted() or hunter_event.active가 True
        """

        pass
