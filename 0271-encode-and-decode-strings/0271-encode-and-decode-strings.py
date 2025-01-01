import base64

class Codec:
    def encode(self, strs: List[str]) -> str:
        new_strs = "à".join(strs)  # 문자 사이에 non-ascii(à) 을 넣고
        return base64.b64encode(new_strs.encode("UTF-8")).decode("ascii")  # 인코딩

    def decode(self, s: str) -> List[str]:
        new_strs = base64.b64decode(s.encode("ascii")).decode("UTF-8")
        return new_strs.split("à")
