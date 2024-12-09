from dataclasses import dataclass


def unpack(disk_map: str) -> list[int]:
    blocks = []
    for value, n in zip(map(int, list(disk_map)), range(len(disk_map))):
        if n % 2:
            blocks += [-1] * value
        else:
            blocks += [int(n / 2)] * value
    return blocks


def compactify(l: list[int]) -> list[int]:
    result = []
    i = 0
    n = len(l)
    j = n - 1
    while i <= j:
        while l[j] < 0:
            j -= 1
        if l[i] > -1:
            result.append(l[i])
        else:
            result.append(l[j])
            j -= 1
        i += 1
    return result


def checksum(l: list[int]) -> int:
    return sum(x * y for x, y in zip(l, range(len(l))))


@dataclass
class Block:
    id: int
    position: int
    length: int

    def __repr__(self):
        return f"({self.id}, {self.position}, {self.length})"


def list_blocks(disk_map: str) -> list[Block]:
    blocks = []
    for n in range(len(disk_map)):
        if not n % 2:
            block_id = n // 2
            position = sum(int(x) for x in disk_map[:n])
            length = int(disk_map[n])
            blocks.append(Block(block_id, position, length))
    return blocks


def block_compactify(blocks: list[Block]) -> list[Block]:
    n = len(blocks)
    i = n - 1
    block_id = n - 1
    while block_id > -1:
        while blocks[i].id != block_id:
            i -= 1
        for j in range(i):
            if (
                blocks[j + 1].position - blocks[j].position - blocks[j].length
                < blocks[i].length
            ):
                continue
            else:
                block = blocks.pop(i)
                block.position = blocks[j].position + blocks[j].length
                blocks.insert(j + 1, block)
                break
        block_id -= 1
    return blocks


def block_checksum(blocks: list[Block]):
    checksum = 0
    for block in blocks:
        for n in range(block.length):
            checksum += block.id * (block.position + n)
    return checksum


def process_part1(disk_map: str) -> int:
    return checksum(compactify(unpack(disk_map)))


def process_part2(disk_map: str) -> int:
    return block_checksum(block_compactify(list_blocks(disk_map)))


if __name__ == "__main__":
    with open("input.txt") as file:
        disk_map = file.read().strip()
    result1 = process_part1(disk_map)
    print(f"{result1}")
    result2 = process_part2(disk_map)
    print(f"{result2}")
