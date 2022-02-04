// https://leetcode.com/problems/longest-substring-without-repeating-characters/
function lengthOfLongestSubstring(s: string): number {
    let max_length: number = 0;
    let longest: string = '';
    for(let i: number = 0; i < s.length; i++)
        {
            let current_letter = s[i];
            let existing_letter_index = longest.indexOf(current_letter);
            longest = existing_letter_index > -1 ? longest.substring(existing_letter_index + 1) + current_letter
                : longest + current_letter;
            max_length = Math.max(max_length, longest.length);
            
            
            /* refactored out, leaving in here just to remember
            if(current_longest_string.includes(s[i]))
            {
                let cutoff_index = current_longest_string.indexOf(s[i]) + 1;
                current_longest_string = current_longest_string.substring(cutoff_index) + s[i];
            }
            else
                current_longest_string += s[i];
            max_length = Math.max(max_length, current_longest_string.length);
            */
        }
    return max_length;
};