class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sets = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
                524288,
                1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912]
        str_sets = [str(i) for i in sets]
        len_str_sets = [len(i) for i in str_sets]

        str_n = str(n)
        len_n = len(str_n)
        srt_n = sorted(str_n)

        for i in range(len(len_str_sets)):
            if len_str_sets[i] == len_n:
                if sorted(str_sets[i]) == srt_n:
                    return True
        return False
