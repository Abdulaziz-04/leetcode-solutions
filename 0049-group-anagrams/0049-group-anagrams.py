class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def calculate_frequency(word):
            word_freq=[0 for i in range(26)]
            for letter in word:
                word_freq[ord(letter)-ord('a')]+=1
            return tuple(word_freq)
        freq_map={}
        for word in strs:
            word_freq=calculate_frequency(word)
            if word_freq in freq_map:
                freq_map[word_freq].append(word)
            else:
                freq_map[word_freq]=[word]
        return freq_map.values()

        