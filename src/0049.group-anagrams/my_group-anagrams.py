class Solution:
    def groupAnagrams(self, strs) :
        dict_key2list={}
        for s in strs:
            sort_s=tuple(sorted(s))
            if sort_s in dict_key2list:
                dict_key2list[sort_s].append(s)
            else:
                dict_key2list[sort_s]=[s]

        return [item for key,item in dict_key2list.items()]


string_list=["eat", "tea", "tan", "ate", "nat", "bat"]
s=Solution()
print(s.groupAnagrams(string_list))