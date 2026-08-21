class Solution:

    def encode(self, strs: List[str]) -> str:
        combined_product = ""
        for word in strs:
            length = str(len(word))
            combined_product = combined_product + length + "#" + word
        return combined_product

    def decode(self, s: str) -> List[str]:
        final_list = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            final_list.append(word)
            i = j + 1 + length
        
        return final_list


