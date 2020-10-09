import math

# assuming only lower case letters

def rabin_karp(string, target):
    if len(string) < len(target):
        return False
    elif len(string) > 1 and len(target) > 1:
        n = len(string)
        m = len(target)

        def hasher(s):
            s = list(s)
            hashcode = 0
            start = None
            for i in range(len(s)):
                val = ord(s[i]) * (26 ** i)
                if i == 0:
                    start = val
                hashcode += val
            return hashcode, start 

        target_hash, _ = hasher(target)
        idx = m-1
        window = string[:idx]
        window_hash, start = hasher(window)
        prev_start = start

        if window_hash != target_hash:
            while idx < n:
                new_letter = string[idx]
                new_hash, val = hasher(new_letter)
                prev_start = 

                window_hash += new_hash

                if window_hash == target_hash:
                    return True

                # get start of new hash
                window_hash = (window_hash - prev_start) * 26
                prev_start = window_hash
                
                idx += 1

            return False
        else:
            return True

print (rabin_karp("abc", "abc"))
print (rabin_karp("aabcde", "abc"))