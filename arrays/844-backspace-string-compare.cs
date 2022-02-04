// https://leetcode.com/problems/backspace-string-compare/
public class Solution {
    private string GetTypedString(string s){
        var typedString = "";
        var backspaceCount = 0;
        for(int i = s.Length - 1; i > -1; i--)
        {
            if(s[i] == '#')
            {
                backspaceCount++;
            }
            else if(backspaceCount > 0) backspaceCount--;
            else if(backspaceCount == 0)
            {
                typedString = typedString + s[i];
            }
        }
        return typedString;
    }
    public bool BackspaceCompare(string s, string t) {
        return GetTypedString(s) == GetTypedString(t);
    }
}