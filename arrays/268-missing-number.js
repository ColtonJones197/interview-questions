/**
 * @param {number[]} nums
 * @return {number}
 */
// https://leetcode.com/problems/missing-number/
 var missingNumber = function(nums) {
    //gauss's law solution
    const sum = nums.reduce((total, currentVal) => total += currentVal);
    const n = nums.length + 1
    return (n * (n - 1) / 2) - sum; //uses a fun math trick to figure out what the sum should be
};