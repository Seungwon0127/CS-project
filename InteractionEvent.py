class InteractionEvent:
    """동물 사이에서 발생한 상호작용을 짧은 시간 동안 기록하는 이벤트 클래스."""

    def __init__(self):
        # 이벤트 종류입니다. 예: "eat", "move", "attack" 같은 문자열을 넣을 수 있습니다.
        self.event_type = None

        # 행동을 수행한 Animal 객체입니다.
        self.actor = None

        # 행동의 대상이 된 Animal 객체입니다.
        self.target = None

        # 이벤트가 발생한 월드 좌표입니다.
        self.location = None

        # 이벤트가 성공했는지 나타냅니다.
        self.success = None

        # 이벤트 표시가 남아 있을 시간입니다.
        self.timer = None

    def update(self):
        """이벤트 표시 시간을 1 줄이고, 0 아래로 내려가지 않도록 보정합니다."""
        if self.timer is not None:
            self.timer -= 1
            if self.timer < 0:
                self.timer = 0

        return None

    def is_finished(self):
        """timer가 0 이하가 되면 이벤트가 끝난 것으로 판단합니다."""
        if self.timer is None:
            return False

        return self.timer <= 0
