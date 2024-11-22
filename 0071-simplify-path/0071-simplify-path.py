class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for st in path.split("/"):
            if st == "":
                continue

            if st == ".." and len(stack):
                stack.pop()
            elif st != ".." and st != ".":
                stack.append(st)
        return "/" + "/".join(stack)