class ArcticEnvironment:
    """빙하, 기온, 생물 밀도, 종료 이벤트를 묶어서 관리하는 환경 클래스."""

    def __init__(self):
        # 현재 시뮬레이션 턴 번호입니다. None이면 아직 시작 전 상태로 봅니다.
        self.turn = None

        # 현재 환경 온도입니다. update() 때 global_warming_rate만큼 증가합니다.
        self.temperature = None

        # 빙하 면적 대비 살아 있는 생물 수입니다.
        self.density = None

        # 한 턴이 지날 때마다 증가하는 온도 변화량입니다.
        self.global_warming_rate = None

        # 빙하 면적과 녹는 속도를 담당하는 IceField 객체입니다.
        self.ice_field = None

        # 사용자 입력으로 전체 생물을 제거하는 HunterEvent 객체입니다.
        self.hunter_event = None

    def update(self, animals):
        """
        환경을 한 턴 진행합니다.

        - 턴 수를 1 증가시킵니다.
        - 지구 온난화 비율이 설정되어 있으면 기온을 올립니다.
        - 빙하 객체가 있으면 빙하를 녹입니다.
        - 현재 살아 있는 생물 기준으로 밀도를 다시 계산합니다.
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
        살아 있는 생물 수를 빙하 면적으로 나누어 생물 밀도를 계산합니다.

        빙하 면적이 없거나 0이면 계산할 수 없으므로 density를 None으로 둡니다.
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
        사용자 입력 key를 HunterEvent에 전달하고, 이벤트가 활성화되면 생물을 모두 제거합니다.
        """
        if self.hunter_event is None:
            return None

        self.hunter_event.trigger(key)

        if self.hunter_event.active:
            self.hunter_event.eliminate_all(animals)

        return self.hunter_event.active

    def check_end_condition(self):
        """
        시뮬레이션 종료 여부를 반환합니다.

        종료 조건은 빙하가 최소 면적까지 녹았거나, 사냥 이벤트가 활성화된 경우입니다.
        """
        ice_melted = False
        hunter_active = False

        if self.ice_field is not None:
            ice_melted = self.ice_field.is_melted()

        if self.hunter_event is not None:
            hunter_active = bool(self.hunter_event.active)

        return ice_melted or hunter_active
