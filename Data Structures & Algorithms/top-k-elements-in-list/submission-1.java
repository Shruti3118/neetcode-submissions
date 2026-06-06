class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            hm.putIfAbsent(nums[i], 0);
            hm.put(nums[i], hm.get(nums[i])+1);
        }
        ArrayList<ArrayList<Integer>> countArr = new ArrayList<>();
        for(int i=0; i<=nums.length; i++){
            countArr.add(new ArrayList<Integer>());
        }
        for(Map.Entry<Integer, Integer> entry: hm.entrySet()){
            countArr.get(entry.getValue()).add(entry.getKey());
        }
        int ans[] = new int[k];
        for(int i=nums.length; i>0; i--){
            if(k==-1)
                return ans;
            if(countArr.get(i).size()>0){
                int j = countArr.get(i).size();
                while(j>0 && k>0){
                    ans[--k] = countArr.get(i).get(--j);
                }
            }
        }
        return ans;
    }
}
