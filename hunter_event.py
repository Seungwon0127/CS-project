class HunterEvent:

    def __init__(self):

        # 이벤트 활성화 여부 (bool)
        self.active = None

        # 이벤트 발생 키 (str)
        self.trigger_key = None

    def trigger(self, key):
        """
        - key와 trigger_key 비교
        - 같으면 active 값을 True로 변경
        """
        if self.trigger_key is not None and key == self.trigger_key:
            self.active = True

        return self.active

    def eliminate_all(self, animals):
        """
        - 모든 생물의 alive 값을 False로 변경
        - 생태계를 강제로 종료
        """
        for animal in animals:
            if hasattr(animal, "alive"):
                animal.alive = False

        return None
