class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        String[][] sortedStrs = new String[strs.length][2];
        for(int i=0; i<strs.length; i++){
            char[] strArray = strs[i].toCharArray();
            Arrays.sort(strArray);
            String str = new String(strArray);
            sortedStrs[i][0] = str;
            sortedStrs[i][1] = strs[i];
        }
        Arrays.sort(sortedStrs, (a,b) -> a[0].compareTo(b[0]));
        List<List<String>> ans = new ArrayList<List<String>>();
        int flag = 0;
        List<String> innerAns = new ArrayList<>();
        innerAns.add(sortedStrs[0][1]);
        for(int i=1; i<sortedStrs.length; i++){
            flag = (sortedStrs[i][0].equals(sortedStrs[i-1][0])) ? 1 : 0;
            if(flag==0)
            {
                ans.add(innerAns);
                innerAns = new ArrayList<String>();
                System.out.println(ans);
            }
            innerAns.add(sortedStrs[i][1]);
            System.out.println(innerAns);
        }
        ans.add(innerAns);
        return ans;
    }
}
