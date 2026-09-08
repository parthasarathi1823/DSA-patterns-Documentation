class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
        int count=0;
        int max=0;

        for(int i: nums){

            if(i==0){
                count=0;
            }
            else{
                count++;
                max = Math.max(max,count);
            }
        }
        return max;
    }
}