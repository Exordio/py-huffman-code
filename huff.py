import collections
import heapq


class Node(collections.namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(collections.namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def encode(s):
    if s:
        h = []
        for ch, freq in collections.Counter(s).items():
            h.append((freq, len(h), Leaf(ch)))
        heapq.heapify(h)
        print(h)

        count = len(h)
        while len(h) > 1:
            freq1, _count1, left = heapq.heappop(h)
            freq2, _count2, right = heapq.heappop(h)
            heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
            count += 1

        [(_freq, _count, root)] = h
        code = {}
        root.walk(code, "")
    else:
        code = 'Empty str'
    return code


def huffman_decode(en, code):
    pointer = 0
    encoded_str = ''
    while pointer < len(en):
        for ch in code.keys():
            if en.startswith(code[ch], pointer):
                encoded_str += ch
                pointer += len(code[ch])
    return encoded_str


def main():
    s = input("input str : ")

    code = encode(s)
    encoded = "".join(code[ch] for ch in s)


    print(f" Symb dict {code}\n")

    for ch in sorted(code):
        print(f"{ch} : {code[ch]}")
    else:
        print("\nAll job done!")

    print(f"\nInput str : {s}")
    print(f"Encoded str : {encoded}\n")
    print(huffman_decode(encoded, code))

    print(code)


if __name__ == "__main__":
    main()
