class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;
        int sChar[] = new int[26];
        int tChar[] = new int[26];
        for(int i=0; i<s.length(); i++){
            sChar[s.charAt(i)-'a']++;
        }
        for(int j=0; j<t.length(); j++){
            tChar[t.charAt(j)-'a']++;
        }
        return Arrays.equals(sChar, tChar);
    }
}
