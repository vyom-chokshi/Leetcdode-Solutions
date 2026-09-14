class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        parts = path.split("/")

        for i in parts:

            if i == "" or i == ".":
                continue

            elif i == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(i)

        return "/" + "/".join(stack)