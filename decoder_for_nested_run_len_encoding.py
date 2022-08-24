from string import punctuation


class Decoder:
    def __init__(self, s: str) -> None:
        self.output = ""
        self.num_stack = []
        self.temp_str_stack = []
        self.idx = 0
        self.s = s

    def decode(self) -> str:
        """decode. assume numbers are single digit numbers 1-9.
            e.g. 3[a]2[bc] -> 'aaabcbc' and 3[a2[c]] -> 'accaccacc' """
        if self.idx == len(self.s):
            if self.temp_str_stack:
                return self.output + self.temp_str_stack[0]
            else:
                return self.output
        else:
            if self.s[self.idx].isalpha():
                if self.temp_str_stack:
                    temp_str = self.temp_str_stack.pop()
                    self.temp_str_stack.append(temp_str + self.s[self.idx])
                else:
                    self.temp_str_stack.append(self.s[self.idx])
                self.idx += 1
            elif self.s[self.idx].isnumeric():
                self.num_stack.append(int(self.s[self.idx]))
                self.temp_str_stack.append("")
                self.idx += 2
            elif self.s[self.idx] == "]":
                num = self.num_stack.pop()
                string = self.temp_str_stack.pop()
                if not self.temp_str_stack:
                    self.output += num * string
                else:
                    temp_str2 = self.temp_str_stack.pop()
                    self.temp_str_stack.append(temp_str2 + num * string)
                self.idx += 1
            elif self.s[self.idx] in punctuation:
                if self.temp_str_stack:
                    temp_str = self.temp_str_stack.pop()
                    self.temp_str_stack.append(temp_str + self.s[self.idx])
                else:
                    self.temp_str_stack.append(self.s[self.idx])
                self.idx += 1

        return self.decode()


d = Decoder("3[a]2[bc]")
d2 = Decoder("2[abc]3[cd]ef")
d3 = Decoder("3[a2[c]]")
d4 = Decoder("Mi2[s]i2[s]i2[p]i3[.]3[yada-]hey")
print(d.decode())
print(d2.decode())
print(d3.decode())
print(d4.decode())


