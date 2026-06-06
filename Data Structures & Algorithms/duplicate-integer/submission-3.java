class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hashSet = new HashSet<Integer>();
        for(int i=0; i<nums.length; i++){
            hashSet.add(nums[i]);
        }
        if(hashSet.size()==nums.length)
            return false;
        return true;
    }
}
