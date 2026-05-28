class ArcticEnvironment:

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
        if self.turn is not None:
            self.turn += 1

        if self.temperature is not None and self.global_warming_rate is not None:
            self.temperature += self.global_warming_rate

        if self.ice_field is not None:
            self.ice_field.melt()

        self.calculate_density(animals)

        return None

    def calculate_density(self, animals):
        """
        - alive가 True인 생물 수 계산
        - ice_field.area를 이용해 density 계산
        """
        alive_count = sum(1 for animal in animals if getattr(animal, "alive", False))
        area = getattr(self.ice_field, "area", None)

        if area is None or area == 0:
            self.density = None
        else:
            self.density = alive_count / area

        return self.density

    def handle_event(self, key, animals):
        """
        - hunter_event.trigger(key) 호출
        - hunter_event가 active 상태가 되면 eliminate_all(animals) 호출
        """
        if self.hunter_event is None:
            return None

        self.hunter_event.trigger(key)

        if self.hunter_event.active:
            self.hunter_event.eliminate_all(animals)

        return self.hunter_event.active

    def check_end_condition(self):
        """
        반환: True/False
        종료 조건:  ice_field.is_melted() or hunter_event.active가 True
        """
        ice_melted = False
        hunter_active = False

        if self.ice_field is not None:
            ice_melted = self.ice_field.is_melted()

        if self.hunter_event is not None:
            hunter_active = bool(self.hunter_event.active)

        return ice_melted or hunter_active
