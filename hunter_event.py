class HunterEvent:
    """특정 키 입력으로 생태계를 강제 종료시키는 사냥 이벤트 클래스."""

    def __init__(self):
        # 이벤트가 이미 발동했는지 나타냅니다.
        self.active = None

        # 이벤트를 발동시키는 입력 키입니다.
        self.trigger_key = None

    def trigger(self, key):
        """
        입력된 key가 trigger_key와 같으면 이벤트를 활성화합니다.

        trigger_key가 None이면 아직 발동 키가 정해지지 않은 상태로 보고 아무 일도 하지 않습니다.
        """
        if self.trigger_key is not None and key == self.trigger_key:
            self.active = True

        return self.active

    def eliminate_all(self, animals):
        """전달받은 모든 생물 객체의 alive 값을 False로 바꿉니다."""
        for animal in animals:
            # alive 속성이 있는 객체만 생물로 보고 제거 처리합니다.
            if hasattr(animal, "alive"):
                animal.alive = False

        return None
