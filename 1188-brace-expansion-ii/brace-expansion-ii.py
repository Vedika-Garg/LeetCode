class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_union():
            nonlocal i

            result = parse_concat()

            while i < len(expression) and expression[i] == ',':
                i += 1
                result |= parse_concat()

            return result

        def parse_concat():
            nonlocal i

            result = {""}

            while i < len(expression) and expression[i] not in ',}':

                if expression[i] == '{':
                    i += 1
                    curr = parse_union()
                    i += 1  # skip '}'

                else:
                    curr = {expression[i]}
                    i += 1

                result = {
                    a + b
                    for a in result
                    for b in curr
                }

            return result

        i = 0
        return sorted(parse_union())