class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # each line should have maxWidth characters and is fully (left and right) justified
            # pad extra spaces when necessary to do this
        # extra spaces should be even
            # if spaces arent even btween words, assign more spaces to left first
        # last line of text left justified, no spaces between words
        # ["This is an", 
        # "example of text", 
        # "justification."]
        #  i
        #   chars = 15
          # iterate over words
          # when new word, add space
          # if can't finish word without > maxwidth, current word goes on new line
        
         # 1. determine which words should be on a line
         # 2. take words from first task and create a line.

        def getWords(i):
            current_line = []
            curr_length = 0

            while i < len(words) and curr_length + len(words[i]) <= maxWidth:
                current_line.append(words[i])
                curr_length += len(words[i]) + 1
                i += 1

            return current_line

        def createLine(line,i):
            base_length = -1
            for word in line:
                base_length += len(word) + 1
            extra_spaces = maxWidth - base_length

            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces
            
            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            spaces_needed = extra_spaces % word_count

            for j in range(spaces_needed):
                line[j] += " "
            
            for j in range(word_count):
                line[j] += " " * spaces_per_word
            
            return " ".join(line)


        ans = []
        i = 0
        while i < len(words):
            current_line = getWords(i)
            i += len(current_line)
            ans.append(createLine(current_line,i))
        return ans
            