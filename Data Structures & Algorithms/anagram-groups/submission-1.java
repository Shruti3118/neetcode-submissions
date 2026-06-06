class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, Integer> hm = new HashMap<>();
        List<List<String>> ans = new ArrayList<List<String>>();
        List<String> innerAns = new ArrayList<String>();
        innerAns.add(strs[0]);
        ans.add(innerAns);
        int unique = 0;
        hm.put((charArr(strs[0])), unique++);
        for(int i=1; i<strs.length; i++){
            String tempCharArr = charArr(strs[i]);
            if(!hm.containsKey(tempCharArr))
            {
                hm.put(tempCharArr,unique++);
                innerAns = new ArrayList<String>();
                innerAns.add(strs[i]);
                ans.add(innerAns);
            }
            else{
                ans.get(hm.get(tempCharArr)).add(strs[i]);
            }
        }
        return ans;
    }
    public String charArr(String s){
        int sCharArr[] = new int[26];
        for(int i=0; i<s.length(); i++){
            sCharArr[s.charAt(i)-'a']++;
        }
        return Arrays.toString(sCharArr);
    }
}
