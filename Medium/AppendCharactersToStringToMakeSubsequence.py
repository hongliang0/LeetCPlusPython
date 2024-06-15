class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_track, t_track = 0, 0
        while s_track < len(s) and t_track < len(t):
            if s[s_track] == t[t_track]:
                s_track += 1
                t_track += 1
            else:
                s_track += 1
        return len(t) - t_track
