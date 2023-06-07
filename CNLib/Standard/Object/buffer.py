class Buffer(list):
    def __init__(self, prealocate_size: int) -> None:
        super().__init__(0x00 for _ in range(prealocate_size))
