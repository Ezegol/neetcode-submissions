class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str((len(s))) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):

            j = i

            #Find the #
            while s[j] != "#":
                j += 1

            #Get the length
            length = int(s[i:j])

            # Move past #
            i = j + 1

            #Extract the exact length characters
            result.append(s[i:i + length])
            i += length
        return result
