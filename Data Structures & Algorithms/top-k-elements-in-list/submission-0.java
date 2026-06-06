class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int ans[] = new int[k];
        HashMap<Integer, Integer> map = new HashMap<>();
        LinkedHashMap<Integer, Integer> sortedMap = new LinkedHashMap<>();
        for(int i=0; i<nums.length; i++){
            map.putIfAbsent(nums[i],0);
            map.put(nums[i], map.get(nums[i])+1);
        }
        ArrayList<Integer> list = new ArrayList<Integer>(map.values());
        Collections.sort(list, Collections.reverseOrder()); 
        for (int num : list) {
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if (entry.getValue().equals(num)) {
                    sortedMap.put(entry.getKey(), num);
                }
            }
        }
        Set<Integer> keySet = sortedMap.keySet();
        ArrayList<Integer> keyIndex = new ArrayList<>(keySet);
        for(int i=0; i<k; i++){
            ans[i] = keyIndex.get(i);
        }
        return ans;
    }
}
